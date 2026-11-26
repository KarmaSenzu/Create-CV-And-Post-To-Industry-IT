import os, csv

previous_jobs_meta = [
    {
        "id": "glints-kolega-software-developer",
        "source": "glints",
        "title": "Software Developer (Full-Stack)",
        "company": "PT KOLEGA TEKNOLOGI INDONESIA",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Jakarta, Indonesia",
        "work_mode": "hybrid",
        "salary": "Rp5.740.000 - 6.500.000/Bulan",
        "experience_years": "0-2 years (Fresh Graduate welcome)",
        "level": "Junior / Associate",
        "must_have": "JavaScript;TypeScript;React;Next.js;RESTful API;PostgreSQL;MySQL;Git",
        "nice_to_have": "Docker;Linux VPS;Clean Architecture",
        "responsibilities": "Membangun dan mengoperasikan software untuk alur bisnis nyata mencakup frontend React/Next.js backend REST API dan basis data relasional.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/software-developer-full-stack/0eff72bb-f314-486c-8cbe-3da02ab5c0b0",
        "apply_url": "https://glints.com/id/opportunities/jobs/software-developer-full-stack/0eff72bb-f314-486c-8cbe-3da02ab5c0b0",
        "company_url": "https://kolega.co.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "https://glints.com/id/companies/pt-kolega-teknologi-indonesia/f804409e-fa5d-484e-8ae2-f2365027c0b3",
        "retrieved_at": "2026-10-29 12:00:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-solusi-kode-software-engineer",
        "source": "glints",
        "title": "Software Engineer",
        "company": "PT. Solusi Kode Indonesia",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Jakarta Selatan, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Rp 5.000.000 - 7.000.000 / bulan",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior",
        "must_have": "JavaScript;TypeScript;React.js;Node.js;PostgreSQL;RESTful API;Git",
        "nice_to_have": "Docker;Linux;Clean Architecture",
        "responsibilities": "Mengembangkan antarmuka aplikasi web dan integrasi API backend untuk solusi sistem klien korporasi.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/software-engineer/54b4fe4f-45b1-47d6-8fde-03f64c841e35",
        "apply_url": "https://glints.com/id/opportunities/jobs/software-engineer/54b4fe4f-45b1-47d6-8fde-03f64c841e35",
        "company_url": "https://solusikode.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-truf-software-engineer",
        "source": "glints",
        "title": "Software Engineer",
        "company": "PT Truf Teknologi Indonesia",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Bekasi / Jakarta, Indonesia",
        "work_mode": "hybrid",
        "salary": "Rp 5.000.000 - 12.000.000 / bulan",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior / Associate",
        "must_have": "JavaScript;React;Node.js;Go;REST API;PostgreSQL;Git",
        "nice_to_have": "WebSockets;Docker;Linux VPS",
        "responsibilities": "Membangun fitur aplikasi modern berskala besar, optimasi endpoint backend berkinerja tinggi, dan integrasi database relasional.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/software-engineer/4abb53d3-2b97-413f-b5c9-748aaba75664",
        "apply_url": "https://glints.com/id/opportunities/jobs/software-engineer/4abb53d3-2b97-413f-b5c9-748aaba75664",
        "company_url": "https://truf.co.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-msbu-software-developer",
        "source": "glints",
        "title": "Software Developer",
        "company": "MSBU",
        "category": "01-fullstack",
        "category_secondary": "03-frontend",
        "location": "Jakarta Pusat, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Perusahaan tidak menampilkan gaji",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior",
        "must_have": "JavaScript;TypeScript;React.js;Next.js;REST API;MySQL;Git",
        "nice_to_have": "Tailwind CSS;PostgreSQL;Clean Code",
        "responsibilities": "Mengembangkan antarmuka portal enterprise interaktif dan menyambungkannya dengan REST API internal perusahaan.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/software-developer/66c8002a-4953-4e90-b8a3-625d58e7feb8",
        "apply_url": "https://glints.com/id/opportunities/jobs/software-developer/66c8002a-4953-4e90-b8a3-625d58e7feb8",
        "company_url": "https://msbu.co.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-aldmic-software-engineer",
        "source": "glints",
        "title": "Software Engineer",
        "company": "Aldmic COOPN Digital",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Jakarta Barat, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Perusahaan tidak menampilkan gaji",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior / Associate",
        "must_have": "JavaScript;PHP;Go;PostgreSQL;MySQL;REST API;Git",
        "nice_to_have": "Docker;Linux VPS;Payment Gateway Integration",
        "responsibilities": "Membangun dan memelihara sistem digital reward & e-voucher transaction engine dengan keandalan backend tinggi.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/software-engineer/635f5e15-cd17-43ee-9e18-632fdf122671",
        "apply_url": "https://glints.com/id/opportunities/jobs/software-engineer/635f5e15-cd17-43ee-9e18-632fdf122671",
        "company_url": "https://aldmic.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-adi-perdana-backend",
        "source": "glints",
        "title": "Backend Developer",
        "company": "PT Adi Perdana Nusantara",
        "category": "02-backend",
        "category_secondary": "01-fullstack",
        "location": "Jakarta Utara, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Rp 5.800.000 - 8.700.000 / bulan",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior",
        "must_have": "Node.js;Go;RESTful API;PostgreSQL;MySQL;Git",
        "nice_to_have": "Redis;Docker;Linux VPS",
        "responsibilities": "Merancang arsitektur API backend, penanganan query transaksi database relasional, dan integrasi modul sistem bisnis.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/backend-developer/9bf4cbda-d60a-44b7-b7d2-5a2ad9b2725e",
        "apply_url": "https://glints.com/id/opportunities/jobs/backend-developer/9bf4cbda-d60a-44b7-b7d2-5a2ad9b2725e",
        "company_url": "https://adiperdana.co.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-sigmatech-backend-developer",
        "source": "glints",
        "title": "Backend Developer",
        "company": "PT Sigma Global Teknologi",
        "category": "02-backend",
        "category_secondary": "05-devops-cloud",
        "location": "Jakarta Selatan, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Kompetitif",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior",
        "must_have": "Go;PostgreSQL;MySQL;RESTful API Architecture;Git",
        "nice_to_have": "Docker;Linux VPS;Clean Architecture",
        "responsibilities": "Mengembangkan endpoint microservices berbasis Go untuk sistem perbankan dan transaksi enterprise klien.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/backend-developer/b607feb2-dcb2-4bb4-bbbd-f0d20d90dcc1",
        "apply_url": "https://glints.com/id/opportunities/jobs/backend-developer/b607feb2-dcb2-4bb4-bbbd-f0d20d90dcc1",
        "company_url": "https://sigmatech.co.id",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-enigma-backend-engineer",
        "source": "glints",
        "title": "Backend Engineer",
        "company": "PT. Enigma Cipta Humanika (Enigma Camp)",
        "category": "02-backend",
        "category_secondary": "01-fullstack",
        "location": "Jakarta Selatan, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Kompetitif",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior / Entry-Level",
        "must_have": "Go;Java;PostgreSQL;REST API;Clean Architecture;Git",
        "nice_to_have": "Docker;Linux;Unit Testing",
        "responsibilities": "Menerapkan standard coding best-practice pada microservice backend, optimasi query relasional, dan integrasi sistem.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/backend-engineer/2849d0be-4539-44d5-9787-a7e20500cac7",
        "apply_url": "https://glints.com/id/opportunities/jobs/backend-engineer/2849d0be-4539-44d5-9787-a7e20500cac7",
        "company_url": "https://enigmacamp.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "applied"
    },
    {
        "id": "glints-trimegah-fullstack-engineer",
        "source": "glints",
        "title": "Full Stack Engineer",
        "company": "Trimegah Sekuritas",
        "category": "01-fullstack",
        "category_secondary": "02-backend",
        "location": "Jakarta Selatan, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Kompetitif (Dirahasiakan)",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior",
        "must_have": "TypeScript;React;Node.js;Go;PostgreSQL;WebSockets;Git",
        "nice_to_have": "Docker;Financial Tech;Clean Code",
        "responsibilities": "Membangun modul antarmuka trading/investasi modern, integrasi streaming harga real-time WebSockets, dan arsitektur database relasional.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/full-stack-engineer/93fd68c1-0130-4d92-8d7e-383d3095a568",
        "apply_url": "https://glints.com/id/opportunities/jobs/full-stack-engineer/93fd68c1-0130-4d92-8d7e-383d3095a568",
        "company_url": "https://trimegah.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "skipped"
    },
    {
        "id": "glints-trimegah-backend-developer",
        "source": "glints",
        "title": "Backend Developer",
        "company": "Trimegah Sekuritas",
        "category": "02-backend",
        "category_secondary": "01-fullstack",
        "location": "Jakarta Selatan, DKI Jakarta",
        "work_mode": "hybrid",
        "salary": "Kompetitif (Dirahasiakan)",
        "experience_years": "0-2 tahun (Fresh Graduate welcome)",
        "level": "Junior",
        "must_have": "Go;PostgreSQL;RESTful API;WebSockets;Microservices;Git",
        "nice_to_have": "Docker;Linux;Clean Architecture",
        "responsibilities": "Merancang backend engine transaksi berkecepatan tinggi, integrasi database PostgreSQL, dan pemrosesan antrean data.",
        "language": "id",
        "posted_date": "2026-10-29",
        "deadline": "tidak ditemukan",
        "job_url": "https://glints.com/id/opportunities/jobs/backend-developer/c3a06b1e-35f6-4c96-8cef-40b978d6b09f",
        "apply_url": "https://glints.com/id/opportunities/jobs/backend-developer/c3a06b1e-35f6-4c96-8cef-40b978d6b09f",
        "company_url": "https://trimegah.com",
        "careers_url": "tidak ditemukan",
        "company_profile_url": "tidak ditemukan",
        "retrieved_at": "2026-10-29 12:55:00",
        "source_status": "live",
        "match_score": "100%",
        "missing_skills": "none",
        "status": "skipped"
    }
]

# 1. Read existing 8 junior jobs from tracker.csv
current_tracker_rows = []
with open("tracker.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        current_tracker_rows.append(row)

# 2. Read previous 10 jobs from tracker_history.csv
previous_tracker_rows = []
with open("tracker_history.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        previous_tracker_rows.append(row)

# Combined tracker: 8 pending_review first, then 8 applied, then 2 skipped
all_tracker_rows = current_tracker_rows + previous_tracker_rows

with open("tracker.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "job_id","category","company","role","cv_path","status","applied_date","last_update","notes"
    ])
    writer.writeheader()
    writer.writerows(all_tracker_rows)

print(f"✓ tracker.csv updated: Total {len(all_tracker_rows)} jobs (8 pending_review, 8 applied, 2 skipped)")

# 3. Read current 8 jobs from jobs/jobs.csv
current_jobs_rows = []
with open("jobs/jobs.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        current_jobs_rows.append(row)

all_jobs_rows = current_jobs_rows + previous_jobs_meta

with open("jobs/jobs.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "id","source","title","company","category","category_secondary","location","work_mode",
        "salary","experience_years","level","must_have","nice_to_have","responsibilities","language",
        "posted_date","deadline","job_url","apply_url","company_url","careers_url",
        "company_profile_url","retrieved_at","source_status","match_score","missing_skills","status"
    ])
    writer.writeheader()
    writer.writerows(all_jobs_rows)

print(f"✓ jobs/jobs.csv updated: Total {len(all_jobs_rows)} jobs preserved in database.")
