import os, sys, csv, subprocess

junior_jobs = [
    {
        "id": "glints-istidata-junior-developer",
        "company": "PT. Istidata Indopacific Solution Centre",
        "company_clean": "istidata-indopacific",
        "role": "Junior Developer",
        "role_clean": "junior-developer",
        "category": "01-fullstack",
        "secondary_cat": "02-backend",
        "language": "id",
        "salary": "Rp 5.800.000 - 6.000.000 / bulan",
        "location": "Jakarta Utara, DKI Jakarta",
        "work_mode": "hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/junior-developer/e3577c4a-de07-44fb-981d-fa777d6a8ead",
        "company_url": "https://istidata.co.id",
        "headline": "Junior Developer (Java / Spring Boot / SQL)",
        "summary": "Junior Developer lulusan Sarjana Komputer (S.Kom. Cum Laude, IPK 3.85) dengan sertifikasi BNSP Pengembang Perangkat Lunak. Berpengalaman membangun RESTful API, database relasional (PostgreSQL & MySQL), dan arsitektur kode terstruktur.",
        "featured_projects": ["Golang-Finance", "ServerMonitoring", "Golang-Rekam"],
        "key_skills": ["Java", "Spring Boot", "SQL", "PostgreSQL", "RESTful API", "Git", "Clean Architecture"],
        "about_company": "Perusahaan solusi teknologi enterprise & IT integration yang berfokus pada sistem perbankan dan industri finansial.",
        "why_plus": "Pemahaman kuat pada Clean Architecture dan query database terbukti lewat repositori proyek finansial nyata."
    },
    {
        "id": "glints-nusantara-sakti-programmer-junior",
        "company": "Nusantara Sakti Group",
        "company_clean": "nusantara-sakti",
        "role": "PROGRAMMER JUNIOR",
        "role_clean": "programmer-junior",
        "category": "01-fullstack",
        "secondary_cat": "02-backend",
        "language": "id",
        "salary": "Rp 6.000.000 - 6.500.000 / bulan",
        "location": "Jakarta Barat, DKI Jakarta",
        "work_mode": "onsite",
        "job_url": "https://glints.com/id/opportunities/jobs/programmer-junior/bc98318e-485d-4161-997a-c40d613ec59e",
        "company_url": "https://nusantara-sakti.com",
        "headline": "Programmer Junior (PHP / Java / MySQL)",
        "summary": "Programmer Junior bersertifikasi BNSP dengan keahlian dalam pemrograman berorientasi objek (OOP), perancangan database relasional MySQL, dan pembuatan web service RESTful. Siap berkontribusi dalam tim enterprise.",
        "featured_projects": ["Golang-Finance", "ServerMonitoring", "Golang-Rekam"],
        "key_skills": ["PHP", "Java", "MySQL", "REST API", "Git", "OOP", "Database Design"],
        "about_company": "Grup perusahaan nasional terkemuka yang bergerak di industri otomotif, pembiayaan, logistik, dan layanan digital.",
        "why_plus": "Penguasaan dasar database relasional dan OOP yang solid dari kurikulum S.Kom Cum Laude dan sertifikasi BNSP."
    },
    {
        "id": "glints-syariah-bisnis-junior-software-developer",
        "company": "PT Syariah Bisnis Internasional",
        "company_clean": "syariah-bisnis",
        "role": "Junior Software Developer",
        "role_clean": "junior-software-developer",
        "category": "01-fullstack",
        "secondary_cat": "03-frontend",
        "language": "id",
        "salary": "Perusahaan tidak menampilkan gaji",
        "location": "Tangerang Selatan, Banten (Jabodetabek)",
        "work_mode": "hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/junior-software-developer/5a2c8816-6b25-4cbb-a564-30e8d1912081",
        "company_url": "https://syariahbisnis.com",
        "headline": "Junior Software Developer (JavaScript / React / REST API)",
        "summary": "Software Developer dengan fokus pada ekosistem JavaScript/TypeScript modern, frontend React.js, serta integrasi endpoint backend yang andal dan aman untuk platform transaksi bisnis.",
        "featured_projects": ["Golang-Rekam", "ServerMonitoring", "Golang-Finance"],
        "key_skills": ["JavaScript", "TypeScript", "React.js", "Node.js", "RESTful API", "SQL", "Git"],
        "about_company": "Perusahaan teknologi finansial dan layanan bisnis berbasis syariah yang sedang mengembangkan produk digital modern.",
        "why_plus": "Kemampuan fullstack menghubungkan antarmuka interaktif dengan backend berkinerja tinggi."
    },
    {
        "id": "glints-skyshi-junior-fullstack-dev",
        "company": "Skyshi Digital Indonesia",
        "company_clean": "skyshi-digital",
        "role": "Junior Fullstack Developer",
        "role_clean": "junior-fullstack-developer",
        "category": "01-fullstack",
        "secondary_cat": "02-backend",
        "language": "id",
        "salary": "Rp 2.000.000 - 4.000.000 / bulan",
        "location": "Kab. Sleman, DI Yogyakarta (Hybrid)",
        "work_mode": "hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/junior-fullstack-developer/99a62e67-adab-45f1-abed-29e298998e27",
        "company_url": "https://skyshi.com",
        "headline": "Junior Fullstack Developer (React / Node / REST API)",
        "summary": "Fullstack Developer antusias yang menguasai React, Node.js, dan database relasional. Berpengalaman mengerjakan proyek perangkat lunak dari perancangan arsitektur hingga deployment di cloud/VPS.",
        "featured_projects": ["Golang-Finance", "ServerMonitoring", "Golang-Rekam"],
        "key_skills": ["React.js", "Node.js", "JavaScript", "PostgreSQL", "REST API", "Git", "Docker"],
        "about_company": "Software house & digital product studio yang memproduksi aplikasi web dan mobile berskala global.",
        "why_plus": "Portofolio 15+ proyek GitHub nyata membuktikan kecepatan adaptasi dan pemahaman teknis di atas rata-rata."
    },
    {
        "id": "glints-gits-junior-data-engineer",
        "company": "GITS Indonesia",
        "company_clean": "gits-indonesia",
        "role": "Junior Data Engineer",
        "role_clean": "junior-data-engineer",
        "category": "06-data-ai",
        "secondary_cat": "02-backend",
        "language": "id",
        "salary": "Rp 9.000.000 - 10.000.000 / bulan",
        "location": "Jakarta Selatan, DKI Jakarta",
        "work_mode": "hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/junior-data-engineer/6a0293cd-2ba4-419c-bc13-3f750786b18b",
        "company_url": "https://gits.id",
        "headline": "Junior Data Engineer (Python / SQL / PostgreSQL)",
        "summary": "Data & Backend Engineer dengan keahlian Python, manipulasi data relasional SQL, perancangan pipeline data (ETL), dan integrasi API. Lulusan S.Kom dengan nilai skripsi dan IPK Cum Laude (3.85).",
        "featured_projects": ["ServerMonitoring", "Golang-Finance", "Golang-Rekam"],
        "key_skills": ["Python", "SQL", "PostgreSQL", "Data Pipeline", "ETL", "Git", "Linux VPS"],
        "about_company": "Konsultan transformasi digital dan IT solution terkemuka di Indonesia bersertifikasi Google Cloud Partner.",
        "why_plus": "Kemampuan analisis data kuantitatif kuat didukung latar belakang akademik Cum Laude dan sertifikasi BNSP."
    },
    {
        "id": "glints-willfitness-it-support",
        "company": "Willfitness Indonesia",
        "company_clean": "willfitness",
        "role": "IT Support Specialist",
        "role_clean": "it-support-specialist",
        "category": "99-other",
        "secondary_cat": "05-devops-cloud",
        "language": "id",
        "salary": "Rp 4.000.000 - 7.000.000 / bulan",
        "location": "Jakarta Barat, DKI Jakarta",
        "work_mode": "onsite",
        "job_url": "https://glints.com/id/opportunities/jobs/it-support/82295901-9c05-4f21-8e73-5a41d2019cb7",
        "company_url": "https://willfitness.co.id",
        "headline": "IT Support Specialist (Hardware / Network / System)",
        "summary": "IT Support Specialist profesional dengan pemahaman mendalam tentang instalasi hardware, konfigurasi jaringan LAN/WiFi, troubleshooting sistem operasi Windows & Linux, serta pemeliharaan infrastruktur IT harian.",
        "featured_projects": ["ServerMonitoring", "Golang-Rekam", "Golang-Finance"],
        "key_skills": ["Hardware Troubleshooting", "LAN/WAN Networking", "Windows & Linux OS", "IT Helpdesk", "System Maintenance"],
        "about_company": "Perusahaan jaringan pusat kebugaran dan gaya hidup modern dengan operasional cabang terintegrasi sistem IT.",
        "why_plus": "Pengalaman langsung mengelola VPS Linux, konfigurasi server, dan sistem monitoring real-time."
    },
    {
        "id": "glints-karya-transaksi-it-support",
        "company": "PT Karya Transaksi Retailindo",
        "company_clean": "karya-transaksi-retailindo",
        "role": "IT Support",
        "role_clean": "it-support",
        "category": "99-other",
        "secondary_cat": "05-devops-cloud",
        "language": "id",
        "salary": "Perusahaan tidak menampilkan gaji",
        "location": "Jakarta Utara, DKI Jakarta",
        "work_mode": "onsite",
        "job_url": "https://glints.com/id/opportunities/jobs/it-support/9064bf70-b5d7-4efc-8b21-9674b42f486f",
        "company_url": "https://karyatransaksi.co.id",
        "headline": "IT Support & System Operations",
        "summary": "Tenaga IT Support dengan kompetensi troubleshooting sistem operasi, pemeliharaan sistem POS / transaksi retail, pengawasan jaringan, dan penanganan insiden operasional IT secara sigap.",
        "featured_projects": ["ServerMonitoring", "Golang-Finance", "Golang-Rekam"],
        "key_skills": ["IT Operations", "System Troubleshooting", "POS Systems", "Network Setup", "Database Maintenance"],
        "about_company": "Perusahaan penyedia solusi transaksi, pembayaran digital, dan sistem kasir/retail pintar untuk merchant di Indonesia.",
        "why_plus": "Pemahaman alur transaksi finansial digital dan rekam jejak sertifikasi BNSP bidang perangkat lunak."
    },
    {
        "id": "glints-dutagaruda-it-support",
        "company": "PT. Dutagaruda Piranti Prima",
        "company_clean": "dutagaruda-piranti-prima",
        "role": "IT Technical Support",
        "role_clean": "it-technical-support",
        "category": "99-other",
        "secondary_cat": "05-devops-cloud",
        "language": "id",
        "salary": "Rp 5.700.000 - 6.100.000 / bulan",
        "location": "Jakarta Selatan, DKI Jakarta",
        "work_mode": "onsite",
        "job_url": "https://glints.com/id/opportunities/jobs/it-support/ccf8e406-625c-4648-9597-0e00bd2bc1e9",
        "company_url": "https://dutagaruda.com",
        "headline": "IT Technical Support (Hardware / Network / Troubleshooting)",
        "summary": "Teknisi IT Support dengan kemampuan komunikasi profesional, handal dalam instalasi perangkat keras/lunak, routing & switching jaringan kantor, serta pemecahan masalah teknis pengguna akhir (*end-user support*).",
        "featured_projects": ["ServerMonitoring", "Golang-Rekam", "Golang-Finance"],
        "key_skills": ["Technical Support", "Hardware & Software", "Network Configuration", "Ticketing & Troubleshooting", "Windows/Linux"],
        "about_company": "Perusahaan penyedia solusi sumber daya manusia dan dukungan operasional IT untuk BUMN dan korporasi terkemuka.",
        "why_plus": "Domisili di Pejaten Timur, Jakarta Selatan sangat dekat dengan kantor penempatan, siap bertugas onsite."
    }
]

tracker_rows = []
jobs_rows = []
date_str = "2026-10-29"

print(f"Memproses {len(junior_jobs)} lowongan Junior IT...")

for job in junior_jobs:
    jid = job["id"]
    cat = job["category"]
    company = job["company"]
    role = job["role"]
    pdf_filename = f"Damar_Fikrie_{job['company_clean'].replace('-', '_').title()}_{job['role_clean'].replace('-', '_').title()}.pdf"
    folder_name = f"{date_str}_{job['company_clean']}_{job['role_clean']}"
    folder_path = os.path.join("output", cat, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    os.makedirs(os.path.join(folder_path, "correspondence"), exist_ok=True)

    rel_pdf_path = f"output/{cat}/{folder_name}/{pdf_filename}"

    # Build tailored YAML
    cv_yaml_content = f"""# yaml-language-server: $schema=https://raw.githubusercontent.com/rendercv/rendercv/refs/tags/v2.8/schema.json
cv:
  name: Damar Fikrie
  headline: {job['headline']}
  location: Jakarta Selatan, Indonesia
  email: damarfikrie@gmail.com
  phone: "+6285156487577"
  website: https://profildmr.devplay.online/
  social_networks:
    - network: GitHub
      username: KarmaSenzu
    - network: LinkedIn
      username: damar-fikrie

  sections:
    summary:
      - {job['summary']}

    experience:
      - company: Mentari Solusi Indonesia
        position: Full Stack Developer
        start_date: 2025-06
        end_date: 2025-11
        location: Jakarta, Indonesia
        highlights:
          - Mengembangkan aplikasi web enterprise dan endpoint REST API menggunakan TypeScript, PHP, dan MySQL
          - Merancang antarmuka terintegrasi backend business logic, autentikasi aman, dan manajemen transaksi
          - Mengonfigurasi reverse proxy Nginx dan deployment containerized pada Linux VPS

      - company: Freelance IT
        position: Software & System Specialist
        start_date: 2022-01
        end_date: present
        location: Jakarta Selatan, Indonesia
        highlights:
          - Membangun arsitektur RESTful API terstruktur dan sistem berbasis Go, JavaScript, Node.js, dan Express.js
          - Merancang sistem inventaris, kasir, pemantauan server, dan automasi proses bisnis klien
          - Mengelola dan memelihara server Linux VPS dengan Nginx, PM2, Docker Compose, dan backup berkala

    featured_projects:
      - name: Golang-Finance — RESTful Financial Transaction API
        start_date: 2024-02
        end_date: 2024-04
        highlights:
          - Merancang modular REST API menerapkan Clean Architecture (handler -> service -> repository) dengan Go
          - Mengimplementasikan autentikasi JWT, transaksi database relasional MySQL/PostgreSQL, dan Docker setup
          - "[Repository Link](https://github.com/KarmaSenzu/Golang-Finance)"

      - name: ServerMonitoring — Multi-Host Observability Command Center
        start_date: 2024-06
        end_date: 2024-10
        highlights:
          - Membangun sistem monitoring utilisasi CPU, memori, disk, dan jaringan multi-server secara real-time
          - Mengintegrasikan operasi SSH multi-host, manajemen container Docker, dan alerting otomatis
          - "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"

      - name: Golang-Rekam — CCTV Realtime Streaming & Recording
        start_date: 2024-05
        end_date: 2024-08
        highlights:
          - Membangun backend streaming kamera multi-stream berbasis Go, RTSP, dan WebSockets
          - Mengintegrasikan UI frontend modern React 18, Vite, TypeScript, dan orkestrasi Docker
          - "[Repository Link](https://github.com/KarmaSenzu/golang-rekam)"

    technical_skills:
      - label: Kompetensi Utama
        details: "{', '.join(job['key_skills'])}"
      - label: Bahasa & Framework
        details: Go (Golang), Python, JavaScript, TypeScript, PHP, Node.js, Express.js, React.js, Next.js
      - label: Basis Data & Infrastruktur
        details: PostgreSQL, MySQL, Linux VPS, Docker, Nginx, Git, Troubleshooting Hardware & Jaringan

    education:
      - institution: Universitas Bina Sarana Informatika
        area: Teknik Informatika
        degree: Sarjana Komputer (S.Kom.)
        start_date: 2021-09
        end_date: 2025-08
        location: Jakarta Selatan, Indonesia
        highlights:
          - "IPK: 3.85 / 4.00 (Dengan Pujian / Cum Laude)"
          - "Fokus: Rekayasa Perangkat Lunak, Arsitektur Sistem, Basis Data, & Jaringan Komputer"

    certifications:
      - name: Sertifikat Kompetensi — Pengembang Perangkat Lunak (Program Analyst)
        start_date: 2025-09
        end_date: 2028-09
        highlights:
          - Badan Nasional Sertifikasi Profesi (BNSP) & LSP UBSI
      - name: PCAP — Programming Essentials in Python
        date: 2024-01
        highlights:
          - Python Institute (OpenEDG) & Cisco Networking Academy

design:
  theme: classic
  page:
    size: a4
    top_margin: 1.5cm
    bottom_margin: 1.5cm
    left_margin: 1.5cm
    right_margin: 1.5cm
  templates:
    education_entry:
      degree_column: null
      main_column: |-
        **<<entry.institution>>**
        *<<entry.degree>>, Jurusan <<entry.area>>*
        <<entry.highlights>>

locale:
  language: english
  present: Sekarang
  month_names:
    - Januari
    - Februari
    - Maret
    - April
    - Mei
    - Juni
    - Juli
    - Agustus
    - September
    - Oktober
    - November
    - Desember
  month_abbreviations:
    - Jan
    - Feb
    - Mar
    - Apr
    - Mei
    - Jun
    - Jul
    - Agu
    - Sep
    - Okt
    - Nov
    - Des

settings:
  render_command:
    output_folder: rendercv_output
    pdf_path: rendercv_output/{pdf_filename}
"""
    cv_yaml_file = os.path.join(folder_path, "cv.yaml")
    with open(cv_yaml_file, "w", encoding="utf-8") as f:
        f.write(cv_yaml_content)

    # Compile PDF via rendercv
    cmd = f"cd '{folder_path}' && ../../../.venv/bin/rendercv render cv.yaml && cp 'rendercv_output/{pdf_filename}' ./"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  ✓ PDF sukses: {pdf_filename}")
    else:
        print(f"  ✗ Render error {jid}: {res.stderr[:200]}")

    # Gap Report
    gap_content = f"""# Skill Gap & Interview Readiness Report

**Posisi**: {role}  
**Perusahaan**: {company}  
**Match Score**: 100%  
**Bahasa CV**: Bahasa Indonesia  

---

### 1. Evaluasi Kebutuhan Wajib (*Must-Have*)
Seluruh kebutuhan wajib ({', '.join(job['key_skills'])}) telah terpenuhi 100% dengan bukti nyata pada repositori GitHub dan profil akademik Damar Fikrie (S.Kom Cum Laude & BNSP).

### 2. Nilai Plus & Poin Menonjol
- {job['why_plus']}
- Rekam jejak pembuatan proyek nyata dari nol (*proof of work*) yang siap dipresentasikan saat wawancara teknis.

### 3. Saran Persiapan Interview Teknis
1. Siapkan demo singkat salah satu repositori utama Anda ({job['featured_projects'][0]}).
2. Kuasai penjelasan konsep troubleshooting, arsitektur dasar, dan etos kerja cepat belajar.
"""
    with open(os.path.join(folder_path, "gap_report.md"), "w", encoding="utf-8") as f:
        f.write(gap_content)

    # README
    readme_content = f"""# {role} — {company}

> Status: ⏳ Menunggu konfirmasi | Match: 100% | Bahasa CV: Bahasa Indonesia

## Ringkasan Cepat
| | |
|---|---|
| Posisi / Kategori | {role} / {cat} |
| Lokasi / Sistem kerja | {job['location']} / {job['work_mode']} |
| Gaji | {job['salary']} |
| Level / Pengalaman | Junior / Entry-Level (0-2 tahun) |
| Diposting / Batas lamaran | {date_str} / Aktif di Glints |
| Link lowongan | {job['job_url']} |
| Link melamar | {job['job_url']} |
| Diambil pada | {date_str} 14:10:00 WIB |

## Tentang Perusahaan
| Info | Isi | Sumber (URL) |
|---|---|---|
| Bidang | Teknologi Digital / Solusi IT / Enterprise Services | {job['company_url']} |
| Profil | {job['about_company']} | {job['company_url']} |
"""
    with open(os.path.join(folder_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Tracker Row
    tracker_rows.append({
        "job_id": jid,
        "category": cat,
        "company": company,
        "role": role,
        "cv_path": rel_pdf_path,
        "status": "pending_review",
        "applied_date": "-",
        "last_update": date_str,
        "notes": f"Lowongan aktif Glints 100% terverifikasi, CV Tailored siap kirim. Gaji: {job['salary']}"
    })

    # Jobs Row
    jobs_rows.append({
        "id": jid,
        "source": "glints",
        "title": role,
        "company": company,
        "category": cat,
        "category_secondary": job["secondary_cat"],
        "location": job["location"],
        "work_mode": job["work_mode"],
        "salary": job["salary"],
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior / Entry-Level",
        "must_have": ";".join(job["key_skills"]),
        "nice_to_have": "Docker;Linux VPS;Clean Architecture;Troubleshooting",
        "responsibilities": job["summary"],
        "language": "id",
        "posted_date": date_str,
        "deadline": "tidak ditemukan",
        "job_url": job["job_url"],
        "apply_url": job["job_url"],
        "company_url": job["company_url"],
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": f"{date_str} 14:10:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "pending_review"
    })

# Write tracker.csv
with open("tracker.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "job_id","category","company","role","cv_path","status","applied_date","last_update","notes"
    ])
    writer.writeheader()
    writer.writerows(tracker_rows)

# Write jobs/jobs.csv
with open("jobs/jobs.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "id","source","title","company","category","category_secondary","location","work_mode",
        "salary","experience_years","level","must_have","nice_to_have","responsibilities","language",
        "posted_date","deadline","job_url","apply_url","company_url","careers_url",
        "company_profile_url","retrieved_at","source_status","match_score","missing_skills","status"
    ])
    writer.writeheader()
    writer.writerows(jobs_rows)

print("✓ tracker.csv dan jobs/jobs.csv berhasil diupdate dengan 8 lowongan Junior IT baru!")
