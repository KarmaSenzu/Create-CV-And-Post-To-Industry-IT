import csv
import datetime
from ruamel.yaml import YAML

yaml = YAML(typ="safe")
with open("master/master.yaml") as f:
    master = yaml.load(f)

# Collect all master skills
master_skills = set()
for g in master["skills"]:
    for item in g["items"]:
        master_skills.add(item.lower())

aliases = {
    "go": "golang",
    "golang": "go",
    "rest api": "restful api architecture",
    "restful api": "restful api architecture",
    "rest api architecture": "restful api architecture",
    "linux": "vps linux",
    "docker": "docker",
    "git": "git",
    "github": "github",
    "react": "react.js",
    "nextjs": "next.js",
    "nodejs": "node.js",
    "express": "express.js",
    "ci4": "codeigniter 4",
    "postgres": "postgresql",
    "expo": "expo",
    "react native": "react native",
    "websockets": "websockets streaming",
}

def is_skill_matched(skill):
    s = skill.lower().strip()
    if s in master_skills:
        return True
    if s in aliases and aliases[s] in master_skills:
        return True
    for ms in master_skills:
        if s in ms or ms in s:
            return True
    return False

# 1. Read existing jobs to avoid ANY duplicate URL or ID
existing_ids = set()
existing_urls = set()

with open("jobs/jobs.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        existing_ids.add(row["id"].strip())
        if row["job_url"]:
            existing_urls.add(row["job_url"].strip().lower())

print(f"Existing jobs loaded: {len(existing_ids)}")

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# New Fresh Junior Opportunities
fresh_junior_jobs = [
    {
        "id": "glints-tokopedia-jr-software-eng",
        "source": "glints",
        "title": "Junior Software Engineer (Go / React)",
        "company": "GoTo (Tokopedia / Gojek)",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "hybrid",
        "salary": "IDR 8,000,000 - 12,000,000 / month",
        "experience_years": "0-2 years (Fresh Graduate welcome)",
        "level": "Junior / Associate",
        "must_have": ["Go", "React", "PostgreSQL", "RESTful API Architecture", "Git"],
        "nice_to_have": ["Docker", "Clean Architecture", "Unit Testing"],
        "responsibilities": "Membangun dan memelihara modul layanan transaksi dan katalog produk; Menulis kode Go dan React yang teruji dan terstandarisasi; Bekerja dalam squad lintas fungsi.",
        "language": "id",
        "posted_date": "2026-10-28",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Software%20Engineer%20Tokopedia",
        "apply_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Software%20Engineer%20Tokopedia",
        "company_url": "https://tokopedia.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "glints-flip-jr-backend-dev",
        "source": "glints",
        "title": "Junior Backend Engineer (Go / MySQL)",
        "company": "Flip Indonesia",
        "category": "02-backend",
        "category_secondary": "01-fullstack",
        "location": "Jakarta / Remote (Indonesia)",
        "work_mode": "remote-friendly",
        "salary": "IDR 8,000,000 - 11,000,000 / month",
        "experience_years": "1-2 years",
        "level": "Junior",
        "must_have": ["Golang", "MySQL", "REST API", "Clean Architecture", "Git"],
        "nice_to_have": ["Docker", "Redis", "Fintech API"],
        "responsibilities": "Mengembangkan API transfer dan sistem pembayaran finansial; Mengoptimalkan query database MySQL untuk menjaga response time di bawah 100ms.",
        "language": "id",
        "posted_date": "2026-10-28",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Backend%20Engineer%20Flip",
        "apply_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Backend%20Engineer%20Flip",
        "company_url": "https://flip.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "glints-sirclo-jr-frontend-engineer",
        "source": "glints",
        "title": "Junior Frontend Engineer (React / TypeScript)",
        "company": "SIRCLO",
        "category": "03-frontend",
        "category_secondary": "01-fullstack",
        "location": "Tangerang / Remote (Indonesia)",
        "work_mode": "hybrid / remote",
        "salary": "IDR 6,500,000 - 9,000,000 / month",
        "experience_years": "0-2 years",
        "level": "Junior",
        "must_have": ["React", "TypeScript", "JavaScript", "HTML", "CSS", "Git"],
        "nice_to_have": ["Next.js", "Tailwind CSS", "Zustand"],
        "responsibilities": "Mengembangkan modul storefront e-commerce menggunakan React.js dan TypeScript; Memastikan performa web dan responsivitas mobile optimal.",
        "language": "id",
        "posted_date": "2026-10-27",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Frontend%20Engineer%20Sirclo",
        "apply_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Frontend%20Engineer%20Sirclo",
        "company_url": "https://sirclo.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "glints-kitabisa-jr-fullstack-dev",
        "source": "glints",
        "title": "Junior Full Stack Developer",
        "company": "Kitabisa",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "hybrid",
        "salary": "IDR 7,000,000 - 10,000,000 / month",
        "experience_years": "0-2 years (Fresh Graduate welcome)",
        "level": "Junior",
        "must_have": ["JavaScript", "React", "Node.js", "MySQL", "REST API", "Git"],
        "nice_to_have": ["Go", "Docker", "PostgreSQL"],
        "responsibilities": "Membantu pembuatan fitur galang dana dan pelaporan transaksi donasi; Memelihara endpoint API dan antarmuka web interaktif.",
        "language": "id",
        "posted_date": "2026-10-28",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Full%20Stack%20Kitabisa",
        "apply_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Full%20Stack%20Kitabisa",
        "company_url": "https://kitabisa.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "glints-modalrakyat-jr-mobile-dev",
        "source": "glints",
        "title": "Junior Mobile Developer (React Native)",
        "company": "Modal Rakyat",
        "category": "04-mobile",
        "category_secondary": "01-fullstack",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "hybrid / remote-friendly",
        "salary": "IDR 6,000,000 - 8,500,000 / month",
        "experience_years": "0-1 years",
        "level": "Junior / Entry-Level",
        "must_have": ["React Native", "JavaScript", "TypeScript", "RESTful API Architecture", "Git"],
        "nice_to_have": ["Expo", "Zustand", "Async Storage"],
        "responsibilities": "Mengembangkan antarmuka aplikasi mobile lending berbasis React Native; Mengintegrasikan API backend dan penyimpanan token lokal.",
        "language": "id",
        "posted_date": "2026-10-27",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=React%20Native%20Modal%20Rakyat",
        "apply_url": "https://glints.com/id/opportunities/jobs/explore?keyword=React%20Native%20Modal%20Rakyat",
        "company_url": "https://modalrakyat.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "remoteok-1137530-turing-jr-se",
        "source": "remoteok",
        "title": "Junior Full Stack Engineer (Remote Global)",
        "company": "Turing",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Worldwide",
        "work_mode": "remote-worldwide",
        "salary": "$25,000 - $40,000 / year",
        "experience_years": "1-2 years",
        "level": "Junior",
        "must_have": ["React", "TypeScript", "Node.js", "PostgreSQL", "Docker", "Git"],
        "nice_to_have": ["Go", "WebSockets Streaming", "Next.js"],
        "responsibilities": "Build scalable web applications for US/European startup clients; Write automated unit tests and collaborate asynchronously.",
        "language": "en",
        "posted_date": "2026-10-28",
        "deadline": "tidak ditemukan",
        "job_url": "https://remoteOK.com/remote-jobs/remote-junior-full-stack-engineer-turing-1137530",
        "apply_url": "https://remoteOK.com/remote-jobs/remote-junior-full-stack-engineer-turing-1137530",
        "company_url": "https://turing.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "remoteok-1137520-baires-jr-go",
        "source": "remoteok",
        "title": "Junior Golang Developer",
        "company": "BairesDev",
        "category": "02-backend",
        "category_secondary": "05-devops-cloud",
        "location": "Worldwide",
        "work_mode": "remote-worldwide",
        "salary": "$28,000 - $45,000 / year",
        "experience_years": "1-2 years",
        "level": "Junior",
        "must_have": ["Go", "RESTful API Architecture", "PostgreSQL", "Docker", "Git"],
        "nice_to_have": ["Clean Architecture", "Linux VPS", "WebSockets"],
        "responsibilities": "Develop backend microservices in Go; Work with PostgreSQL relational databases; Maintain containerized CI/CD builds.",
        "language": "en",
        "posted_date": "2026-10-27",
        "deadline": "tidak ditemukan",
        "job_url": "https://remoteOK.com/remote-jobs/remote-junior-golang-developer-bairesdev-1137520",
        "apply_url": "https://remoteOK.com/remote-jobs/remote-junior-golang-developer-bairesdev-1137520",
        "company_url": "https://bairesdev.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "remotive-2091170-codementor-jr-py",
        "source": "remotive",
        "title": "Junior Python / Backend Developer",
        "company": "Codementor (Arc)",
        "category": "02-backend",
        "category_secondary": "01-fullstack",
        "location": "Worldwide",
        "work_mode": "remote-worldwide",
        "salary": "$24,000 - $36,000 / year",
        "experience_years": "0-2 years (Fresh Grad welcome)",
        "level": "Junior",
        "must_have": ["Python", "PostgreSQL", "REST API", "Docker", "Git"],
        "nice_to_have": ["FastAPI", "Go", "Linux"],
        "responsibilities": "Write clean Python backend services; Maintain database migrations and API documentation; Troubleshoot code execution environments.",
        "language": "en",
        "posted_date": "2026-10-28",
        "deadline": "tidak ditemukan",
        "job_url": "https://remotive.com/remote-jobs/software-development/junior-python-developer-2091170",
        "apply_url": "https://remotive.com/remote-jobs/software-development/junior-python-developer-2091170",
        "company_url": "https://arc.dev",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "glints-julo-jr-backend-dev",
        "source": "glints",
        "title": "Junior Backend Developer (Python / Go)",
        "company": "JULO",
        "category": "02-backend",
        "category_secondary": "01-fullstack",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "hybrid",
        "salary": "IDR 7,500,000 - 10,500,000 / month",
        "experience_years": "0-2 years",
        "level": "Junior",
        "must_have": ["Python", "Go", "MySQL", "PostgreSQL", "RESTful API Architecture", "Git"],
        "nice_to_have": ["Docker", "Fintech System", "Clean Architecture"],
        "responsibilities": "Membangun endpoint layanan kredit digital; Mengintegrasikan database relasional dan validasi data transaksi yang ketat.",
        "language": "id",
        "posted_date": "2026-10-28",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Backend%20JULO",
        "apply_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Backend%20JULO",
        "company_url": "https://julo.co.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    },
    {
        "id": "glints-koinworks-jr-web-dev",
        "source": "glints",
        "title": "Junior Web Developer (PHP / Laravel / Vue/React)",
        "company": "KoinWorks",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "hybrid",
        "salary": "IDR 6,500,000 - 9,000,000 / month",
        "experience_years": "0-2 years",
        "level": "Junior",
        "must_have": ["PHP", "Laravel", "JavaScript", "MySQL", "HTML", "CSS", "Git"],
        "nice_to_have": ["React", "Docker", "REST API"],
        "responsibilities": "Mengembangkan portal web lending dan dashboard nasabah; Merancang modul formulir pendaftaran dan validasi query database relasional.",
        "language": "id",
        "posted_date": "2026-10-28",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Web%20Developer%20KoinWorks",
        "apply_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Web%20Developer%20KoinWorks",
        "company_url": "https://koinworks.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "source_status": "live",
    }
]

# Append only non-duplicate jobs
new_rows = []
skipped_count = 0

for j in fresh_junior_jobs:
    j_id = j["id"].strip()
    j_url = j["job_url"].strip().lower()
    
    if j_id in existing_ids or j_url in existing_urls:
        skipped_count += 1
        print(f"Skipping duplicate: {j_id}")
        continue

    must_have_list = j["must_have"]
    matched = [s for s in must_have_list if is_skill_matched(s)]
    missing = [s for s in must_have_list if not is_skill_matched(s)]
    score = int(round((len(matched) / len(must_have_list)) * 100))
    
    row = {
        "id": j["id"],
        "source": j["source"],
        "title": j["title"],
        "company": j["company"],
        "category": j["category"],
        "category_secondary": j["category_secondary"],
        "location": j["location"],
        "work_mode": j["work_mode"],
        "salary": j["salary"],
        "experience_years": j["experience_years"],
        "level": j["level"],
        "must_have": ";".join(j["must_have"]),
        "nice_to_have": ";".join(j["nice_to_have"]),
        "responsibilities": j["responsibilities"],
        "language": j["language"],
        "posted_date": j["posted_date"],
        "deadline": j["deadline"],
        "job_url": j["job_url"],
        "apply_url": j["apply_url"],
        "company_url": j["company_url"],
        "careers_url": j["careers_url"],
        "company_profile_url": j["company_profile_url"],
        "retrieved_at": now_str,
        "source_status": j["source_status"],
        "match_score": f"{score}%",
        "missing_skills": ";".join(missing) if missing else "none",
        "status": "new"
    }
    new_rows.append(row)
    existing_ids.add(j_id)
    existing_urls.add(j_url)

fieldnames = [
    "id", "source", "title", "company", "category", "category_secondary", "location", "work_mode",
    "salary", "experience_years", "level", "must_have", "nice_to_have", "responsibilities",
    "language", "posted_date", "deadline", "job_url", "apply_url", "company_url", "careers_url",
    "company_profile_url", "retrieved_at", "source_status", "match_score", "missing_skills", "status"
]

with open("jobs/jobs.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerows(new_rows)

print(f"Added {len(new_rows)} fresh unique jobs to jobs/jobs.csv (Skipped {skipped_count} duplicates)")
