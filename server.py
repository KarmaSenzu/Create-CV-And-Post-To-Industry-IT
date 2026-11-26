#!/usr/bin/env python3
"""
AGY Job Hunter & CV Commander - Multi-Profile Web Backend Server
Supports:
- Multi-profile management & instant switching
- Profile CRUD (Create, Read, Update, Delete) with CV upload
- Google Drive-style File & Folder Explorer (Browse, View, Delete, Drag & Drop Upload)
- Full job application tracking & tailored RenderCV generation
"""

import os
import sys
import glob
import json
import csv
import urllib.parse
import subprocess
import platform
import base64
import re
import shutil
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(WORKSPACE_DIR, "web")
PROFILES_DIR = os.path.join(WORKSPACE_DIR, "profiles")
RENDERCV_BIN = os.path.join(WORKSPACE_DIR, ".venv", "bin", "rendercv")
CONFIG_PATH = os.path.join(WORKSPACE_DIR, "config.json")
PORT = 8080

os.makedirs(PROFILES_DIR, exist_ok=True)

def get_active_profile_id():
    """Get active profile ID from config.json, defaulting to damar-fikrie."""
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                return cfg.get("active_profile", "damar-fikrie")
        except Exception:
            pass
    return "damar-fikrie"

def get_profile_dir(profile_id=None):
    """Get root directory for the specified or active profile."""
    pid = profile_id or get_active_profile_id()
    pdir = os.path.join(PROFILES_DIR, pid)
    if os.path.exists(pdir):
        return pdir
    return WORKSPACE_DIR

def get_tracker_path(profile_id=None):
    pdir = get_profile_dir(profile_id)
    p_tracker = os.path.join(pdir, "tracker.csv")
    if os.path.exists(p_tracker):
        return p_tracker
    return os.path.join(WORKSPACE_DIR, "tracker.csv")

def get_jobs_path(profile_id=None):
    pdir = get_profile_dir(profile_id)
    p_jobs = os.path.join(pdir, "jobs.csv")
    if os.path.exists(p_jobs):
        return p_jobs
    return os.path.join(WORKSPACE_DIR, "jobs", "jobs.csv")

def get_output_dir(profile_id=None):
    pdir = get_profile_dir(profile_id)
    p_out = os.path.join(pdir, "output")
    if os.path.exists(p_out):
        return p_out
    return os.path.join(WORKSPACE_DIR, "output")

def find_job_folder(job_id, profile_id=None):
    """Find specific output folder for a job_id within profile or fallback."""
    tracker_path = get_tracker_path(profile_id)
    pdir = get_profile_dir(profile_id)
    if os.path.exists(tracker_path):
        with open(tracker_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("job_id") == job_id:
                    cv_path = row.get("cv_path", "")
                    if cv_path:
                        # Try inside profile dir first
                        candidate = os.path.dirname(os.path.join(pdir, cv_path))
                        if os.path.exists(candidate):
                            return candidate
                        # Fallback to workspace root
                        candidate_root = os.path.dirname(os.path.join(WORKSPACE_DIR, cv_path))
                        if os.path.exists(candidate_root):
                            return candidate_root

    # Scan output folders
    out_dirs = [get_output_dir(profile_id), os.path.join(WORKSPACE_DIR, "output")]
    for od in out_dirs:
        candidates = glob.glob(os.path.join(od, "*", "*"))
        for c in candidates:
            job_md = os.path.join(c, "job.md")
            if os.path.exists(job_md):
                with open(job_md, "r", encoding="utf-8") as f:
                    if job_id in f.read():
                        return c
            clean_id = job_id.replace("glints-", "").replace("remoteok-", "").replace("remotive-", "")
            if clean_id in os.path.basename(c):
                return c
    return None

def get_job_meta(job_id, profile_id=None):
    """Get metadata for a job from jobs.csv or tracker.csv."""
    jobs_csv = get_jobs_path(profile_id)
    if os.path.exists(jobs_csv):
        with open(jobs_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("job_id") == job_id or row.get("id") == job_id:
                    if not row.get("role") and row.get("title"):
                        row["role"] = row["title"]
                    return row
    return {}

def format_file_size(size_bytes):
    """Format bytes into readable size."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"

class CommanderHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        # Static assets
        if path == "/" or path == "/index.html":
            self.serve_file(os.path.join(WEB_DIR, "index.html"), "text/html; charset=utf-8")
            return
        elif path.startswith("/static/") or path in ["/styles.css", "/app.js", "/favicon.ico"]:
            filename = os.path.basename(path)
            content_type = "text/plain"
            if filename.endswith(".css"):
                content_type = "text/css; charset=utf-8"
            elif filename.endswith(".js"):
                content_type = "application/javascript; charset=utf-8"
            elif filename.endswith(".svg"):
                content_type = "image/svg+xml"
            elif filename.endswith(".png"):
                content_type = "image/png"
            self.serve_file(os.path.join(WEB_DIR, filename), content_type)
            return

        # API Endpoints
        if path == "/api/stats":
            self.handle_api_stats()
        elif path == "/api/jobs":
            self.handle_api_jobs()
        elif path.startswith("/api/job/"):
            job_id = path.replace("/api/job/", "")
            self.handle_api_job_detail(job_id)
        elif path.startswith("/api/pdf/"):
            job_id = path.replace("/api/pdf/", "")
            self.handle_api_pdf(job_id)
        elif path == "/api/projects":
            self.handle_api_projects()
        elif path == "/api/logs":
            self.handle_api_logs()
        # Multi-Profile API
        elif path == "/api/profiles":
            self.handle_api_profiles_list()
        # Google Drive-Style Explorer API
        elif path == "/api/explorer":
            req_path = query.get("path", [""])[0]
            self.handle_api_explorer(req_path)
        elif path == "/api/explorer/file":
            req_path = query.get("path", [""])[0]
            self.handle_api_explorer_file(req_path)
        else:
            self.send_error(404, "Endpoint not found")

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(length) if length > 0 else b"{}"
        try:
            payload = json.loads(post_data.decode("utf-8"))
        except Exception:
            payload = {}

        if path == "/api/action":
            self.handle_api_action(payload)
        elif path == "/api/search":
            self.handle_api_search(payload)
        # Profile Management
        elif path == "/api/profiles/active":
            self.handle_api_profile_switch(payload)
        elif path == "/api/profiles/create":
            self.handle_api_profile_create(payload)
        elif path == "/api/profiles/update":
            self.handle_api_profile_update(payload)
        elif path == "/api/profiles/delete":
            self.handle_api_profile_delete(payload)
        # Drive Explorer CRUD
        elif path == "/api/explorer/delete":
            self.handle_api_explorer_delete(payload)
        elif path == "/api/explorer/upload":
            self.handle_api_explorer_upload(payload)
        # Job CRUD
        elif path == "/api/jobs/delete":
            self.handle_api_job_delete(payload)
        elif path == "/api/rerender":
            self.handle_api_rerender(payload)
        else:
            self.send_error(404, "Endpoint not found")

    def serve_file(self, file_path, content_type):
        if not os.path.exists(file_path):
            self.send_error(404, f"File {os.path.basename(file_path)} not found")
            return
        with open(file_path, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        self.wfile.write(data)

    # -------------------------------------------------------------
    # Multi-Profile Handlers
    # -------------------------------------------------------------
    def handle_api_profiles_list(self):
        active_id = get_active_profile_id()
        profiles = []

        dirs = sorted(glob.glob(os.path.join(PROFILES_DIR, "*")))
        for p in dirs:
            if os.path.isdir(p):
                pj = os.path.join(p, "profile.json")
                if os.path.exists(pj):
                    try:
                        with open(pj, "r", encoding="utf-8") as f:
                            pdata = json.load(f)
                            pdata["is_active"] = (pdata.get("id") == active_id)

                            # Count jobs
                            t_path = os.path.join(p, "tracker.csv")
                            total_jobs = 0
                            pending_count = 0
                            applied_count = 0
                            if os.path.exists(t_path):
                                with open(t_path, "r", encoding="utf-8") as tf:
                                    reader = csv.DictReader(tf)
                                    for row in reader:
                                        total_jobs += 1
                                        st = row.get("status")
                                        if st == "pending_review":
                                            pending_count += 1
                                        elif st == "applied":
                                            applied_count += 1

                            pdata["stats"] = {
                                "total_jobs": total_jobs,
                                "pending_jobs": pending_count,
                                "applied_jobs": applied_count
                            }
                            profiles.append(pdata)
                    except Exception:
                        pass

        self.send_json({
            "active_profile": active_id,
            "profiles": profiles
        })

    def handle_api_profile_switch(self, payload):
        target_id = payload.get("profile_id") or payload.get("id")
        if not target_id:
            self.send_json({"success": False, "error": "Profile ID is required"}, status=400)
            return

        target_dir = os.path.join(PROFILES_DIR, target_id)
        if not os.path.exists(target_dir):
            self.send_json({"success": False, "error": f"Profile {target_id} not found"}, status=404)
            return

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump({"active_profile": target_id}, f, indent=2)

        self.send_json({
            "success": True,
            "active_profile": target_id,
            "message": f"Berhasil beralih ke profil {target_id}!"
        })

    def handle_api_profile_create(self, payload):
        name = payload.get("name", "").strip()
        if not name:
            self.send_json({"success": False, "error": "Nama lengkap wajib diisi"}, status=400)
            return

        slug = payload.get("id", "").strip().lower()
        if not slug:
            slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

        target_dir = os.path.join(PROFILES_DIR, slug)
        if os.path.exists(target_dir):
            self.send_json({"success": False, "error": f"Profil dengan ID '{slug}' sudah ada"}, status=400)
            return

        os.makedirs(target_dir, exist_ok=True)
        os.makedirs(os.path.join(target_dir, "output"), exist_ok=True)

        # Init CSVs
        tracker_header = "job_id,category,company,role,cv_path,status,applied_date,last_update,notes\n"
        with open(os.path.join(target_dir, "tracker.csv"), "w", encoding="utf-8") as f:
            f.write(tracker_header)

        jobs_header = "id,source,title,company,category,category_secondary,location,work_mode,salary,experience_years,level,must_have,nice_to_have,responsibilities,language,posted_date,deadline,job_url,apply_url,company_url,careers_url,company_profile_url,retrieved_at,source_status,match_score,missing_skills,status\n"
        with open(os.path.join(target_dir, "jobs.csv"), "w", encoding="utf-8") as f:
            f.write(jobs_header)

        # Handle uploaded CV file if present
        cv_base64 = payload.get("cv_file_base64")
        if cv_base64:
            try:
                # Remove header if data URI
                if "," in cv_base64:
                    cv_base64 = cv_base64.split(",")[1]
                cv_bytes = base64.b64decode(cv_base64)
                with open(os.path.join(target_dir, "cv_lama.pdf"), "wb") as f:
                    f.write(cv_bytes)
            except Exception as e:
                print(f"Error saving uploaded CV: {e}")

        # Construct profile.json
        avatar = "".join([part[0].upper() for part in name.split()[:2]]) or "ID"
        skills = payload.get("skills", [])
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(",") if s.strip()]

        target_roles = payload.get("target_roles", [])
        if isinstance(target_roles, str):
            target_roles = [r.strip() for r in target_roles.split(",") if r.strip()]

        glints_keywords = payload.get("glints_keywords", [])
        if isinstance(glints_keywords, str):
            glints_keywords = [k.strip() for k in glints_keywords.split(",") if k.strip()]

        profile_data = {
            "id": slug,
            "name": name,
            "title": payload.get("title", "Professional"),
            "industry": payload.get("industry", "General"),
            "industry_tag": payload.get("industry_tag", payload.get("industry", "General")),
            "avatar": avatar,
            "education": payload.get("education", ""),
            "university": payload.get("university", ""),
            "gpa": payload.get("gpa", ""),
            "location": payload.get("location", "Indonesia"),
            "phone": payload.get("phone", ""),
            "email": payload.get("email", ""),
            "website": payload.get("website", ""),
            "github": payload.get("github", ""),
            "linkedin": payload.get("linkedin", ""),
            "certification": payload.get("certification", ""),
            "target_roles": target_roles or [payload.get("title", "Professional")],
            "glints_keywords": glints_keywords or [payload.get("title", "Professional")],
            "skills": skills
        }

        with open(os.path.join(target_dir, "profile.json"), "w", encoding="utf-8") as f:
            json.dump(profile_data, f, indent=2)

        # Generate starter master.yaml
        master_yaml = f"""# Master facts for {name}
cv:
  name: {name}
  headline: "{payload.get('title', 'Professional')}"
  location: {payload.get('location', 'Indonesia')}
  email: {payload.get('email', '')}
  phone: "{payload.get('phone', '')}"
  website: {payload.get('website', '')}

summary_facts:
  - {payload.get('title', 'Professional')} dengan pengalaman dalam industri {payload.get('industry', 'Teknik')}.
  - Menguasai {', '.join(skills[:5]) if skills else 'keahlian di bidang terkait'}.

education:
  - institution: {payload.get('university', 'Perguruan Tinggi')}
    area: {payload.get('education', 'Sarjana')}
    degree: {payload.get('education', 'Sarjana')}
    highlights:
      - "IPK: {payload.get('gpa', '3.50')}"

technical_skills:
  - label: Core Skills
    details: "{', '.join(skills) if skills else 'Spesialisasi Teknis'}"
"""
        with open(os.path.join(target_dir, "master.yaml"), "w", encoding="utf-8") as f:
            f.write(master_yaml)

        # Switch to new profile automatically if requested
        if payload.get("switch_active", True):
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump({"active_profile": slug}, f, indent=2)

        self.send_json({
            "success": True,
            "profile": profile_data,
            "message": f"Profil {name} ({slug}) berhasil dibuat dan diaktifkan!"
        })

    def handle_api_profile_update(self, payload):
        slug = payload.get("id")
        if not slug:
            self.send_json({"success": False, "error": "Profile ID is required"}, status=400)
            return

        target_dir = os.path.join(PROFILES_DIR, slug)
        if not os.path.exists(target_dir):
            self.send_json({"success": False, "error": f"Profile {slug} not found"}, status=404)
            return

        pj_path = os.path.join(target_dir, "profile.json")
        current_data = {}
        if os.path.exists(pj_path):
            with open(pj_path, "r", encoding="utf-8") as f:
                current_data = json.load(f)

        # Update fields
        for k in ["name", "title", "industry", "industry_tag", "education", "university",
                  "gpa", "location", "phone", "email", "website", "github", "linkedin",
                  "certification"]:
            if k in payload:
                current_data[k] = payload[k]

        if "skills" in payload:
            skills = payload["skills"]
            if isinstance(skills, str):
                skills = [s.strip() for s in skills.split(",") if s.strip()]
            current_data["skills"] = skills

        if "target_roles" in payload:
            roles = payload["target_roles"]
            if isinstance(roles, str):
                roles = [r.strip() for r in roles.split(",") if r.strip()]
            current_data["target_roles"] = roles

        if "glints_keywords" in payload:
            keywords = payload["glints_keywords"]
            if isinstance(keywords, str):
                keywords = [k.strip() for k in keywords.split(",") if k.strip()]
            current_data["glints_keywords"] = keywords

        with open(pj_path, "w", encoding="utf-8") as f:
            json.dump(current_data, f, indent=2)

        self.send_json({
            "success": True,
            "profile": current_data,
            "message": f"Profil {current_data.get('name')} berhasil diperbarui!"
        })

    def handle_api_profile_delete(self, payload):
        target_id = payload.get("profile_id")
        if not target_id:
            self.send_json({"success": False, "error": "Profile ID is required"}, status=400)
            return

        dirs = [d for d in glob.glob(os.path.join(PROFILES_DIR, "*")) if os.path.isdir(d)]
        if len(dirs) <= 1:
            self.send_json({"success": False, "error": "Tidak dapat menghapus satu-satunya profil yang tersisa."}, status=400)
            return

        target_dir = os.path.join(PROFILES_DIR, target_id)
        if not os.path.exists(target_dir):
            self.send_json({"success": False, "error": "Profil tidak ditemukan"}, status=404)
            return

        shutil.rmtree(target_dir)

        # If deleted was active, switch to first remaining
        active_id = get_active_profile_id()
        if active_id == target_id:
            remaining = [os.path.basename(d) for d in glob.glob(os.path.join(PROFILES_DIR, "*")) if os.path.isdir(d)]
            new_active = remaining[0] if remaining else "damar-fikrie"
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump({"active_profile": new_active}, f, indent=2)
            active_id = new_active

        self.send_json({
            "success": True,
            "active_profile": active_id,
            "message": f"Profil '{target_id}' berhasil dihapus!"
        })

    # -------------------------------------------------------------
    # Google Drive-Style Explorer Handlers
    # -------------------------------------------------------------
    def handle_api_explorer(self, sub_path):
        pdir = get_profile_dir()
        clean_sub = sub_path.strip("/").replace("\\", "/")

        # Prevent traversal
        resolved = os.path.abspath(os.path.join(pdir, clean_sub))
        if not resolved.startswith(os.path.abspath(pdir)) and not resolved.startswith(os.path.abspath(WORKSPACE_DIR)):
            self.send_json({"success": False, "error": "Akses path tidak diizinkan"}, status=403)
            return

        if not os.path.exists(resolved) or not os.path.isdir(resolved):
            resolved = pdir
            clean_sub = ""

        # Build breadcrumbs
        parts = clean_sub.split("/") if clean_sub else []
        breadcrumbs = [{"name": "Root Profil", "path": ""}]
        accum = []
        for p in parts:
            if p:
                accum.append(p)
                breadcrumbs.append({"name": p, "path": "/".join(accum)})

        items = []
        try:
            for entry in sorted(os.scandir(resolved), key=lambda e: (not e.is_dir(), e.name.lower())):
                if entry.name.startswith("."):
                    continue

                rel_item_path = os.path.relpath(entry.path, pdir).replace("\\", "/")
                is_dir = entry.is_dir()
                stat = entry.stat()

                ext = ""
                if not is_dir and "." in entry.name:
                    ext = entry.name.rsplit(".", 1)[1].lower()

                items.append({
                    "name": entry.name,
                    "path": rel_item_path,
                    "is_dir": is_dir,
                    "type": "folder" if is_dir else "file",
                    "ext": ext,
                    "size": format_file_size(stat.st_size) if not is_dir else "--",
                    "size_bytes": stat.st_size if not is_dir else 0,
                    "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                    "is_deletable": entry.name not in ["profile.json", "master.yaml"]
                })
        except Exception as e:
            print(f"Error scanning dir: {e}")

        self.send_json({
            "current_path": clean_sub,
            "profile_id": get_active_profile_id(),
            "breadcrumbs": breadcrumbs,
            "items": items
        })

    def handle_api_explorer_file(self, rel_path):
        pdir = get_profile_dir()
        clean_rel = rel_path.strip("/").replace("\\", "/")

        resolved = os.path.abspath(os.path.join(pdir, clean_rel))
        # Also check root workspace
        if not os.path.exists(resolved):
            resolved = os.path.abspath(os.path.join(WORKSPACE_DIR, clean_rel))

        if not resolved.startswith(os.path.abspath(pdir)) and not resolved.startswith(os.path.abspath(WORKSPACE_DIR)):
            self.send_error(403, "Access denied")
            return

        if not os.path.exists(resolved) or os.path.isdir(resolved):
            self.send_error(404, "File not found")
            return

        ext = resolved.rsplit(".", 1)[-1].lower() if "." in resolved else ""
        content_type = "application/octet-stream"
        if ext == "pdf":
            content_type = "application/pdf"
        elif ext in ["png", "jpg", "jpeg", "webp"]:
            content_type = f"image/{ext}"
        elif ext == "svg":
            content_type = "image/svg+xml"
        elif ext in ["md", "markdown", "txt", "log"]:
            content_type = "text/markdown; charset=utf-8"
        elif ext in ["yaml", "yml"]:
            content_type = "text/yaml; charset=utf-8"
        elif ext == "json":
            content_type = "application/json; charset=utf-8"
        elif ext == "csv":
            content_type = "text/csv; charset=utf-8"

        with open(resolved, "rb") as f:
            data = f.read()

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        # Allow inline viewing for PDF and text
        if ext in ["pdf", "png", "jpg", "jpeg", "svg", "md", "txt", "yaml", "json"]:
            self.send_header("Content-Disposition", f"inline; filename=\"{os.path.basename(resolved)}\"")
        else:
            self.send_header("Content-Disposition", f"attachment; filename=\"{os.path.basename(resolved)}\"")
        self.end_headers()
        self.wfile.write(data)

    def handle_api_explorer_delete(self, payload):
        pdir = get_profile_dir()
        paths = payload.get("paths", [])
        if isinstance(paths, str):
            paths = [paths]

        deleted = []
        errors = []
        for p in paths:
            clean_rel = p.strip("/").replace("\\", "/")
            if not clean_rel or clean_rel in ["profile.json", "master.yaml"]:
                errors.append(f"{clean_rel}: Berkas inti profil dilindungi")
                continue

            resolved = os.path.abspath(os.path.join(pdir, clean_rel))
            if not resolved.startswith(os.path.abspath(pdir)) and not resolved.startswith(os.path.abspath(WORKSPACE_DIR)):
                errors.append(f"{clean_rel}: Akses ditolak")
                continue

            if os.path.exists(resolved):
                try:
                    if os.path.isdir(resolved):
                        shutil.rmtree(resolved)
                    else:
                        os.remove(resolved)
                    deleted.append(clean_rel)
                except Exception as e:
                    errors.append(f"{clean_rel}: {str(e)}")

        self.send_json({
            "success": len(deleted) > 0,
            "deleted": deleted,
            "errors": errors,
            "message": f"Berhasil menghapus {len(deleted)} item." if deleted else "Tidak ada item yang dihapus."
        })

    def handle_api_explorer_upload(self, payload):
        pdir = get_profile_dir()
        target_dir = payload.get("target_dir", "").strip("/").replace("\\", "/")
        filename = payload.get("filename", "").strip()
        file_base64 = payload.get("file_base64", "")

        if not filename or not file_base64:
            self.send_json({"success": False, "error": "Nama berkas dan data wajib diisi"}, status=400)
            return

        dest_dir = os.path.abspath(os.path.join(pdir, target_dir))
        if not dest_dir.startswith(os.path.abspath(pdir)):
            dest_dir = pdir

        os.makedirs(dest_dir, exist_ok=True)
        dest_file = os.path.join(dest_dir, filename)

        try:
            if "," in file_base64:
                file_base64 = file_base64.split(",")[1]
            raw_data = base64.b64decode(file_base64)
            with open(dest_file, "wb") as f:
                f.write(raw_data)

            self.send_json({
                "success": True,
                "filename": filename,
                "path": os.path.relpath(dest_file, pdir),
                "size": format_file_size(len(raw_data)),
                "message": f"Berkas '{filename}' berhasil diunggah ke Drive!"
            })
        except Exception as e:
            self.send_json({"success": False, "error": str(e)}, status=500)

    # -------------------------------------------------------------
    # Job Delete CRUD
    # -------------------------------------------------------------
    def handle_api_job_delete(self, payload):
        job_id = payload.get("job_id")
        if not job_id:
            self.send_json({"success": False, "error": "Job ID is required"}, status=400)
            return

        # 1. Delete folder
        folder = find_job_folder(job_id)
        folder_deleted = False
        if folder and os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                folder_deleted = True
            except Exception as e:
                print(f"Error removing folder: {e}")

        # 2. Remove from active profile tracker and root tracker
        tracker_paths = [get_tracker_path(), os.path.join(WORKSPACE_DIR, "tracker.csv")]
        for tp in set(tracker_paths):
            if os.path.exists(tp):
                rows = []
                with open(tp, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    fieldnames = reader.fieldnames
                    for r in reader:
                        if r.get("job_id") != job_id:
                            rows.append(r)
                with open(tp, "w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

        # 3. Remove from active profile jobs.csv and root jobs.csv
        jobs_paths = [get_jobs_path(), os.path.join(WORKSPACE_DIR, "jobs", "jobs.csv")]
        for jp in set(jobs_paths):
            if os.path.exists(jp):
                rows = []
                with open(jp, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    fieldnames = reader.fieldnames
                    for r in reader:
                        if r.get("id") != job_id and r.get("job_id") != job_id:
                            rows.append(r)
                with open(jp, "w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

        self.send_json({
            "success": True,
            "job_id": job_id,
            "folder_deleted": folder_deleted,
            "message": f"Lowongan '{job_id}' dan foldernya berhasil dihapus dari sistem."
        })

    def handle_api_rerender(self, payload):
        job_id = payload.get("job_id")
        yaml_content = payload.get("cv_yaml", "")
        if not job_id:
            self.send_json({"success": False, "error": "Job ID is required"}, status=400)
            return

        folder = find_job_folder(job_id)
        if not folder or not os.path.exists(folder):
            self.send_json({"success": False, "error": f"Folder job {job_id} tidak ditemukan"}, status=404)
            return

        cv_yaml_path = os.path.join(folder, "cv.yaml")
        if yaml_content.strip():
            with open(cv_yaml_path, "w", encoding="utf-8") as f:
                f.write(yaml_content)

        rendercv_bin = os.path.join(WORKSPACE_DIR, ".venv", "bin", "rendercv")
        if not os.path.exists(rendercv_bin):
            rendercv_bin = "rendercv"

        try:
            res = subprocess.run([rendercv_bin, "render", "cv.yaml"], cwd=folder, capture_output=True, text=True)
            if res.returncode != 0:
                self.send_json({
                    "success": False,
                    "error": f"RenderCV gagal dikompilasi: {res.stderr or res.stdout}"
                }, status=500)
                return

            # Copy latest PDF to job root
            out_dir = os.path.join(folder, "rendercv_output")
            pdfs = glob.glob(os.path.join(out_dir, "*.pdf"))
            pdf_filename = ""
            if pdfs:
                latest_pdf = pdfs[0]
                pdf_filename = os.path.basename(latest_pdf)
                target_pdf = os.path.join(folder, pdf_filename)
                shutil.copy2(latest_pdf, target_pdf)

            self.send_json({
                "success": True,
                "job_id": job_id,
                "pdf_filename": pdf_filename,
                "pdf_url": f"/api/pdf/{job_id}?t={int(datetime.now().timestamp())}",
                "message": "PDF CV berhasil dikompilasi ulang secara instan!"
            })
        except Exception as e:
            self.send_json({"success": False, "error": str(e)}, status=500)

    # -------------------------------------------------------------
    # Standard Job Hunter Handlers
    # -------------------------------------------------------------
    def handle_api_stats(self):
        tracker_path = get_tracker_path()
        jobs_path = get_jobs_path()
        pdir = get_profile_dir()

        total_scanned = 0
        if os.path.exists(jobs_path):
            with open(jobs_path, "r", encoding="utf-8") as f:
                total_scanned = max(0, sum(1 for _ in f) - 1)

        counts = {}
        total_tracked = 0
        if os.path.exists(tracker_path):
            with open(tracker_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    status = row.get("status", "pending_review")
                    total_tracked += 1
                    counts[status] = counts.get(status, 0) + 1

        # Profile metadata
        profile_json_path = os.path.join(pdir, "profile.json")
        profile_info = {
            "id": get_active_profile_id(),
            "name": "Damar Fikrie",
            "education": "Sarjana Komputer (S.Kom.) — Fresh Graduate",
            "university": "Universitas Bina Sarana Informatika",
            "gpa": "3.85 / 4.00 (Cum Laude)",
            "location": "Jakarta Selatan, Indonesia",
            "certification": "BNSP Pengembang Perangkat Lunak (Program Analyst)",
            "verified_projects": 15
        }
        if os.path.exists(profile_json_path):
            try:
                with open(profile_json_path, "r", encoding="utf-8") as pf:
                    profile_info.update(json.load(pf))
            except Exception:
                pass

        stats = {
            "active_profile": get_active_profile_id(),
            "total_scanned": total_scanned,
            "total_tracked": total_tracked,
            "pending_review": counts.get("pending_review", 0),
            "ready_to_submit": counts.get("ready_to_submit", 0),
            "applied": counts.get("applied", 0),
            "in_pipeline": (
                counts.get("screening", 0) +
                counts.get("test_assigned", 0) +
                counts.get("interview_hr", 0) +
                counts.get("interview_tech", 0)
            ),
            "interview": counts.get("interview_hr", 0) + counts.get("interview_tech", 0),
            "offered": counts.get("offered", 0),
            "rejected": counts.get("rejected", 0),
            "skipped": counts.get("skipped", 0),
            "profile": profile_info
        }
        self.send_json(stats)

    def handle_api_jobs(self):
        tracker_path = get_tracker_path()
        jobs_path = get_jobs_path()

        jobs_meta = {}
        if os.path.exists(jobs_path):
            with open(jobs_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    jid = row.get("job_id") or row.get("id")
                    if jid:
                        jobs_meta[jid] = row

        job_list = []
        if os.path.exists(tracker_path):
            with open(tracker_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    jid = row.get("job_id")
                    meta = jobs_meta.get(jid, {})
                    folder = find_job_folder(jid)

                    pdf_files = []
                    readme_exists = False
                    gap_exists = False
                    if folder and os.path.exists(folder):
                        pdf_files = [os.path.basename(p) for p in glob.glob(os.path.join(folder, "*.pdf"))]
                        readme_exists = os.path.exists(os.path.join(folder, "README.md"))
                        gap_exists = os.path.exists(os.path.join(folder, "gap_report.md"))

                    item = {
                        "job_id": jid,
                        "company": row.get("company") or meta.get("company", "Company"),
                        "role": row.get("role") or meta.get("role", "Role"),
                        "category": row.get("category") or meta.get("category", "01-fullstack"),
                        "status": row.get("status", "pending_review"),
                        "applied_date": row.get("applied_date", "-"),
                        "last_update": row.get("last_update", "-"),
                        "notes": row.get("notes", ""),
                        "salary": meta.get("salary", "Kompetitif"),
                        "location": meta.get("location", "Indonesia"),
                        "work_mode": meta.get("work_mode", "Hybrid / Remote"),
                        "job_url": meta.get("job_url", ""),
                        "match_score": 100,
                        "has_pdf": len(pdf_files) > 0,
                        "pdf_filename": pdf_files[0] if pdf_files else None,
                        "pdf_url": f"/api/pdf/{jid}" if pdf_files else None,
                        "has_readme": readme_exists,
                        "has_gap_report": gap_exists
                    }
                    job_list.append(item)

        self.send_json(job_list)

    def handle_api_job_detail(self, job_id):
        folder = find_job_folder(job_id)
        meta = get_job_meta(job_id)
        tracker_item = None
        tracker_path = get_tracker_path()
        if os.path.exists(tracker_path):
            with open(tracker_path, "r", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if row.get("job_id") == job_id:
                        tracker_item = row
                        break

        if not folder or not os.path.exists(folder):
            status = tracker_item.get("status", "applied") if tracker_item else "applied"
            applied_date = tracker_item.get("applied_date", "-") if tracker_item else "-"
            notes = tracker_item.get("notes", "") if tracker_item else ""
            company = (tracker_item.get("company") if tracker_item else None) or meta.get("company", "Company")
            role = (tracker_item.get("role") if tracker_item else None) or meta.get("role", "Role")
            job_url = meta.get("job_url", "")

            detail = {
                "job_id": job_id,
                "folder": None,
                "absolute_folder": None,
                "absolute_pdf_path": None,
                "meta": meta,
                "readme_md": f"# {role} — {company}\n\n> Status: **{status.upper()}** (Dilamar pada: {applied_date})\n\n- **Catatan**: {notes}\n- **Portal Resmi**: [Buka Lowongan di Glints]({job_url})\n\n*Informasi lamaran tersimpan permanen di database tracker sistem.*",
                "gap_report_md": f"# Riwayat Lamaran — {role} ({company})\n\nLamaran resmi telah tersimpan di sistem dengan status **{status}** pada tanggal **{applied_date}**.\n\n- **Catatan Pelamar**: {notes}",
                "job_md": meta.get("responsibilities", ""),
                "cv_yaml": "# File build lokal telah dibersihkan sesuai konfigurasi penyimpanan hemat disk",
                "log_md": "",
                "pdf_filename": None,
                "pdf_url": None,
                "pdf_download_url": None,
                "archived": True
            }
            self.send_json(detail)
            return

        def read_file_safe(filename):
            fp = os.path.join(folder, filename)
            if os.path.exists(fp):
                with open(fp, "r", encoding="utf-8") as f:
                    return f.read()
            return ""

        pdf_files = [os.path.basename(p) for p in glob.glob(os.path.join(folder, "*.pdf"))]

        detail = {
            "job_id": job_id,
            "folder": os.path.relpath(folder, WORKSPACE_DIR),
            "absolute_folder": os.path.abspath(folder),
            "absolute_pdf_path": os.path.abspath(os.path.join(folder, pdf_files[0])) if pdf_files else None,
            "meta": meta,
            "readme_md": read_file_safe("README.md"),
            "gap_report_md": read_file_safe("gap_report.md"),
            "job_md": read_file_safe("job.md"),
            "cv_yaml": read_file_safe("cv.yaml"),
            "log_md": read_file_safe("log.md"),
            "pdf_filename": pdf_files[0] if pdf_files else None,
            "pdf_url": f"/api/pdf/{job_id}" if pdf_files else None,
            "pdf_download_url": f"/api/pdf/{job_id}" if pdf_files else None,
            "archived": False
        }
        self.send_json(detail)

    def handle_api_pdf(self, job_id):
        folder = find_job_folder(job_id)
        if not folder or not os.path.exists(folder):
            self.send_error(404, f"Berkas CV PDF untuk lowongan {job_id} tidak ditemukan.")
            return

        pdf_files = glob.glob(os.path.join(folder, "*.pdf"))
        if not pdf_files:
            self.send_error(404, "PDF belum selesai dikompilasi")
            return

        target_pdf = pdf_files[0]
        with open(target_pdf, "rb") as f:
            pdf_data = f.read()

        self.send_response(200)
        self.send_header("Content-Type", "application/pdf")
        self.send_header("Content-Length", str(len(pdf_data)))
        self.send_header("Content-Disposition", f"inline; filename=\"{os.path.basename(target_pdf)}\"")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(pdf_data)

    def handle_api_projects(self):
        pdir = get_profile_dir()
        master_path = os.path.join(pdir, "master.yaml")
        if not os.path.exists(master_path):
            master_path = os.path.join(WORKSPACE_DIR, "master", "master.yaml")

        projects = []
        if os.path.exists(master_path):
            try:
                import ruamel.yaml
                yaml = ruamel.yaml.YAML()
                with open(master_path, "r", encoding="utf-8") as f:
                    data = yaml.load(f)
                    projects = data.get("projects", [])
            except Exception:
                pass
        self.send_json(projects)

    def handle_api_logs(self):
        log_path = os.path.join(WORKSPACE_DIR, "logs", "activity_log.csv")
        logs = []
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    logs.append(row)
        logs.reverse()
        self.send_json(logs[:40])

    def handle_api_action(self, payload):
        action = payload.get("action")
        job_id = payload.get("job_id")
        notes = payload.get("notes", "")

        meta = get_job_meta(job_id)
        company = meta.get("company", "Perusahaan")
        role = meta.get("role") or meta.get("title", "Posisi")

        def sync_tracker_update(predicate_fn):
            t_paths = [get_tracker_path()]
            if get_active_profile_id() == "damar-fikrie":
                t_paths.append(os.path.join(WORKSPACE_DIR, "tracker.csv"))
            for tp in set(t_paths):
                if os.path.exists(tp):
                    rows = []
                    updated = False
                    with open(tp, "r", encoding="utf-8") as f:
                        reader = csv.DictReader(f)
                        fieldnames = reader.fieldnames
                        for row in reader:
                            if predicate_fn(row):
                                updated = True
                            rows.append(row)
                    if updated and fieldnames:
                        with open(tp, "w", encoding="utf-8", newline="") as f:
                            writer = csv.DictWriter(f, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(rows)

        if action == "start_apply":
            job_url = meta.get("job_url") or meta.get("apply_url")
            if not job_url:
                job_url = f"https://glints.com/id/explore?keywords={urllib.parse.quote(role)}"

            try:
                if platform.system() == "Darwin":
                    subprocess.run(["open", job_url])
                elif platform.system() == "Windows":
                    subprocess.run(["start", job_url], shell=True)
                else:
                    subprocess.run(["xdg-open", job_url])
            except Exception as e:
                print(f"Error launching browser: {e}")

            def apply_step1(row):
                if row.get("job_id") == job_id and row.get("status") == "pending_review":
                    row["status"] = "ready_to_submit"
                    row["last_update"] = datetime.now().strftime("%Y-%m-%d")
                    return True
                return False

            sync_tracker_update(apply_step1)

            self.send_json({
                "success": True,
                "action": "start_apply",
                "job_id": job_id,
                "job_url": job_url,
                "message": f"Halaman resmi {company} dibuka. Silakan unggah PDF CV dan klik Kirim di portal tersebut."
            })

        elif action in ["confirm_submitted", "confirm"]:
            def apply_step2(row):
                if row.get("job_id") == job_id:
                    row["status"] = "applied"
                    row["applied_date"] = datetime.now().strftime("%Y-%m-%d")
                    row["last_update"] = datetime.now().strftime("%Y-%m-%d")
                    row["notes"] = notes or f"Lamaran telah resmi dikirim via portal {company}"
                    return True
                return False

            sync_tracker_update(apply_step2)

            self.send_json({
                "success": True,
                "action": "confirm_submitted",
                "job_id": job_id,
                "message": f"Hebat! Lamaran untuk {role} di {company} resmi tercatat 'Applied'."
            })

        elif action == "update_stage":
            new_stage = payload.get("stage", "screening")
            stage_notes = payload.get("notes", "")

            def apply_stage(row):
                if row.get("job_id") == job_id:
                    row["status"] = new_stage
                    row["last_update"] = datetime.now().strftime("%Y-%m-%d")
                    if stage_notes:
                        row["notes"] = stage_notes
                    return True
                return False

            sync_tracker_update(apply_stage)

            self.send_json({
                "success": True,
                "action": "update_stage",
                "job_id": job_id,
                "stage": new_stage,
                "message": f"Status seleksi {company} berhasil diperbarui ke '{new_stage}'!"
            })

        elif action == "skip":
            reason = payload.get("reason", "Dilewati oleh pengguna")

            def apply_skip(row):
                if row.get("job_id") == job_id:
                    row["status"] = "skipped"
                    row["notes"] = reason
                    row["last_update"] = datetime.now().strftime("%Y-%m-%d")
                    return True
                return False

            sync_tracker_update(apply_skip)

            self.send_json({
                "success": True,
                "action": "skip",
                "job_id": job_id,
                "message": f"Lowongan {role} di {company} telah ditandai dilewati."
            })

        elif action == "unskip":
            def apply_unskip(row):
                if row.get("job_id") == job_id:
                    row["status"] = "pending_review"
                    row["last_update"] = datetime.now().strftime("%Y-%m-%d")
                    return True
                return False

            sync_tracker_update(apply_unskip)

            self.send_json({
                "success": True,
                "action": "unskip",
                "job_id": job_id,
                "message": f"Lowongan {role} di {company} berhasil dikembalikan ke antrean review!"
            })

        elif action == "open_folder":
            folder = find_job_folder(job_id)
            if not folder or not os.path.exists(folder):
                self.send_json({"success": False, "error": f"Folder untuk {job_id} tidak ditemukan"}, status=404)
                return

            pdf_files = glob.glob(os.path.join(folder, "*.pdf"))
            target_path = pdf_files[0] if pdf_files else folder

            try:
                if platform.system() == "Darwin":
                    if pdf_files:
                        subprocess.run(["open", "-R", target_path])
                    else:
                        subprocess.run(["open", folder])
                elif platform.system() == "Windows":
                    if pdf_files:
                        subprocess.run(["explorer", f"/select,{target_path}"])
                    else:
                        subprocess.run(["explorer", folder])
                else:
                    subprocess.run(["xdg-open", folder])

                self.send_json({
                    "success": True,
                    "action": "open_folder",
                    "folder": os.path.abspath(folder),
                    "file_path": os.path.abspath(target_path),
                    "message": "Finder berhasil dibuka! File PDF CV siap ditarik (drag & drop)."
                })
            except Exception as e:
                self.send_json({"success": False, "error": str(e)}, status=500)
        else:
            self.send_json({"success": False, "error": f"Unknown action: {action}"}, status=400)

    def handle_api_search(self, payload):
        keyword = payload.get("keyword", "Junior Developer")
        location = payload.get("location", "Semua Wilayah")
        source = payload.get("source", "Glints Indonesia")
        self.send_json({
            "success": True,
            "keyword": keyword,
            "location": location,
            "source": source,
            "message": f"Sistem pencarian telah dipicu untuk keyword: '{keyword}' ({location} via {source})."
        })

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    server_address = ("", PORT)
    httpd = socketserver.TCPServer(server_address, CommanderHandler)
    print(f"🚀 AGY Job Hunter & CV Commander Server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
