import os, sys, subprocess

detailed_jobs = [
    {
        "id": "glints-syariah-bisnis-junior-software-developer",
        "cat": "01-fullstack",
        "folder": "2026-10-29_syariah-bisnis_junior-software-developer",
        "pdf_filename": "Damar_Fikrie_Syariah_Bisnis_Junior_Software_Developer.pdf",
        "headline": "Junior Software Developer (React.js / Next.js / TypeScript / Node.js)",
        "summary": "Software Developer lulusan Sarjana Komputer (S.Kom. Cum Laude, IPK 3.85) dengan sertifikasi BNSP Pengembang Perangkat Lunak. Memiliki keahlian kuat dalam ekosistem React.js, Next.js 14, TypeScript, dan backend Node.js. Berpengalaman membangun platform aplikasi web interaktif, modul analisis cerdas, dan integrasi API yang aman.",
        "skills_core": "React.js, Next.js 14, TypeScript, JavaScript, Node.js, Express.js, RESTful API, PostgreSQL",
        "skills_lang": "TypeScript, JavaScript, Go, Python, PHP, SQL, HTML5, CSS3, Tailwind CSS",
        "skills_infra": "PostgreSQL, MySQL, Docker Compose, Linux VPS, Nginx, Git, RESTful Web Services",
        "projects": [
            {
                "name": "Dmrxai — Multi-Model AI Assistant & Document Intelligence Platform",
                "start": "2024-05",
                "end": "2024-09",
                "highlights": [
                    "Membangun platform AI mandiri (self-hosted) yang berfungsi menganalisis dokumen teknis kompleks, riset data otonom, dan visualisasi data interaktif",
                    "Mengembangkan antarmuka responsif menggunakan Next.js 14, TypeScript, dan Tailwind CSS; diorkestrasi secara modular via Docker Compose",
                    "[Repository Link](https://github.com/KarmaSenzu/Dmrxai)"
                ]
            },
            {
                "name": "Golang-Rekam — CCTV Real-time Streaming & Web Surveillance Center",
                "start": "2024-05",
                "end": "2024-08",
                "highlights": [
                    "Engine sentral pemantauan CCTV yang berfungsi menangkap feed multi-kamera RTSP dan mengonversinya menjadi streaming berlatensi rendah untuk antarmuka web",
                    "Merancang frontend modern menggunakan React 18, Vite, TypeScript, dan Zustand terintegrasi koneksi streaming WebSockets real-time",
                    "[Repository Link](https://github.com/KarmaSenzu/golang-rekam)"
                ]
            },
            {
                "name": "AturJajan — Mobile Expense Tracker & Cloud Financial REST API",
                "start": "2024-03",
                "end": "2024-06",
                "highlights": [
                    "Aplikasi pencatat keuangan pribadi yang berfungsi memvisualisasikan grafik pengeluaran dan mengontrol anggaran harian pengguna",
                    "Mengembangkan aplikasi mobile cross-platform via React Native/Expo serta backend Express.js, PostgreSQL, dan autentikasi token JWT aman",
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
        "summary": "Fullstack Developer dengan rekam jejak pembangunan sistem web end-to-end yang solid. Terbiasa memadukan antarmuka interaktif responsif (React.js/Next.js) dengan arsitektur backend terstruktur (Laravel PHP & Node.js/Go) serta perancangan database relasional.",
        "skills_core": "React.js, Next.js, Laravel (PHP), Node.js, RESTful API, PostgreSQL, MySQL, Git",
        "skills_lang": "JavaScript, TypeScript, PHP, Go (Golang), SQL, HTML5, CSS3, Tailwind CSS",
        "skills_infra": "MySQL, PostgreSQL, Docker, Docker Compose, Linux VPS, Nginx, Agile Development",
        "projects": [
            {
                "name": "Laravel Travel — Online Travel Reservation & Booking Web System",
                "start": "2024-01",
                "end": "2024-03",
                "highlights": [
                    "Membangun portal reservasi tiket perjalanan yang berfungsi mendigitalkan alur pembelian tiket penumpang dan pemilihan jadwal rute secara interaktif",
                    "Menerapkan pola MVC pada Laravel, engine templating Blade, validasi form, dan perancangan database relasional MySQL yang terstruktur",
                    "[Repository Link](https://github.com/KarmaSenzu/Laravel-Travel)"
                ]
            },
            {
                "name": "Dmrxai — Multi-Model AI Assistant & Document Intelligence Platform",
                "start": "2024-05",
                "end": "2024-09",
                "highlights": [
                    "Platform aplikasi web interaktif mandiri yang berfungsi membedah dokumen PDF/teks teknis berukuran besar dan visualisasi data secara instan",
                    "Diarsitekturi dengan Next.js 14, TypeScript, dan Tailwind CSS serta diorkestrasi dalam kontainer terisolasi via Docker Compose",
                    "[Repository Link](https://github.com/KarmaSenzu/Dmrxai)"
                ]
            },
            {
                "name": "Golang-Finance — Personal Finance RESTful API & Clean Architecture",
                "start": "2024-02",
                "end": "2024-04",
                "highlights": [
                    "Merancang backend REST API modular dengan Clean Architecture (handler -> service -> repository) untuk pencatatan transaksi keuangan aman",
                    "Menerapkan autentikasi JWT, transaksi database relasional ACID pada MySQL/PostgreSQL, serta kesiapan deployment Docker",
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
        "summary": "Junior Data & Backend Engineer lulusan S.Kom Cum Laude (IPK 3.85) dengan sertifikasi BNSP. Menguasai scripting Python, perancangan pipeline data otomatis (ETL), pemodelan database relasional SQL (PostgreSQL), serta pengawasan utilisasi server Linux.",
        "skills_core": "Python, SQL, PostgreSQL, MySQL, Data Pipeline (ETL), Cron Automation, Git, Linux VPS",
        "skills_lang": "Python, SQL, Go (Golang), Shell/Bash Scripting, JavaScript",
        "skills_infra": "PostgreSQL, MySQL, Timeseries Data, Docker, Linux Server, Git, REST API Integration",
        "projects": [
            {
                "name": "HERMES-PT.-ASISTEN-DMR — Multi-Source Autonomous AI Data Pipeline",
                "start": "2024-07",
                "end": "2024-09",
                "highlights": [
                    "Mengembangkan sistem pipeline pengumpulan data otomatis yang berfungsi memindai, menyaring, dan merangkum riset AI dari arXiv, HuggingFace, & GitHub",
                    "Menerapkan parsing data terstruktur, transformasi JSON, deduplikasi berita, dan otomasi distribusi terjadwal via Linux Cron ke Telegram",
                    "[Repository Link](https://github.com/KarmaSenzu/HERMES-PT.-ASISTEN-DMR)"
                ]
            },
            {
                "name": "Auto-Subtitle-AI — Automated Speech-to-Text & Data Processing Pipeline",
                "start": "2024-04",
                "end": "2024-06",
                "highlights": [
                    "Merancang pipeline pemrosesan audio-ke-teks otomatis yang berfungsi mentranskripsikan dialog video menggunakan model deep learning Faster-Whisper",
                    "Menyusun sinkronisasi timestamp berkas takarir format ASS dan mengotomatisasi rendering hardsub via pipeline FFmpeg di backend FastAPI Python",
                    "[Local Directory Portfolio: Auto Subtitle Editing]"
                ]
            },
            {
                "name": "Golang-Finance — Relational Database Schema & Data Integrity Engine",
                "start": "2024-02",
                "end": "2024-04",
                "highlights": [
                    "Merancang skema relasional, optimasi query transaksi keuangan, dan memastikan kepatuhan ACID guna menjaga konsistensi data finansial",
                    "Menerapkan filtering, pagination berkinerja tinggi, dan penanganan relasi database relasional PostgreSQL & MySQL",
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
        "summary": "Tenaga IT Support profesional lulusan Sarjana Komputer (S.Kom. Cum Laude, IPK 3.85) dengan sertifikasi BNSP. Berpengalaman menangani perakitan dan troubleshooting PC/laptop, penarikan dan konfigurasi jaringan LAN/WiFi kantor, administrasi OS Windows & Linux, serta pemeliharaan infrastruktur operasional.",
        "skills_core": "Hardware Troubleshooting, LAN/WLAN Networking, Windows & Linux OS, IT Helpdesk, Perawatan Periferal",
        "skills_lang": "Shell Scripting, Command Line, PowerShell, Windows Desktop/Server, Ubuntu Linux",
        "skills_infra": "TCP/IP, DNS, DHCP, WiFi Router Setup, Remote Desktop (AnyDesk/RDP), PC Assembly, Backup Data",
        "projects": [
            {
                "name": "ServerMonitoring — Infrastructure & Host Monitoring Command Center",
                "start": "2024-06",
                "end": "2024-10",
                "highlights": [
                    "Command center sentral yang berfungsi memantau utilisasi CPU, memori, disk, dan konektivitas jaringan multi-server secara real-time",
                    "Mengotomatisasi diagnosa kesehatan sistem operasi, eksekusi perintah perbaikan darurat via SSH, dan alerting instan lonjakan beban",
                    "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"
                ]
            },
            {
                "name": "Linux & Windows Infrastructure Administration & Office Networking",
                "start": "2023-01",
                "end": "present",
                "highlights": [
                    "Mengonfigurasi server Linux VPS, routing firewall, setup reverse proxy Nginx, dan manajemen akun pengguna jaringan kantor",
                    "Melakukan troubleshooting konektivitas jaringan LAN/WLAN, penanganan error driver periferal, dan pemeliharaan sistem berkala",
                    "[Infrastructure Portfolio: Self-Hosted Server & VPS]"
                ]
            },
            {
                "name": "Hardware Diagnostic, PC Assembly, & Workstation Deployment",
                "start": "2022-01",
                "end": "present",
                "highlights": [
                    "Berpengalaman dalam perakitan PC dari nol, instalasi sistem operasi Windows & Linux, konfigurasi printer sharing, dan diagnosa komponen fisik",
                    "Memberikan dukungan teknis cepat (end-user support) untuk mengatasi kendala software maupun koneksi jaringan pengguna",
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
                "name": "Program-Aplikasi-Kasir-Java — Desktop Point of Sale (POS) & Inventory System",
                "start": "2023-10",
                "end": "2024-01",
                "highlights": [
                    "Aplikasi kasir desktop yang berfungsi mempercepat transaksi pembayaran, mengkalkulasi nota belanja, dan memotong stok barang retail otomatis",
                    "Merancang integrasi database relasional MySQL, pencetakan bukti bayar nota kasir, dan troubleshooting data transaksi merchant",
                    "[Repository Link](https://github.com/KarmaSenzu/Program-Aplikasi-Kasir-Java)"
                ]
            },
            {
                "name": "Mentari-Smart-Warehouse — Smart Inventory & Stock Form Control",
                "start": "2025-06",
                "end": "2025-11",
                "highlights": [
                    "Modul manajemen inventaris pergudangan enterprise yang berfungsi mencegah kesalahan input stok barang oleh operator melalui validasi real-time",
                    "Mengembangkan pengkategorian barang dinamis dan penomoran kode SKU otomatis guna memastikan keakuratan data stok dagangan retail",
                    "[Local Directory Portfolio: Mentari Solusi Indonesia]"
                ]
            },
            {
                "name": "ServerMonitoring — Infrastructure & Terminal Uptime Monitor",
                "start": "2024-06",
                "end": "2024-10",
                "highlights": [
                    "Platform monitoring yang berfungsi memantau ketersediaan jaringan terminal transaksi kasir dan infrastruktur server secara konsisten",
                    "Mengirimkan notifikasi peringatan instan saat terjadi pemutusan koneksi jaringan atau lonjakan utilisasi perangkat",
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
        "summary": "Teknisi IT Support berorientasi solusi dengan keahlian troubleshooting perangkat keras PC/Laptop, penarikan & konfigurasi kabel jaringan LAN/WAN, instalasi software berlisensi, serta layanan bantuan teknis (helpdesk ticketing) yang komunikatif dan sigap.",
        "skills_core": "Technical Support, Hardware Maintenance, Network Cabling & Configuration, Windows & Linux, Helpdesk",
        "skills_lang": "Command Prompt/PowerShell, Linux Shell, TCP/IP Utilities (ping, traceroute, netstat)",
        "skills_infra": "Crimping RJ45, LAN Cabling, Switch, Router WiFi, Printer Sharing, Remote Desktop, Antivirus Deployment",
        "projects": [
            {
                "name": "ServerMonitoring — Network Incident Alerting & Host Health Platform",
                "start": "2024-06",
                "end": "2024-10",
                "highlights": [
                    "Platform pemantauan jaringan sentral yang berfungsi mendeteksi gangguan konektivitas dan memantau status kesehatan host kerja",
                    "Mengotomatisasi diagnosa respon latensi jaringan (ping), utilisasi memori, serta peringatan dini insiden teknis sebelum mengganggu pengguna",
                    "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"
                ]
            },
            {
                "name": "Workstation & Network Deployment Operations",
                "start": "2023-01",
                "end": "present",
                "highlights": [
                    "Menangani instalasi sistem operasi Windows/Linux, konfigurasi IP Static/DHCP kantor, printer sharing, dan deployment antivirus berlisensi",
                    "Melakukan crimping kabel UTP RJ45, pengujian konektivitas port LAN/WLAN, serta penanganan insiden hardware pengguna akhir",
                    "[Technical Support Operations]"
                ]
            },
            {
                "name": "Program-Aplikasi-Kasir-Java — Client-Server Database Setup",
                "start": "2023-10",
                "end": "2024-01",
                "highlights": [
                    "Melakukan konfigurasi koneksi jaringan client-server antara workstation kerja pengguna dengan server database lokal",
                    "Menangani perizinan port database, instalasi Java Runtime Environment (JRE), dan konfigurasi driver periferal pendukung",
                    "[Repository Link](https://github.com/KarmaSenzu/Program-Aplikasi-Kasir-Java)"
                ]
            }
        ]
    }
]

print(f"Mulai kompilasi CV dengan deskripsi fungsional lengkap untuk {len(detailed_jobs)} lowongan aktif...")

for item in detailed_jobs:
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
          - Merancang modul formulir barang dinamis, penomoran kode stok otomatis, dan validasi data transaksi real-time
          - Mengonfigurasi deployment containerized pada Linux VPS dan reverse proxy Nginx untuk keandalan akses server

      - company: Freelance IT
        position: Software & Technical Specialist
        start_date: 2022-01
        end_date: present
        location: Jakarta Selatan, Indonesia
        highlights:
          - Mengembangkan aplikasi web, sistem kasir/POS desktop, dan RESTful API terstruktur untuk kebutuhan bisnis klien
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
        print(f"  ✓ PDF berhasil di-render dengan penjelasan fungsional: {pdf_filename}")
    else:
        print(f"  ✗ Render error pada {item['id']}: {res.stderr[:200]}")

print("✓ Selesai mengompilasi CV dengan fungsi nyata proyek!")
