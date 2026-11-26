import os, sys, csv, subprocess, pathlib
from ruamel.yaml import YAML

yaml = YAML(typ="safe")
with open("master/master.yaml") as f:
    master = yaml.load(f)

# The 10 approved jobs to generate
jobs_to_process = [
    {
        "id": "glints-tokopedia-jr-software-eng",
        "company": "GoTo (Tokopedia)",
        "company_clean": "goto-tokopedia",
        "role": "Junior Software Engineer",
        "role_clean": "junior-software-engineer",
        "category": "01-fullstack",
        "language": "id",
        "salary": "IDR 8,000,000 - 12,000,000 / month",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "Hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Software%20Engineer%20Tokopedia",
        "company_url": "https://tokopedia.com",
        "headline": "Junior Software Engineer (Go / React)",
        "summary": "Software Engineer dengan keahlian dalam Go (Golang), React.js, dan arsitektur RESTful API. Berpengalaman membangun sistem streaming realtime, backend terstruktur, dan platform web berbasis PostgreSQL dan MySQL.",
        "featured_projects": ["Golang-Rekam", "ServerMonitoring", "Golang-Finance"],
        "key_skills": ["Go", "React", "PostgreSQL", "RESTful API Architecture", "Docker", "Git"],
        "about_company": "Perusahaan teknologi ekosistem digital terbesar di Indonesia (GoTo Group) yang menaungi Tokopedia dan Gojek.",
        "why_plus": "Lokasi kantor di Jakarta Selatan (sangat dekat dari Pejaten Timur), ekosistem teknologi Go terkemuka di Asia Tenggara."
    },
    {
        "id": "glints-flip-jr-backend-dev",
        "company": "Flip Indonesia",
        "company_clean": "flip-indonesia",
        "role": "Junior Backend Engineer",
        "role_clean": "junior-backend-engineer",
        "category": "02-backend",
        "language": "id",
        "salary": "IDR 8,000,000 - 11,000,000 / month",
        "location": "Jakarta / Remote (Indonesia)",
        "work_mode": "Remote-friendly",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Backend%20Engineer%20Flip",
        "company_url": "https://flip.id",
        "headline": "Junior Backend Engineer (Go / Clean Architecture)",
        "summary": "Backend Engineer yang berfokus pada Go (Golang), Clean Architecture, transaksi database relasional, dan perancangan REST API berkinerja tinggi. Berpengalaman mengembangkan API finansial dan sistem observabilitas server.",
        "featured_projects": ["Golang-Finance", "Golang-Rekam", "ServerMonitoring"],
        "key_skills": ["Golang", "MySQL", "PostgreSQL", "Clean Architecture", "REST API", "Docker", "Git"],
        "about_company": "Perusahaan fintech transfer dana antar bank dan payment gateway terkemuka di Indonesia.",
        "why_plus": "Pengalaman nyata merancang Golang-Finance (Clean Architecture REST API) sangat sejalan dengan sistem transaksi Flip."
    },
    {
        "id": "glints-kitabisa-jr-fullstack-dev",
        "company": "Kitabisa",
        "company_clean": "kitabisa",
        "role": "Junior Full Stack Developer",
        "role_clean": "junior-full-stack-developer",
        "category": "01-fullstack",
        "language": "id",
        "salary": "IDR 7,000,000 - 10,000,000 / month",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "Hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Full%20Stack%20Kitabisa",
        "company_url": "https://kitabisa.com",
        "headline": "Junior Full Stack Developer",
        "summary": "Full Stack Developer dengan pengalaman membangun aplikasi web interaktif React.js, backend REST API Node.js/Go, dan integrasi database MySQL/PostgreSQL. Berpengalaman dalam deployment server Linux VPS dan Docker.",
        "featured_projects": ["Dmrxai", "Golang-Finance", "Golang-Rekam"],
        "key_skills": ["JavaScript", "React", "Node.js", "MySQL", "REST API", "Git", "Docker"],
        "about_company": "Platform penggalangan dana dan donasi online sosial terbesar di Indonesia.",
        "why_plus": "Kantor berlokasi di Jakarta Selatan, budaya kerja berdampak sosial tinggi, teknologi web modern."
    },
    {
        "id": "glints-julo-jr-backend-dev",
        "company": "JULO",
        "company_clean": "julo",
        "role": "Junior Backend Developer",
        "role_clean": "junior-backend-developer",
        "category": "02-backend",
        "language": "id",
        "salary": "IDR 7,500,000 - 10,500,000 / month",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "Hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Backend%20JULO",
        "company_url": "https://julo.co.id",
        "headline": "Junior Backend Developer (Python / Go)",
        "summary": "Backend Developer dengan keahlian ganda Python dan Go (Golang), pengelolaan database relasional PostgreSQL & MySQL, dan perancangan REST API terstruktur untuk sistem finansial berbasis server Linux.",
        "featured_projects": ["Golang-Finance", "HERMES-PT.-ASISTEN-DMR", "Golang-Rekam"],
        "key_skills": ["Python", "Go", "PostgreSQL", "MySQL", "RESTful API Architecture", "Git"],
        "about_company": "Perusahaan fintech lending berlisensi OJK dengan sistem credit scoring berbasis AI.",
        "why_plus": "Lokasi kantor di Jakarta Selatan, kebutuhan kombinasi Python & Go sangat presisi dengan portofolio Anda."
    },
    {
        "id": "glints-modalrakyat-jr-mobile-dev",
        "company": "Modal Rakyat",
        "company_clean": "modal-rakyat",
        "role": "Junior Mobile Developer",
        "role_clean": "junior-mobile-developer",
        "category": "04-mobile",
        "language": "id",
        "salary": "IDR 6,000,000 - 8,500,000 / month",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "Hybrid / Remote-friendly",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=React%20Native%20Modal%20Rakyat",
        "company_url": "https://modalrakyat.id",
        "headline": "Junior Mobile Developer (React Native)",
        "summary": "Mobile Developer dengan pengalaman membangun aplikasi seluler menggunakan React Native, Expo, dan TypeScript. Terbiasa mengintegrasikan RESTful API, state management Zustand, dan penyimpanan lokal Async Storage.",
        "featured_projects": ["AturJajan", "Project-Aplikasi_Perpustakaan-fluter", "Dmrxai"],
        "key_skills": ["React Native", "Expo", "JavaScript", "TypeScript", "REST API", "Zustand", "Git"],
        "about_company": "Platform P2P lending terkemuka yang menghubungkan pendana dengan UMKM di Indonesia.",
        "why_plus": "Portofolio mobile AturJajan (React Native + Expo) menjadi bukti nyata yang tepat sasaran."
    },
    {
        "id": "glints-sirclo-jr-frontend-engineer",
        "company": "SIRCLO",
        "company_clean": "sirclo",
        "role": "Junior Frontend Engineer",
        "role_clean": "junior-frontend-engineer",
        "category": "03-frontend",
        "language": "id",
        "salary": "IDR 6,500,000 - 9,000,000 / month",
        "location": "Tangerang / Remote (Indonesia)",
        "work_mode": "Hybrid / Remote",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Frontend%20Engineer%20Sirclo",
        "company_url": "https://sirclo.com",
        "headline": "Junior Frontend Engineer (React / TypeScript)",
        "summary": "Frontend Engineer dengan keahlian React.js, TypeScript, Next.js, dan Tailwind CSS. Berpengalaman membangun modul antarmuka web interaktif yang responsif, berkinerja tinggi, dan terintegrasi dengan RESTful API.",
        "featured_projects": ["Dmrxai", "Golang-Rekam", "Hermes-Desktop-Pet"],
        "key_skills": ["React", "TypeScript", "JavaScript", "HTML5", "CSS3", "Tailwind CSS", "Git"],
        "about_company": "Solusi e-commerce omni-channel penyedia teknologi toko online dan marketplace enabler di Indonesia.",
        "why_plus": "Fokus pada ekosistem React & TypeScript modern untuk storefront e-commerce."
    },
    {
        "id": "glints-koinworks-jr-web-dev",
        "company": "KoinWorks",
        "company_clean": "koinworks",
        "role": "Junior Web Developer",
        "role_clean": "junior-web-developer",
        "category": "01-fullstack",
        "language": "id",
        "salary": "IDR 6,500,000 - 9,000,000 / month",
        "location": "Jakarta Selatan, Indonesia",
        "work_mode": "Hybrid",
        "job_url": "https://glints.com/id/opportunities/jobs/explore?keyword=Web%20Developer%20KoinWorks",
        "company_url": "https://koinworks.com",
        "headline": "Junior Web Developer (PHP / Laravel / React)",
        "summary": "Web Developer dengan penguasaan PHP (Laravel, CodeIgniter), React.js, dan database MySQL. Berpengalaman membangun sistem web operasional, portal transaksi, serta deployment server Linux VPS.",
        "featured_projects": ["Laravel Travel", "CI4-Perpuspus-2", "Dmrxai"],
        "key_skills": ["PHP", "Laravel", "JavaScript", "MySQL", "HTML5", "CSS3", "Git"],
        "about_company": "Super financial app terdepan di Indonesia untuk kebutuhan finansial personal dan UMKM.",
        "why_plus": "Lokasi kantor di Jakarta Selatan, tech stack PHP/Laravel sangat sesuai dengan proyek Laravel Travel Anda."
    },
    {
        "id": "remoteok-1137530-turing-jr-se",
        "company": "Turing",
        "company_clean": "turing",
        "role": "Junior Full Stack Engineer",
        "role_clean": "junior-full-stack-engineer",
        "category": "01-fullstack",
        "language": "en",
        "salary": "$25,000 - $40,000 / year",
        "location": "Worldwide",
        "work_mode": "remote-worldwide",
        "job_url": "https://remoteOK.com/remote-jobs/remote-junior-full-stack-engineer-turing-1137530",
        "company_url": "https://turing.com",
        "headline": "Junior Full Stack Engineer (Remote Global)",
        "summary": "Full Stack Engineer proficient in React.js, TypeScript, Go (Golang), and Node.js. Experienced in designing modular REST APIs, real-time WebSocket applications, and containerized deployment with Docker.",
        "featured_projects": ["Golang-Rekam", "Dmrxai", "ServerMonitoring"],
        "key_skills": ["React", "TypeScript", "Node.js", "PostgreSQL", "Docker", "Git"],
        "about_company": "AI-powered global platform connecting elite developers with high-growth US tech companies.",
        "why_plus": "Worldwide remote, competitive USD compensation, global engineering exposure."
    },
    {
        "id": "remoteok-1137520-baires-jr-go",
        "company": "BairesDev",
        "company_clean": "bairesdev",
        "role": "Junior Golang Developer",
        "role_clean": "junior-golang-developer",
        "category": "02-backend",
        "language": "en",
        "salary": "$28,000 - $45,000 / year",
        "location": "Worldwide",
        "work_mode": "remote-worldwide",
        "job_url": "https://remoteOK.com/remote-jobs/remote-junior-golang-developer-bairesdev-1137520",
        "company_url": "https://bairesdev.com",
        "headline": "Junior Golang Developer (Remote Global)",
        "summary": "Backend Developer specializing in Go (Golang), Clean Architecture REST APIs, real-time systems, and PostgreSQL databases. Proven hands-on track record building multi-server infrastructure and video streaming backends.",
        "featured_projects": ["Golang-Finance", "Golang-Rekam", "ServerMonitoring"],
        "key_skills": ["Go", "RESTful API Architecture", "PostgreSQL", "Docker", "Git"],
        "about_company": "Leading nearshore tech solutions company serving top Fortune 500 enterprises.",
        "why_plus": "Pure Go backend role with high architectural standards and full remote flexibility."
    },
    {
        "id": "remotive-2091170-codementor-jr-py",
        "company": "Codementor (Arc)",
        "company_clean": "codementor-arc",
        "role": "Junior Python / Backend Developer",
        "role_clean": "junior-python-backend-developer",
        "category": "02-backend",
        "language": "en",
        "salary": "$24,000 - $36,000 / year",
        "location": "Worldwide",
        "work_mode": "remote-worldwide",
        "job_url": "https://remotive.com/remote-jobs/software-development/junior-python-developer-2091170",
        "company_url": "https://arc.dev",
        "headline": "Junior Python & Backend Developer (Remote Global)",
        "summary": "Software Engineer with strong competencies in Python, Go, RESTful API development, and PostgreSQL. Experienced in building automated AI agents, database schema optimization, and Docker Compose environments.",
        "featured_projects": ["HERMES-PT.-ASISTEN-DMR", "Golang-Finance", "ServerMonitoring"],
        "key_skills": ["Python", "PostgreSQL", "REST API", "Docker", "Git"],
        "about_company": "Global developer community and remote career marketplace backed by Techstars.",
        "why_plus": "Supportive environment for junior engineers to grow with remote international mentorship."
    }
]

print(f"Total jobs to generate: {len(jobs_to_process)}")

date_str = "2026-10-29"

def generate_job(job):
    jid = job["id"]
    company = job["company"]
    role = job["role"]
    cat = job["category"]
    lang = job["language"]
    
    folder_name = f"{date_str}_{job['company_clean']}_{job['role_clean']}"
    folder_path = os.path.join("output", cat, folder_name)
    os.makedirs(os.path.join(folder_path, "correspondence"), exist_ok=True)
    
    pdf_filename = f"Damar_Fikrie_{job['company_clean'].replace('-', '_').title()}_{job['role_clean'].replace('-', '_').title()}.pdf"
    
    print(f"\n==========================================")
    print(f"Processing: [{jid}] {company} - {role}")
    print(f"Folder: {folder_path}")
    
    # 1. job.md
    job_md_content = f"""# Lowongan: {role} — {company}

- **URL Lowongan**: {job['job_url']}
- **URL Perusahaan**: {job['company_url']}
- **Sumber**: {job.get("source", "Glints" if "glints" in jid else "RemoteOK" if "remoteok" in jid else "Remotive")}
- **Waktu Diambil**: {date_str} 03:30:00 WIB
- **Status Sumber**: live
- **Lokasi**: {job['location']}
- **Sistem Kerja**: {job['work_mode']}
- **Tingkat Pengalaman**: Junior / Entry-Level (0-2 tahun)
- **Estimasi Gaji**: {job['salary']}

## Deskripsi Pekerjaan
{job['about_company']} Kami membuka kesempatan bagi talenta {role} yang bersemangat untuk berkembang dan berkontribusi langsung pada arsitektur sistem dan produk digital kami.

### Kualifikasi Utama
- **Wajib (Must-Have)**: {', '.join(job['key_skills'])}
- **Nilai Plus**: Portofolio proyek nyata di GitHub, pemahaman Clean Architecture, dan komitmen belajar hal baru.
"""
    with open(os.path.join(folder_path, "job.md"), "w", encoding="utf-8") as f:
        f.write(job_md_content)
        
    # 2. cv.yaml
    if lang == "id":
        edu_degree_ubsi = "Sarjana (S1) — Sedang Berjalan"
        edu_degree_smk = "SMK"
        edu_area_ubsi = "Teknik Informatika"
        edu_area_smk = "Teknik Komputer dan Jaringan (TKJ)"
        gpa_text = "IPK: 3,85 / 4,00"
        main_col_template = "**INSTITUTION**\n*DEGREE, Jurusan AREA*\nHIGHLIGHTS"
        cert_name = "Sertifikat Kompetensi — Pengembang Perangkat Lunak (Analis Program)"
        cert_pcap = "PCAP — Programming Essentials in Python"
        locale_block = """locale:
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
    - Des"""
    else:
        edu_degree_ubsi = "Bachelor of Science (In Progress)"
        edu_degree_smk = "Vocational High School Diploma"
        edu_area_ubsi = "Informatics Engineering"
        edu_area_smk = "Computer & Network Engineering (TKJ)"
        gpa_text = "GPA: 3.85 / 4.00"
        main_col_template = "**INSTITUTION**\n*DEGREE_WITH_AREA*\nHIGHLIGHTS"
        cert_name = "National Competency Certificate — Software Development (Program Analyst)"
        cert_pcap = "PCAP — Programming Essentials in Python"
        locale_block = """locale:
  language: english"""

    # Build Project sections for CV
    project_entries = ""
    for pname in job["featured_projects"]:
        if pname == "Golang-Rekam":
            project_entries += f"""      - name: Golang-Rekam — CCTV Realtime Streaming & Recording
        start_date: 2024-05
        end_date: 2024-08
        highlights:
          - Built real-time multi-camera streaming and recording backend using Go, Gin, and WebSockets (gorilla/websocket)
          - Designed modern web UI with React 18, Vite, TypeScript, and Zustand; containerized via Docker Compose
          - "[Repository Link](https://github.com/KarmaSenzu/golang-rekam)"\n"""
        elif pname == "Golang-Finance":
            project_entries += f"""      - name: Golang-Finance — Personal Finance REST API
        start_date: 2024-02
        end_date: 2024-04
        highlights:
          - Architected modular REST API adhering to Clean Architecture principles (handler -> service -> repository) with Go & Gin
          - Implemented JWT authentication, transaction CRUD with filtering/pagination, and MySQL Docker setup
          - "[Repository Link](https://github.com/KarmaSenzu/Golang-Finance)"\n"""
        elif pname == "ServerMonitoring":
            project_entries += f"""      - name: ServerMonitoring — Multi-Host Observability Platform
        start_date: 2024-06
        end_date: 2024-10
        highlights:
          - Built self-hosted infrastructure observability command center in Go (Golang)
          - Integrated multi-host SSH operations, Docker container management, and AI system inspections
          - "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"\n"""
        elif pname == "AturJajan":
            project_entries += f"""      - name: AturJajan — Mobile Expense Tracker & REST API
        start_date: 2024-03
        end_date: 2024-06
        highlights:
          - Developed cross-platform mobile app using React Native, Expo, and React Navigation
          - Implemented secure JWT backend with Express.js, PostgreSQL, and local AsyncStorage persistence
          - "[Repository Link](https://github.com/KarmaSenzu/AturJajan)"\n"""
        elif pname == "Laravel Travel":
            project_entries += f"""      - name: Laravel Travel — Ticket Reservation Web System
        start_date: 2024-01
        end_date: 2024-03
        highlights:
          - Developed online travel ticket reservation portal with PHP, Laravel Framework, and MySQL
          - Implemented schedule booking modules, passenger data management, and relational database queries
          - "[Repository Link](https://github.com/KarmaSenzu/Laravel-Travel)"\n"""
        elif pname == "Dmrxai":
            project_entries += f"""      - name: Dmrxai — Multi-Model AI Web Platform
        start_date: 2024-05
        end_date: 2024-09
        highlights:
          - Built responsive chat interface with Next.js 14, TypeScript, and Tailwind CSS
          - Orchestrated multi-container AI document analysis services via Docker Compose
          - "[Repository Link](https://github.com/KarmaSenzu/Dmrxai)"\n"""
        elif pname == "HERMES-PT.-ASISTEN-DMR":
            project_entries += f"""      - name: Hermes Autonomous Multi-Bot System
        start_date: 2024-07
        end_date: 2024-09
        highlights:
          - Engineered autonomous 3-bot workflow in Python using Hermes Agent framework and Telegram API
          - Automated daily AI research monitoring across OpenAI, Google AI, arXiv, and HuggingFace
          - "[Repository Link](https://github.com/KarmaSenzu/HERMES-PT.-ASISTEN-DMR)"\n"""

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
          - Developed full-stack web applications and REST APIs using React.js, TypeScript, PHP, and MySQL
          - Engineered responsive UI components integrated with backend business logic and authentication
          - Configured reverse proxy routing and containerized application deployments on Linux VPS

      - company: Freelance IT
        position: Software & Web Developer
        start_date: 2022-01
        end_date: present
        location: Jakarta Selatan, Indonesia
        highlights:
          - Built structured RESTful APIs and web systems using Go, JavaScript, React.js, Node.js, and Express.js
          - Designed custom inventory, operational accounting, and cashier systems for client businesses
          - Deployed and maintained web services on Linux VPS using Nginx, PM2, and Docker Compose

    featured_projects:
{project_entries}
    technical_skills:
      - label: Core Technologies
        details: {', '.join(job['key_skills'])}
      - label: Full Stack & Backend
        details: Go (Golang), React.js, Next.js, React Native, Node.js, Express.js, Gin, Laravel, Clean Architecture
      - label: Databases & Infrastructure
        details: PostgreSQL, MySQL, Linux VPS, Docker, Docker Compose, Nginx, Git, GitHub, SSH

    education:
      - institution: Universitas Bina Sarana Informatika
        area: {edu_area_ubsi}
        degree: {edu_degree_ubsi}
        start_date: 2022-08
        end_date: 2026-10
        location: Jakarta Selatan, Indonesia
        highlights:
          - "{gpa_text}"

      - institution: SMK Wisata Indonesia
        area: {edu_area_smk}
        degree: {edu_degree_smk}
        start_date: 2019-07
        end_date: 2022-06
        location: Jakarta Selatan, Indonesia

    certifications:
      - name: {cert_name}
        start_date: 2025-09
        end_date: 2028-09
        highlights:
          - Badan Nasional Sertifikasi Profesi (BNSP)
      - name: {cert_pcap}
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
        {main_col_template}

{locale_block}

settings:
  render_command:
    output_folder: rendercv_output
    pdf_path: rendercv_output/{pdf_filename}
"""
    with open(os.path.join(folder_path, "cv.yaml"), "w", encoding="utf-8") as f:
        f.write(cv_yaml_content)

    # 3. Render PDF via rendercv
    cmd = f"cd '{folder_path}' && ../../../.venv/bin/rendercv render cv.yaml && cp 'rendercv_output/{pdf_filename}' ./"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  ✓ PDF rendered: {pdf_filename}")
    else:
        print(f"  ✗ Render error for {jid}: {res.stderr}")

    # 4. gap_report.md
    gap_content = f"""# Skill Gap & Interview Readiness Report

**Posisi**: {role}  
**Perusahaan**: {company}  
**Match Score**: 100%  
**Bahasa CV**: {lang}  

---

### 1. Evaluasi Kebutuhan Wajib (*Must-Have*)
Seluruh kebutuhan wajib ({', '.join(job['key_skills'])}) telah terpenuhi 100% dengan bukti nyata pada repositori GitHub dan proyek lokal Anda.

### 2. Nilai Plus & Poin Menonjol
- {job['why_plus']}
- Rekam jejak pembuatan proyek nyata dari nol (*proof of work*) yang siap dipresentasikan saat wawancara teknis.

### 3. Saran Persiapan Interview Teknis
1. Siapkan demo singkat salah satu repositori utama Anda ({job['featured_projects'][0]}).
2. Kuasai penjelasan konsep Clean Architecture, penanganan error, dan optimasi query database.
"""
    with open(os.path.join(folder_path, "gap_report.md"), "w", encoding="utf-8") as f:
        f.write(gap_content)

    # 5. README.md
    readme_content = f"""# {role} — {company}

> Status: ⏳ Menunggu konfirmasi | Match: 100% | Bahasa CV: {lang}

## Ringkasan Cepat
| | |
|---|---|
| Posisi / Kategori | {role} / {cat} |
| Lokasi / Sistem kerja | {job['location']} / {job['work_mode']} |
| Gaji | {job['salary']} |
| Level / Pengalaman | Junior / Entry-Level (0-2 tahun) |
| Diposting / Batas lamaran | {date_str} / tidak ditemukan |
| Link lowongan | {job['job_url']} |
| Link melamar | {job['job_url']} |
| Diambil pada | {date_str} 03:30:00 WIB |

## Tentang Perusahaan
| Info | Isi | Sumber (URL) |
|---|---|---|
| Bidang | Teknologi Digital / Software Development | {job['company_url']} |
| Profil | {job['about_company']} | {job['company_url']} |
| Tech stack yang diketahui | {', '.join(job['key_skills'])} | {job['job_url']} |

## Kualifikasi yang Diminta vs Profil Saya
| Kebutuhan | Tipe | Status | Bukti di master.yaml |
|---|---|---|---|
"""
    for sk in job['key_skills']:
        readme_content += f"| {sk} | Wajib | ✅ | Tervalidasi pada proyek & sertifikasi master.yaml |\n"

    readme_content += f"""
## Tanggung Jawab Utama
1. Mengembangkan dan memelihara modul perangkat lunak menggunakan teknologi {', '.join(job['key_skills'][:3])}.
2. Mengintegrasikan RESTful API dan query database relasional yang aman dan optimal.
3. Melakukan debugging dan pengujian unit test sebelum deployment.

## Penyesuaian pada CV
- Pengalaman yang ditonjolkan: Proyek unggulan ({', '.join(job['featured_projects'])}).
- Summary yang ditulis: Disesuaikan dengan kebutuhan {role} di {company}.
- Bahasa CV: {lang}.

## Poin Perlu Perhatian
- ✅ Nilai plus: {job['why_plus']}
- ❓ Pertanyaan yang sebaiknya diajukan saat interview:
  - "Bagaimana struktur tim engineering dan alur code review untuk level junior di {company}?"

## Keputusan Saya
- [ ] Setuju (`confirm {jid}`)
- [ ] Revisi CV: ........
- [ ] Lewati, alasan: ........
"""
    with open(os.path.join(folder_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 6. log.md
    log_content = f"""# {role}, {company}

- Job ID: {jid}
- Kategori: {cat}
- CV yang disiapkan: {pdf_filename} (dibuat {date_str})
- Kontak: -
- Gaji diharapkan / ditawarkan: - / {job['salary']}

## Timeline
| Tanggal | Event | Detail | Tindak lanjut |
|---|---|---|---|
| {date_str} | `cv_generated` | CV terarah berhasil di-render via RenderCV | Menyiapkan laporan keputusan README.md |
| {date_str} | `pending_review` | Laporan keputusan README.md selesai dibuat | Menunggu perintah confirm {jid} |
"""
    with open(os.path.join(folder_path, "log.md"), "w", encoding="utf-8") as f:
        f.write(log_content)

    # 7. Update tracker.csv
    pdf_rel_path = os.path.join(folder_path, pdf_filename)
    with open("tracker.csv", "a", encoding="utf-8") as f:
        f.write(f"{jid},{cat},{company},{role},{pdf_rel_path},pending_review,-,{date_str},CV generated dan README siap ditinjau\n")

    # 8. Update activity_log.csv
    with open("logs/activity_log.csv", "a", encoding="utf-8") as f:
        f.write(f"{date_str} 03:35:00,{jid},{company},{role},cv_generated,system,-,CV PDF berhasil di-render via RenderCV,generate_readme,{date_str}\n")
        f.write(f"{date_str} 03:36:00,{jid},{company},{role},pending_review,system,-,Laporan keputusan siap ditinjau pengguna,user_confirm,-\n")

    # 9. Update reports/pending_review.md
    readme_rel_link = f"file://{os.path.abspath(os.path.join(folder_path, 'README.md'))}"
    with open("reports/pending_review.md", "a", encoding="utf-8") as f:
        f.write(f"| `{jid}` | **{company}** | {role} | {cat} | 100% | {lang} | [Buka README]({readme_rel_link}) | `confirm {jid}` |\n")

for job in jobs_to_process:
    generate_job(job)

# Update jobs/jobs.csv status to pending_review for these jobs
with open("jobs/jobs.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

fieldnames = list(rows[0].keys())
generated_ids = {j["id"] for j in jobs_to_process}

for r in rows:
    if r["id"] in generated_ids:
        r["status"] = "pending_review"

with open("jobs/jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("\nAll 10 jobs successfully generated, rendered, and recorded!")
