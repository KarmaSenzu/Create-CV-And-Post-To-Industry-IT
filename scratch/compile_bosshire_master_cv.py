#!/usr/bin/env python3
"""
Generate Complete Master CV for BossHire & Render PDF
"""

import os
import subprocess
import shutil

WORKSPACE = "/Users/damarfikrie/Desktop/Create CV And Post To Industry IT"
RENDERCV = os.path.join(WORKSPACE, ".venv", "bin", "rendercv")
TARGET_DIR = os.path.join(WORKSPACE, "output", "00-master-bosshire")
os.makedirs(TARGET_DIR, exist_ok=True)

yaml_content = """# yaml-language-server: $schema=https://raw.githubusercontent.com/rendercv/rendercv/refs/tags/v2.8/schema.json
cv:
  name: Damar Fikrie
  headline: "Full Stack & Backend Developer"
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
      - "Full Stack & Backend Developer lulusan Sarjana Komputer (S.Kom. Cum Laude, IPK 3.85 / 4.00, Universitas Bina Sarana Informatika) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Berpengalaman membangun aplikasi web scalable dan backend API berkecepatan tinggi menggunakan Go (Golang), TypeScript, React.js, Next.js, Node.js, dan PHP. Menguasai arsitektur Clean Architecture, sistem perpesanan streaming WebSockets, manajemen basis data relasional terstruktur (PostgreSQL & MySQL), serta deployment server Linux VPS dan kontainerisasi Docker."

    experience:
      - company: Mentari Solusi Indonesia
        position: Full Stack Developer
        start_date: 2025-06
        end_date: 2025-11
        location: Jakarta, Indonesia
        highlights:
          - "Mengembangkan aplikasi web full stack dan arsitektur REST API menggunakan React.js, TypeScript, PHP, dan database MySQL"
          - "Membangun sistem inventaris pintar (Smart Product Form) dengan kategorisasi dinamis, penomoran kode barang otomatis, dan validasi data real-time"
          - "Mengonfigurasi deployment aplikasi pada server produksi Linux VPS menggunakan kontainer Docker dan reverse proxy Nginx"

      - company: Freelance IT
        position: IT Web Developer & Freelance Engineer
        start_date: 2022-01
        end_date: present
        location: Jakarta Selatan, Indonesia
        highlights:
          - "Merancang dan membangun aplikasi web production-ready, integrasi backend API asinkron, serta manajemen database relasional"
          - "Mengelola server Linux VPS (Ubuntu), setup reverse proxy Nginx, manajemen proses PM2, kontainerisasi Docker, dan Cloudflare Tunnel"
          - "Membangun sistem operasional bisnis terintegrasi meliputi inventaris stok multi-item, kasir (POS), dan pencatatan transaksi pengguna"
          - "Melakukan pemeliharaan sistem, monitoring kesehatan server Linux, optimasi kueri database, serta troubleshooting teknis end-to-end"

    featured_projects:
      - name: "Golang-Rekam — High-Throughput Streaming WebSocket & Audio Engine"
        start_date: 2024-09
        end_date: 2024-11
        highlights:
          - "Merancang backend streaming event-driven berkecepatan tinggi berbasis Go Gin, gorilla/websocket, dan database PostgreSQL 16"
          - "Membangun antarmuka dashboard monitoring interaktif modern berbasis React 18, Vite, TypeScript, Tailwind CSS, dan Zustand"
          - "Mengimplementasikan in-memory channel hub, autentikasi aman JWT + bcrypt, dan pemutar ulang rekaman video interaktif"
          - "[Repository Link](https://github.com/KarmaSenzu/Golang-Rekam)"

      - name: "Golang-Finance — RESTful API Transaksi Finansial Clean Architecture"
        start_date: 2024-02
        end_date: 2024-04
        highlights:
          - "Merancang arsitektur backend transaksi finansial menerapkan Clean Architecture (Handler -> Service -> Repository) dengan Go"
          - "Mengintegrasikan database relasional PostgreSQL 16 dengan penjaminan kepatuhan konsistensi data transaksional ACID"
          - "Menerapkan pengujian unit terotomatisasi, autentikasi aman JWT, serta penulisan clean code berstandar industri"
          - "[Repository Link](https://github.com/KarmaSenzu/Golang-Finance)"

      - name: "Dmrxai — Multi-Model AI Web Platform & Interactive Interface"
        start_date: 2024-05
        end_date: 2024-08
        highlights:
          - "Membangun antarmuka web interaktif modern berbasis React, Next.js 14, TypeScript, dan Tailwind CSS"
          - "Mengintegrasikan state management responsif dengan backend RESTful API, pemrosesan data asinkron, dan Docker Compose"
          - "[Repository Link](https://github.com/KarmaSenzu/Dmrxai)"

      - name: "Mentari-Smart-Warehouse — Sistem Inventaris Bisnis & Manajemen Gudang"
        start_date: 2025-06
        end_date: 2025-11
        highlights:
          - "Mengembangkan modul Smart Product Form dan manajemen inventaris gudang berbasis React 18, TypeScript, dan database MySQL"
          - "Mengimplementasikan fitur penomoran kode barang otomatis, kategorisasi dinamis, serta validasi data transaksional real-time"
          - "Mengonfigurasi deployment server produksi Linux VPS dengan reverse proxy Nginx dan integrasi RESTful API teruji"

      - name: "ServerMonitoring — Multi-Host Linux VPS Telemetry & Observability Hub"
        start_date: 2024-09
        end_date: 2024-10
        highlights:
          - "Membangun command center observabilitas multi-host Linux VPS, telemetri real-time, eksekusi SSH, dan manajemen proses Nginx"
          - "Mengonfigurasi deployment otomatis kontainer Docker, file manager server, event audit, dan inspeksi kesehatan infrastruktur"
          - "[Repository Link](https://github.com/KarmaSenzu/ServerMonitoring)"

      - name: "Auto-Subtitle-AI — Asynchronous Multimedia Processing & Speech-to-Text"
        start_date: 2024-08
        end_date: 2024-09
        highlights:
          - "Merancang backend pemrosesan video dan speech-to-text otomatis menggunakan Python, FastAPI, Faster-Whisper, dan FFmpeg"
          - "Mengimplementasikan integrasi model AI transkripsi presisi tinggi, generator subtitle format ASS, dan pipeline automasi video"

    technical_skills:
      - label: Core Competencies
        details: "Full Stack Web Development, Backend RESTful API, Microservices Architecture, Relational Database Design, Clean Architecture, Server Administration"
      - label: Programming Languages
        details: "Go (Golang), TypeScript, JavaScript, Python, PHP, Java, SQL, Linux Shell, HTML5, CSS3"
      - label: Frameworks & Libraries
        details: "React.js, Next.js, Node.js, Express.js, FastAPI, Gin, Laravel, CodeIgniter 4, Vite, Zustand, Tailwind CSS, Electron"
      - label: Databases & Cloud Infra
        details: "PostgreSQL, MySQL, Redis, Linux VPS (Ubuntu), Docker, Docker Compose, Nginx Reverse Proxy, PM2, Cloudflare Tunnel, Git, GitHub"
      - label: Systems & DevOps
        details: "CI/CD Pipeline, WebSockets Streaming, System Observability, Unit Testing, API Security (JWT, bcrypt), Nginx Configuration, Linux System Admin"

    education:
      - institution: Universitas Bina Sarana Informatika
        area: Teknik Informatika
        degree: Sarjana Komputer (S.Kom. / S1) — Fresh Graduate (Lulus)
        start_date: 2022-08
        end_date: 2026-10
        location: Jakarta Selatan, Indonesia
        highlights:
          - "IPK: 3.85 / 4.00 (Cum Laude)"
          - "Fokus: Rekayasa Perangkat Lunak, Arsitektur Backend, Sistem Database, dan Jaringan Komputer"
      - institution: SMK Wisata Indonesia
        area: Teknik Komputer dan Jaringan (TKJ)
        degree: SMK / Sekolah Menengah Kejuruan
        start_date: 2019-07
        end_date: 2022-06
        location: Jakarta Selatan, Indonesia

    certifications:
      - name: "Sertifikat Kompetensi Pengembang Perangkat Lunak (Kualifikasi Analis Program / Program Analyst)"
        start_date: 2025-09
        end_date: 2028-09
        highlights:
          - "Badan Nasional Sertifikasi Profesi (BNSP) & Lembaga Sertifikasi Profesi (LSP UBSI)"
      - name: "PCAP — Programming Essentials in Python"
        date: 2024-01
        highlights:
          - "Python Institute (OpenEDG) & Cisco Networking Academy"
      - name: "Belajar Dasar Pemrograman Web"
        start_date: 2024-12
        end_date: 2027-12
        highlights:
          - "Dicoding Indonesia (41 Jam Pembelajaran)"
      - name: "Fundamental Cyber Security"
        date: 2024-07
        highlights:
          - "Coding Studio"

    leadership_and_activities:
      - name: "Pemateri Seminar WIB: Pengenalan Website Sederhana untuk Siswa SMA"
        date: 2024-08
        highlights:
          - "Himpunan Mahasiswa Informatika (HIMAIF UBSI) — Lokasi: SMA Taman Madya 1 Jakarta"
      - name: "Sie. Sosial Kemasyarakatan — Himpunan Mahasiswa Informatika UBSI"
        start_date: 2024-01
        end_date: 2024-12
        highlights:
          - "Penerima Piagam Penghargaan Kontribusi Kepengurusan Resmi dari Rektorat Universitas Bina Sarana Informatika"

design:
  theme: classic
  page:
    size: a4
    top_margin: 1.4cm
    bottom_margin: 1.4cm
    left_margin: 1.4cm
    right_margin: 1.4cm
  templates:
    education_entry:
      degree_column: null
      main_column: |-
        **INSTITUTION**
        *DEGREE — AREA*
        HIGHLIGHTS

locale:
  language: indonesian

settings:
  render_command:
    output_folder: rendercv_output
    pdf_path: rendercv_output/Damar_Fikrie_CV_Lengkap_BossHire.pdf
"""

cv_yaml_path = os.path.join(TARGET_DIR, "cv.yaml")
with open(cv_yaml_path, "w", encoding="utf-8") as f:
    f.write(yaml_content)

print(f"Written: {cv_yaml_path}")
print("Rendering PDF via RenderCV...")
res = subprocess.run([RENDERCV, "render", "cv.yaml"], cwd=TARGET_DIR, capture_output=True, text=True)
if res.returncode != 0:
    print("RenderCV Error:", res.stderr)
else:
    print("RenderCV Success!")
    rendered_pdf = os.path.join(TARGET_DIR, "rendercv_output", "Damar_Fikrie_CV_Lengkap_BossHire.pdf")
    final_pdf = os.path.join(TARGET_DIR, "Damar_Fikrie_CV_Lengkap_BossHire.pdf")
    if os.path.exists(rendered_pdf):
        shutil.copy2(rendered_pdf, final_pdf)
        print(f"Copied final PDF to: {final_pdf}")
        
        # Also copy to profiles/damar-fikrie/
        profile_dest = os.path.join(WORKSPACE, "profiles", "damar-fikrie", "Damar_Fikrie_CV_Lengkap_BossHire.pdf")
        shutil.copy2(rendered_pdf, profile_dest)
        print(f"Copied to profile: {profile_dest}")

