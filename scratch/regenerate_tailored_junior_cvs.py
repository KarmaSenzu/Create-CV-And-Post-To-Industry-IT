import os, sys, subprocess

tailored_jobs = [
    {
        "id": "glints-nusantara-sakti-programmer-junior",
        "cat": "01-fullstack",
        "folder": "2026-10-29_nusantara-sakti_programmer-junior",
        "pdf_filename": "Damar_Fikrie_Nusantara_Sakti_Programmer_Junior.pdf",
        "headline": "Programmer Junior (PHP / Laravel / Java / MySQL)",
        "summary": "Programmer Junior lulusan Sarjana Komputer (S.Kom. Cum Laude, IPK 3.85) dengan sertifikasi BNSP Pengembang Perangkat Lunak. Berpengalaman membangun aplikasi web berbasis PHP (Laravel & CodeIgniter), aplikasi desktop kasir/POS dengan Java & MySQL, serta perancangan database relasional yang terstruktur.",
        "skills_core": "PHP (Laravel, CodeIgniter), Java, MySQL, RESTful API, Object-Oriented Programming (OOP)",
        "skills_lang": "PHP, Java, Go (Golang), JavaScript, SQL, HTML5, CSS3, Linux Shell, Git",
        "skills_infra": "MySQL, PostgreSQL, Apache/Nginx, Docker, Linux VPS, Database Normalization & Query Tuning",
        "projects": [
            {
                "name": "Laravel Travel — Sistem Reservasi & Pemesanan Tiket Web",
                "start": "2024-01",
                "end": "2024-03",
                "highlights": [
                    "Membangun portal reservasi tiket travel berbasis web menggunakan PHP, Laravel Framework, dan database MySQL",
                    "Mengimplementasikan modul pemilihan jadwal keberangkatan, pemesanan tiket penumpang, dan transaksi data relasional",
                    "[Repository Link](https://github.com/KarmaSenzu/Laravel-Travel)"
                ]
            },
            {
                "name": "Program-Aplikasi-Kasir-Java — Desktop Point of Sale & Inventory",
                "start": "2023-10",
                "end": "2024-01",
                "highlights": [
                    "Merancang aplikasi kasir desktop (POS) menerapkan Object-Oriented Programming (OOP) berbasis Java dan MySQL",
                    "Memfasilitasi transaksi kasir cepat, pencatatan nota transaksi, dan pendataan barang dagangan terintegrasi database",
                    "[Repository Link](https://github.com/KarmaSenzu/Program-Aplikasi-Kasir-Java)"
                ]
            },
            {
                "name": "CI4-Perpuspus-2 — Sistem Informasi Manajemen & Katalog Perpustakaan",
                "start": "2023-06",
                "end": "2023-09",
                "highlights": [
                    "Mengembangkan aplikasi web perpustakaan dengan PHP CodeIgniter 4 dan database relasional MySQL",
                    "Mengelola katalog buku, pencatatan peminjaman, dan otomasi manajemen data anggota perpustakaan",
                    "[Repository Link](https://github.com/KarmaSenzu/CI4-Perpuspus-2)"
                ]
            }
        ]
    },
    {
        "id": "glints-istidata-junior-developer",
        "cat": "01-fullstack",
        "folder": "2026-10-29_istidata-indopacific_junior-developer",
        "pdf_filename": "Damar_Fikrie_Istidata_Indopacific_Junior_Developer.pdf",
        "headline": "Junior Developer (Java / REST API / SQL / Clean Architecture)",
        "summary": "Junior Developer lulusan Sarjana Komputer (S.Kom. Cum Laude, IPK 3.85) bersertifikasi BNSP Pengembang Perangkat Lunak. Menguasai paradigma Object-Oriented Programming (OOP) dengan Java, perancangan database relasional SQL (PostgreSQL & MySQL), dan arsitektur backend REST API modular.",
        "skills_core": "Java, SQL, PostgreSQL, MySQL, RESTful API, Object-Oriented Programming (OOP), Git",
        "skills_lang": "Java, Go (Golang), Python, PHP, JavaScript, SQL, Linux Shell",
        "skills_infra": "PostgreSQL, MySQL, Clean Architecture, Docker, Linux VPS, Git, Microservices",
        "projects": [
            {
                "name": "Program-Aplikasi-Kasir-Java — Desktop Point of Sale & Database Engine",
                "start": "2023-10",
                "end": "2024-01",
                "highlights": [
                    "Membangun aplikasi desktop POS menerapkan prinsip OOP berbasis Java dan database relasional MySQL",
                    "Merancang arsitektur data transaksi kasir, kalkulasi nota belanja, dan manajemen inventaris stok barang",
                    "[Repository Link](https://github.com/KarmaSenzu/Program-Aplikasi-Kasir-Java)"
                ]
            },
            {
                "name": "Golang-Finance — RESTful Financial Transaction API & Clean Architecture",
                "start": "2024-02",
                "end": "2024-04",
                "highlights": [
                    "Merancang modular REST API menerapkan Clean Architecture (handler -> service -> repository) dengan Go & Gin",
                    "Mengimplementasikan autentikasi JWT, transaksi database relasional MySQL/PostgreSQL, dan Docker setup",
                    "[Repository Link](https://github.com/KarmaSenzu/Golang-Finance)"
                ]
            },
            {
                "name": "ServerMonitoring — Observability & Infrastructure Command Center",
                "start": "2024-06",
                "end": "2024-10",
                "highlights": [
                    "Membangun sistem monitoring utilisasi CPU, memori, disk, dan jaringan multi-server secara real-time",
                    "Mengintegrasikan operasi SSH multi-host, manajemen container Docker, dan alerting otomatis",
                    "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"
                ]
            }
        ]
    },
    {
        "id": "glints-syariah-bisnis-junior-software-developer",
        "cat": "01-fullstack",
        "folder": "2026-10-29_syariah-bisnis_junior-software-developer",
        "pdf_filename": "Damar_Fikrie_Syariah_Bisnis_Junior_Software_Developer.pdf",
        "headline": "Junior Software Developer (React / Next.js / TypeScript / Node.js)",
        "summary": "Software Developer dengan keahlian utama dalam ekosistem React.js, Next.js, TypeScript, dan backend Node.js. Berpengalaman membangun platform web modern, antarmuka responsif, dan integrasi API yang aman.",
        "skills_core": "React.js, Next.js, TypeScript, JavaScript, Node.js, Express.js, RESTful API, PostgreSQL",
        "skills_lang": "TypeScript, JavaScript, Go, Python, PHP, SQL, HTML5, CSS3, Tailwind CSS",
        "skills_infra": "PostgreSQL, MySQL, Docker Compose, Linux VPS, Nginx, Git, RESTful Web Services",
        "projects": [
            {
                "name": "Dmrxai — Multi-Model AI Web Platform",
                "start": "2024-05",
                "end": "2024-09",
                "highlights": [
                    "Membangun platform web responsif menggunakan Next.js 14, TypeScript, dan Tailwind CSS",
                    "Mengorkestrasi modul analisis dokumen dan pencarian data multi-kontainer via Docker Compose",
                    "[Repository Link](https://github.com/KarmaSenzu/Dmrxai)"
                ]
            },
            {
                "name": "Golang-Rekam — Modern Web UI & Streaming Platform",
                "start": "2024-05",
                "end": "2024-08",
                "highlights": [
                    "Merancang antarmuka web modern dengan React 18, Vite, TypeScript, dan manajemen state Zustand",
                    "Mengintegrasikan UI dengan streaming video real-time WebSockets dan backend berkinerja tinggi",
                    "[Repository Link](https://github.com/KarmaSenzu/golang-rekam)"
                ]
            },
            {
                "name": "AturJajan — Mobile Expense Tracker & REST API",
                "start": "2024-03",
                "end": "2024-06",
                "highlights": [
                    "Mengembangkan aplikasi mobile cross-platform menggunakan React Native, Expo, dan React Navigation",
                    "Membangun backend REST API dengan Express.js, PostgreSQL, dan autentikasi token JWT yang aman",
                    "[Repository Link](https://github.com/KarmaSenzu/AturJajan)"
                ]
            }
        ]
    },
    {
        "id": "glints-skyshi-junior-fullstack-dev",
        "cat": "01-fullstack",
        "folder": "2026-10-29_skyshi-digital_junior-fullstack-developer",
        "pdf_filename": "Damar_Fikrie_Skyshi_Digital_Junior_Fullstack_Developer.pdf",
        "headline": "Junior Fullstack Developer (React.js / Laravel / Node.js)",
        "summary": "Fullstack Developer dengan portofolio proyek web end-to-end yang kuat. Terbiasa memadukan frontend interaktif (React.js/Next.js) dengan backend terstruktur (Laravel PHP & Node.js/Go) serta database relasional.",
        "skills_core": "React.js, Next.js, Laravel (PHP), Node.js, RESTful API, PostgreSQL, MySQL, Git",
        "skills_lang": "JavaScript, TypeScript, PHP, Go (Golang), SQL, HTML5, CSS3, Tailwind CSS",
        "skills_infra": "MySQL, PostgreSQL, Docker, Docker Compose, Linux VPS, Nginx, Agile Development",
        "projects": [
            {
                "name": "Laravel Travel — Fullstack Web System & Booking Portal",
                "start": "2024-01",
                "end": "2024-03",
                "highlights": [
                    "Membangun portal reservasi tiket travel lengkap dari modul pemesanan hingga database relasional MySQL",
                    "Menerapkan arsitektur MVC Laravel dengan Blade templating dan validasi formulir terstruktur",
                    "[Repository Link](https://github.com/KarmaSenzu/Laravel-Travel)"
                ]
            },
            {
                "name": "Dmrxai — Multi-Model AI Web Platform",
                "start": "2024-05",
                "end": "2024-09",
                "highlights": [
                    "Membangun platform web responsif modern menggunakan Next.js 14, TypeScript, dan Tailwind CSS",
                    "Mengintegrasikan komponen antarmuka dengan REST API dan backend microservices via Docker Compose",
                    "[Repository Link](https://github.com/KarmaSenzu/Dmrxai)"
                ]
            },
            {
                "name": "Golang-Finance — Personal Finance REST API",
                "start": "2024-02",
                "end": "2024-04",
                "highlights": [
                    "Merancang modular REST API menerapkan Clean Architecture (handler -> service -> repository) dengan Go",
                    "Mengimplementasikan autentikasi JWT, transaksi database relasional MySQL/PostgreSQL, dan Docker setup",
                    "[Repository Link](https://github.com/KarmaSenzu/Golang-Finance)"
                ]
            }
        ]
    },
    {
        "id": "glints-gits-junior-data-engineer",
        "cat": "06-data-ai",
        "folder": "2026-10-29_gits-indonesia_junior-data-engineer",
        "pdf_filename": "Damar_Fikrie_Gits_Indonesia_Junior_Data_Engineer.pdf",
        "headline": "Junior Data Engineer (Python / PostgreSQL / ETL / Pipeline)",
        "summary": "Junior Data & Backend Engineer lulusan S.Kom Cum Laude (IPK 3.85) dengan kemampuan scripting Python, manipulasi data relasional SQL (PostgreSQL), pemrosesan data otomatis (ETL pipeline), dan observabilitas sistem.",
        "skills_core": "Python, SQL, PostgreSQL, MySQL, Data Pipeline (ETL), Cron Automation, Git, Linux VPS",
        "skills_lang": "Python, SQL, Go (Golang), Shell/Bash Scripting, JavaScript",
        "skills_infra": "PostgreSQL, MySQL, Timeseries Data, Docker, Linux Server, Git, REST API Integration",
        "projects": [
            {
                "name": "HERMES-PT.-ASISTEN-DMR — Multi-Source Automated Data Pipeline",
                "start": "2024-07",
                "end": "2024-09",
                "highlights": [
                    "Mengembangkan sistem pipeline pengumpulan data otomatis dari berbagai sumber (arXiv, HuggingFace, GitHub, AI APIs)",
                    "Menerapkan parsing data terstruktur, transformasi JSON, dan otomasi distribusi berkala via scheduled cron",
                    "[Repository Link](https://github.com/KarmaSenzu/HERMES-PT.-ASISTEN-DMR)"
                ]
            },
            {
                "name": "Auto-Subtitle-AI — Speech-to-Text & Automated Audio/Data Processing",
                "start": "2024-04",
                "end": "2024-06",
                "highlights": [
                    "Merancang pipeline pemrosesan data audio-ke-teks otomatis presisi tinggi berbasis Python dan Faster-Whisper",
                    "Mengimplementasikan struktur data subtitle format ASS dan integrasi pipeline render video via FFmpeg",
                    "[Local Directory Portfolio: Auto Subtitle Editing]"
                ]
            },
            {
                "name": "Golang-Finance — Relational Database Schema & Data Integrity",
                "start": "2024-02",
                "end": "2024-04",
                "highlights": [
                    "Merancang skema relasional, optimasi query transaksi keuangan, dan validasi integritas data ACID",
                    "Menerapkan filtering, pagination, dan penanganan relasi database relasional PostgreSQL & MySQL",
                    "[Repository Link](https://github.com/KarmaSenzu/Golang-Finance)"
                ]
            }
        ]
    },
    {
        "id": "glints-willfitness-it-support",
        "cat": "99-other",
        "folder": "2026-10-29_willfitness_it-support-specialist",
        "pdf_filename": "Damar_Fikrie_Willfitness_It_Support_Specialist.pdf",
        "headline": "IT Support Specialist (Hardware / Network / Windows & Linux OS)",
        "summary": "Tenaga IT Support profesional dengan latar belakang Sarjana Komputer (S.Kom. Cum Laude) dan sertifikasi BNSP. Terlatih dalam perakitan dan troubleshooting perangkat keras/lunak, routing dan setup jaringan kantor LAN/WiFi, administrasi OS Windows & Linux, serta pemeliharaan infrastruktur operasional.",
        "skills_core": "Hardware Troubleshooting, LAN/WLAN Networking, Windows & Linux OS, IT Helpdesk, Perawatan Periferal",
        "skills_lang": "Shell Scripting, Command Line, PowerShell, Windows Server/Desktop, Ubuntu Linux",
        "skills_infra": "TCP/IP, DNS, DHCP, WiFi Router Setup, Remote Desktop (AnyDesk/RDP), PC Assembly, Backup Data",
        "projects": [
            {
                "name": "ServerMonitoring — Infrastructure & Host Monitoring Center",
                "start": "2024-06",
                "end": "2024-10",
                "highlights": [
                    "Mengelola pemantauan utilisasi CPU, memori, disk, dan konektivitas jaringan multi-server secara real-time",
                    "Mengotomatisasi diagnosa kesehatan sistem, operasi remote SSH, dan penanganan peringatan dini beban server",
                    "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"
                ]
            },
            {
                "name": "Linux & Windows Infrastructure Administration & Networking",
                "start": "2023-01",
                "end": "present",
                "highlights": [
                    "Mengonfigurasi server Linux VPS, routing firewall, setup reverse proxy Nginx, dan manajemen pengguna jaringan kantor",
                    "Melakukan troubleshooting konektivitas jaringan LAN/WLAN, penanganan error driver, dan pemeliharaan sistem berkala",
                    "[Infrastructure Portfolio: Self-Hosted Server & VPS]"
                ]
            },
            {
                "name": "Hardware Diagnostic & Workstation Maintenance",
                "start": "2022-01",
                "end": "present",
                "highlights": [
                    "Berpengalaman dalam perakitan PC, instalasi sistem operasi Windows & Linux, konfigurasi printer, dan diagnosa komponen fisik",
                    "Memberikan dukungan teknis cepat (*end-user support*) untuk mengatasi gangguan software maupun jaringan",
                    "[Technical Support Operations]"
                ]
            }
        ]
    },
    {
        "id": "glints-karya-transaksi-it-support",
        "cat": "99-other",
        "folder": "2026-10-29_karya-transaksi-retailindo_it-support",
        "pdf_filename": "Damar_Fikrie_Karya_Transaksi_Retailindo_It_Support.pdf",
        "headline": "IT Support (POS System / Retail Transactions / Hardware & Network)",
        "summary": "IT Support dengan spesialisasi pemeliharaan sistem Point of Sale (POS), alur transaksi retail digital, troubleshooting jaringan kasir, dan penanganan kendala teknis operasional harian merchant.",
        "skills_core": "POS System Support, Retail Hardware Troubleshooting, Network LAN/WiFi, Windows OS, Database Maintenance",
        "skills_lang": "SQL Query (MySQL), Shell/Command Prompt, Windows Desktop/Server, Linux",
        "skills_infra": "POS Peripherals, Thermal Printer, Barcode Scanner, LAN Switch, Router WiFi, MySQL Backup",
        "projects": [
            {
                "name": "Program-Aplikasi-Kasir-Java — Point of Sale (POS) & Transaction System",
                "start": "2023-10",
                "end": "2024-01",
                "highlights": [
                    "Memahami arsitektur perangkat lunak kasir POS, pencatatan nota transaksi, dan penanganan database lokal retail",
                    "Melakukan pengujian transaksi pembayaran kasir, pencetakan nota, dan troubleshooting integritas data barang",
                    "[Repository Link](https://github.com/KarmaSenzu/Program-Aplikasi-Kasir-Java)"
                ]
            },
            {
                "name": "Mentari-Smart-Warehouse — Smart Inventory & Stock Management",
                "start": "2025-06",
                "end": "2025-11",
                "highlights": [
                    "Mengembangkan modul manajemen inventaris barang gudang dan penomoran kode stok otomatis untuk operasional retail",
                    "Memastikan keakuratan data stok barang dagangan dan integrasi sistem pencatatan dengan operasional fisik",
                    "[Local Directory Portfolio: Mentari Solusi Indonesia]"
                ]
            },
            {
                "name": "ServerMonitoring — Infrastructure & Terminal Uptime Monitor",
                "start": "2024-06",
                "end": "2024-10",
                "highlights": [
                    "Memantau ketersediaan jaringan terminal transaksi kasir dan infrastruktur server secara konsisten",
                    "Mengirimkan notifikasi instan saat terjadi pemutusan jaringan atau lonjakan utilisasi perangkat",
                    "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"
                ]
            }
        ]
    },
    {
        "id": "glints-dutagaruda-it-support",
        "cat": "99-other",
        "folder": "2026-10-29_dutagaruda-piranti-prima_it-technical-support",
        "pdf_filename": "Damar_Fikrie_Dutagaruda_Piranti_Prima_It_Technical_Support.pdf",
        "headline": "IT Technical Support (Hardware / Network Configuration / End-User Support)",
        "summary": "Teknisi IT Support berorientasi solusi dengan keahlian troubleshooting perangkat keras PC/Laptop, penarikan & konfigurasi kabel jaringan LAN/WAN, instalasi software berlisensi, serta layanan bantuan teknis (*helpdesk ticketing*) yang komunikatif dan sigap.",
        "skills_core": "Technical Support, Hardware Maintenance, Network Cabling & Configuration, Windows & Linux, Helpdesk",
        "skills_lang": "Command Prompt/PowerShell, Linux Shell, TCP/IP Utilities (ping, traceroute, netstat)",
        "skills_infra": "Crimping RJ45, LAN Cabling, Switch, Router WiFi, Printer Sharing, Remote Desktop, Antivirus Deployment",
        "projects": [
            {
                "name": "ServerMonitoring — Network & Host Incident Alerting Platform",
                "start": "2024-06",
                "end": "2024-10",
                "highlights": [
                    "Membangun platform pemantauan status konektivitas jaringan dan kesehatan host kerja secara terpusat",
                    "Mengotomatisasi diagnosa respon latency jaringan (ping), utilisasi memori, dan alerting insiden teknis",
                    "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"
                ]
            },
            {
                "name": "Workstation & Network Deployment Operations",
                "start": "2023-01",
                "end": "present",
                "highlights": [
                    "Melakukan instalasi sistem operasi Windows/Linux, konfigurasi IP Static/DHCP, printer sharing, dan antivirus",
                    "Menangani crimping kabel UTP RJ45, pengujian konektivitas LAN/WLAN, dan manajemen perangkat periferal",
                    "[Technical Support Operations]"
                ]
            },
            {
                "name": "Program-Aplikasi-Kasir-Java — Client-Server Database Setup",
                "start": "2023-10",
                "end": "2024-01",
                "highlights": [
                    "Melakukan konfigurasi koneksi jaringan client-server antara workstation pengguna dengan server database lokal",
                    "Menangani troubleshooting perizinan port database, instalasi Java Runtime Environment (JRE), dan driver",
                    "[Repository Link](https://github.com/KarmaSenzu/Program-Aplikasi-Kasir-Java)"
                ]
            }
        ]
    }
]

print(f"Mulai me-regenerate CV Tailored spesifik untuk {len(tailored_jobs)} lowongan...")

for item in tailored_jobs:
    folder_path = os.path.join("output", item["cat"], item["folder"])
    os.makedirs(folder_path, exist_ok=True)
    pdf_filename = item["pdf_filename"]

    # Build Project YAML block
    projects_yaml = ""
    for p in item["projects"]:
        projects_yaml += f"""      - name: {p['name']}
        start_date: {p['start']}
        end_date: {p['end']}
        highlights:
"""
        for h in p["highlights"]:
            projects_yaml += f"          - \"{h}\"\n"

    cv_yaml = f"""# yaml-language-server: $schema=https://raw.githubusercontent.com/rendercv/rendercv/refs/tags/v2.8/schema.json
cv:
  name: Damar Fikrie
  headline: {item['headline']}
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
      - {item['summary']}

    experience:
      - company: Mentari Solusi Indonesia
        position: Full Stack & IT Systems Specialist
        start_date: 2025-06
        end_date: 2025-11
        location: Jakarta, Indonesia
        highlights:
          - Mengembangkan aplikasi web dan sistem inventaris pergudangan terintegrasi database relasional
          - Merancang formulir manajemen barang dinamis, penomoran kode stok otomatis, dan validasi data real-time
          - Mengonfigurasi deployment containerized pada Linux VPS dan reverse proxy Nginx

      - company: Freelance IT
        position: Software & Technical Specialist
        start_date: 2022-01
        end_date: present
        location: Jakarta Selatan, Indonesia
        highlights:
          - Mengembangkan aplikasi web, sistem kasir/POS desktop, dan RESTful API terstruktur untuk klien bisnis
          - Melakukan instalasi perangkat keras/lunak, setup jaringan LAN/WiFi, dan pemeliharaan sistem komputer
          - Mengelola dan memelihara server Linux VPS dengan Nginx, PM2, Docker Compose, dan backup berkala

    featured_projects:
{projects_yaml}
    technical_skills:
      - label: Kompetensi Utama
        details: "{item['skills_core']}"
      - label: Bahasa & Framework
        details: "{item['skills_lang']}"
      - label: Sistem & Infrastruktur
        details: "{item['skills_infra']}"

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

    cv_yaml_path = os.path.join(folder_path, "cv.yaml")
    with open(cv_yaml_path, "w", encoding="utf-8") as f:
        f.write(cv_yaml)

    # Render via rendercv
    cmd = f"cd '{folder_path}' && ../../../.venv/bin/rendercv render cv.yaml && cp 'rendercv_output/{pdf_filename}' ./"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  ✓ Berhasil di-render: {pdf_filename}")
    else:
        print(f"  ✗ Render error pada {item['id']}: {res.stderr[:200]}")

print("✓ Selesai meregenerasi seluruh CV tailored spesifik sesuai lowongan!")
