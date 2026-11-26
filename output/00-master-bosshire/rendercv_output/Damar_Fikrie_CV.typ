// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.3.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Damar Fikrie",
  title: "Damar Fikrie - CV",
  footer: context { [#emph[Damar Fikrie -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Terakhir diperbarui Nov 2026] ],
  locale-catalog-language: "id",
  text-direction: ltr,
  page-size: "a4",
  page-top-margin: 1.15cm,
  page-bottom-margin: 1.15cm,
  page-left-margin: 1.2cm,
  page-right-margin: 1.2cm,
  page-show-footer: true,
  page-show-top-note: true,
  colors-body: rgb(0, 0, 0),
  colors-name: rgb(0, 79, 144),
  colors-headline: rgb(0, 79, 144),
  colors-connections: rgb(0, 79, 144),
  colors-section-titles: rgb(0, 79, 144),
  colors-links: rgb(0, 79, 144),
  colors-footer: rgb(128, 128, 128),
  colors-top-note: rgb(128, 128, 128),
  typography-line-spacing: 0.6em,
  typography-alignment: "justified",
  typography-date-and-location-column-alignment: right,
  typography-font-family-body: "Source Sans 3",
  typography-font-family-name: "Source Sans 3",
  typography-font-family-headline: "Source Sans 3",
  typography-font-family-connections: "Source Sans 3",
  typography-font-family-section-titles: "Source Sans 3",
  typography-font-size-body: 9.5pt,
  typography-font-size-name: 30pt,
  typography-font-size-headline: 10pt,
  typography-font-size-connections: 10pt,
  typography-font-size-section-titles: 1.4em,
  typography-small-caps-name: false,
  typography-small-caps-headline: false,
  typography-small-caps-connections: false,
  typography-small-caps-section-titles: false,
  typography-bold-name: true,
  typography-bold-headline: false,
  typography-bold-connections: false,
  typography-bold-section-titles: true,
  links-underline: false,
  links-show-external-link-icon: false,
  header-alignment: center,
  header-photo-width: 3.5cm,
  header-space-below-name: 0.7cm,
  header-space-below-headline: 0.7cm,
  header-space-below-connections: 0.7cm,
  header-connections-hyperlink: true,
  header-connections-show-icons: true,
  header-connections-display-urls-instead-of-usernames: false,
  header-connections-separator: "",
  header-connections-space-between-connections: 0.5cm,
  section-titles-type: "with_partial_line",
  section-titles-line-thickness: 0.5pt,
  section-titles-space-above: 0.35cm,
  section-titles-space-below: 0.18cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.3em,
  sections-space-between-regular-entries: 0.85em,
  entries-date-and-location-width: 4.15cm,
  entries-side-space: 0.2cm,
  entries-space-between-columns: 0.1cm,
  entries-allow-page-break: false,
  entries-short-second-row: true,
  entries-degree-width: 1cm,
  entries-summary-space-left: 0cm,
  entries-summary-space-above: 0cm,
  entries-highlights-bullet:  "•" ,
  entries-highlights-nested-bullet:  "•" ,
  entries-highlights-space-left: 0.15cm,
  entries-highlights-space-above: 0cm,
  entries-highlights-space-between-items: 0cm,
  entries-highlights-space-between-bullet-and-text: 0.5em,
  date: datetime(
    year: 2026,
    month: 11,
    day: 26,
  ),
)


= Damar Fikrie

  #headline([Full Stack & Backend Developer])

#connections(
  [#connection-with-icon("location-dot")[Jakarta Selatan, Indonesia]],
  [#link("mailto:damarfikrie@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[damarfikrie\@gmail.com]]],
  [#link("tel:+62-851-5648-7577", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[0851-5648-7577]]],
  [#link("https://profildmr.devplay.online/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[profildmr.devplay.online]]],
  [#link("https://github.com/KarmaSenzu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[KarmaSenzu]]],
  [#link("https://linkedin.com/in/damar-fikrie", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[damar-fikrie]]],
)


== Summary

Full Stack & Backend Developer lulusan Sarjana Komputer (S.Kom., IPK 3.85 \/ 4.00, Universitas Bina Sarana Informatika) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Berpengalaman merancang dan mengembangkan sistem web berorientasi solusi, platform kecerdasan buatan (AI), aplikasi manajemen inventaris bisnis, dan layanan backend API transaksi keuangan berkinerja tinggi. Terbiasa memadukan keandalan arsitektur backend Go (Golang) & Node.js dengan antarmuka modern React.js\/Next.js, integritas basis data relasional (PostgreSQL & MySQL), serta otomatisasi deployment server Linux VPS dan Docker.

== Experience

#regular-entry(
  [
    #strong[Mentari Solusi Indonesia], Full Stack Developer

    - Mengembangkan sistem manajemen operasional bisnis berbasis web untuk mempermudah pencatatan inventaris dan arus keluar-masuk barang

    - Membangun antarmuka formulir inventaris pintar dengan kategorisasi dinamis, penomoran kode otomatis, dan validasi data real-time

    - Mengintegrasikan layanan backend RESTful API dengan database relasional terpusat serta deployment server Linux VPS dan Docker

  ],
  [
    Jakarta, Indonesia

    Jun 2025 – Nov 2025

    

    6 bulan

  ],
)

#regular-entry(
  [
    #strong[Freelance IT], IT Web Developer & Freelance Engineer

    - Merancang dan membangun aplikasi web production-ready untuk membantu digitalisasi operasional bisnis klien

    - Mengembangkan sistem inventaris stok multi-item, kasir (POS), dan pencatatan transaksi pengguna dengan alur kerja terstruktur

    - Mengelola infrastruktur server Linux VPS (Ubuntu), konfigurasi reverse proxy Nginx, dan kontainerisasi Docker untuk menjamin uptime aplikasi

    - Melakukan pemeliharaan rutin, monitoring kesehatan server, optimasi kueri database, serta troubleshooting teknis sistem secara menyeluruh

  ],
  [
    Jakarta Selatan, Indonesia

    Jan 2022 – sekarang

    

    5 tahun

  ],
)

== Featured Projects

#regular-entry(
  [
    #strong[Hermes-Desktop-Pet — Autonomous LLM Desktop AI Companion]

    - Merancang arsitektur Decoupled Brain-Actor untuk asisten AI otonom lintas platform (Windows, macOS, Linux) pada overlay desktop transparan always-on-top

    - Menghubungkan Hermes Agent (LLM Brain, tool execution, long-term memory) via WebSocket JSON-RPC 2.0 dengan dukungan multi-provider LLM (OAuth & 9Router) serta monitor kuota & latensi real-time

    - Mengintegrasikan rendering karakter Live2D (PixiJS) & 3D WebGL (Three.js VRM\/GLB\/PMX\/FBX), sintesis suara lokal Kokoro-ONNX TTS & Whisper STT, Screen Vision Snipping, serta Auto-Tiling Window Manager

    - Mengimplementasikan enkripsi kredensial Electron safeStorage, 124 unit test (20 suites Vitest), dan rilis CI\/CD lintas OS via GitHub Actions

    - Tech Stack: Electron 45, Node.js (ESM), JavaScript, PixiJS, Live2D, Three.js, WebSocket JSON-RPC, Kokoro-ONNX, Whisper STT, Vitest | #link("https://github.com/KarmaSenzu/Hermes-Desktop-Pet")[GitHub Repository]

  ],
  [
    Jan 2025 – sekarang

  ],
)

#regular-entry(
  [
    #strong[Golang-Rekam — Real-Time Streaming & Recording Management System]

    - Mengembangkan sistem backend untuk menangani komunikasi data real-time dan pengelolaan aliran streaming kamera melalui koneksi WebSocket

    - Membangun dashboard monitoring interaktif untuk memantau status perangkat kamera dan aktivitas streaming secara langsung

    - Mengimplementasikan autentikasi pengguna yang aman, pengelolaan multi-koneksi, dan fitur pemutaran ulang arsip rekaman video

    - Tech Stack: Go (Golang), Gin, WebSocket, PostgreSQL, React 18, TypeScript, Tailwind CSS | #link("https://github.com/KarmaSenzu/Golang-Rekam")[GitHub Repository]

  ],
  [
    Sep 2024 – Nov 2024

  ],
)

#regular-entry(
  [
    #strong[Golang-Finance — Financial Transaction Management API]

    - Mengembangkan backend API untuk mendukung pencatatan, validasi, dan pemrosesan transaksi keuangan secara terstruktur

    - Membangun mekanisme penyimpanan transaksi dengan konsistensi data tinggi untuk menjaga keakuratan setiap perubahan saldo dan mutasi

    - Mengimplementasikan autentikasi pengguna (JWT), pengujian unit terotomatisasi, serta pemisahan logika bisnis yang mudah dipelihara

    - Tech Stack: Go (Golang), Clean Architecture, PostgreSQL 16, JWT, RESTful API, Docker | #link("https://github.com/KarmaSenzu/Golang-Finance")[GitHub Repository]

  ],
  [
    Feb 2024 – Apr 2024

  ],
)

#regular-entry(
  [
    #strong[Dmrxai — Multi-Model AI Chat & Interactive Web Platform]

    - Membangun platform aplikasi web terpadu yang memungkinkan pengguna berinteraksi dengan berbagai model kecerdasan buatan dalam satu antarmuka

    - Mengembangkan integrasi komunikasi antara antarmuka pengguna dan backend API untuk menangani pemrosesan data secara asinkron

    - Mengimplementasikan manajemen status aplikasi yang responsif dan isolasi lingkungan deployment menggunakan Docker Compose

    - Tech Stack: Next.js 14, React, TypeScript, Tailwind CSS, RESTful API, Docker Compose | #link("https://github.com/KarmaSenzu/Dmrxai")[GitHub Repository]

  ],
  [
    Mei 2024 – Agu 2024

  ],
)

#regular-entry(
  [
    #strong[Mentari-Smart-Warehouse — Inventory & Warehouse Management System]

    - Mengembangkan sistem manajemen inventaris berbasis web untuk membantu pengelolaan data barang dan aktivitas operasional gudang

    - Membangun fitur pencatatan barang dengan penomoran kode otomatis, pengelompokan kategori dinamis, dan validasi data untuk meminimalkan human error

    - Mengintegrasikan antarmuka aplikasi dengan layanan backend API dan database relasional untuk pelaporan stok barang secara terpusat

    - Tech Stack: React, TypeScript, PHP, MySQL, RESTful API, Linux VPS, Nginx Reverse Proxy

  ],
  [
    Jun 2025 – Nov 2025

  ],
)

#regular-entry(
  [
    #strong[ServerMonitoring — Multi-Server Infrastructure Monitoring Platform]

    - Mengembangkan dashboard terpusat untuk memantau kondisi kesehatan, penggunaan sumber daya, dan aktivitas beberapa server Linux secara real-time

    - Mengimplementasikan pengelolaan server jarak jauh melalui koneksi SSH aman, pemantauan status proses layanan, dan manajemen kontainer Docker

    - Membangun fitur penjelajah file server, inspeksi log sistem, serta pencatatan audit aktivitas pemeliharaan infrastruktur

    - Tech Stack: Go (Golang), React, Linux VPS, Docker, SSH, Nginx | #link("https://github.com/KarmaSenzu/ServerMonitoring")[GitHub Repository]

  ],
  [
    Sep 2024 – Okt 2024

  ],
)

#regular-entry(
  [
    #strong[Auto-Subtitle-AI — AI-Powered Video Transcription & Subtitle Generator]

    - Mengembangkan aplikasi pemrosesan video otomatis yang mengubah percakapan audio menjadi teks subtitle menggunakan model speech-to-text AI

    - Mengimplementasikan pipeline otomatis untuk ekstraksi audio, transkripsi suara akurasi tinggi, dan sinkronisasi teks subtitle dengan durasi video

    - Menyediakan fitur ekspor subtitle format standar industri (ASS\/SRT) serta kemampuan pembakaran teks langsung ke dalam video secara otomatis

    - Tech Stack: Python, FastAPI, Faster-Whisper, FFmpeg, Docker Container

  ],
  [
    Agu 2024 – Sep 2024

  ],
)

== Technical Skills

#strong[Core Competencies:] Full Stack Web Development, Backend RESTful API, Microservices Architecture, Relational Database Design, Clean Architecture, Server Administration

#strong[Programming Languages:] Go (Golang), TypeScript, JavaScript, Python, PHP, Java, SQL, Linux Shell, HTML5, CSS3

#strong[Frameworks & Libraries:] React.js, Next.js, Node.js, Express.js, FastAPI, Gin, Laravel, CodeIgniter 4, Vite, Zustand, Tailwind CSS, Electron

#strong[Databases & Cloud Infra:] PostgreSQL, MySQL, Redis, Linux VPS (Ubuntu), Docker, Docker Compose, Nginx Reverse Proxy, PM2, Cloudflare Tunnel, Git, GitHub

#strong[Systems & DevOps:] CI\/CD Pipeline, WebSockets Streaming, System Observability, Unit Testing, API Security (JWT, bcrypt), Nginx Configuration, Linux System Admin

== Education

#education-entry(
  [
    #strong[Universitas Bina Sarana Informatika]

    #emph[Sarjana Komputer (S.Kom. \/ S1) — Fresh Graduate (Lulus) — Teknik Informatika]

    - IPK: 3.85 \/ 4.00

    - Fokus: Rekayasa Perangkat Lunak, Arsitektur Backend, Sistem Database, dan Jaringan Komputer

  ],
  [
    Jakarta Selatan, Indonesia

    Agu 2022 – Okt 2026

  ],
)

#education-entry(
  [
    #strong[SMK Wisata Indonesia]

    #emph[SMK \/ Sekolah Menengah Kejuruan — Teknik Komputer dan Jaringan (TKJ)]

  ],
  [
    Jakarta Selatan, Indonesia

    Jul 2019 – Jun 2022

  ],
)

== Certifications

#regular-entry(
  [
    #strong[Sertifikat Kompetensi Pengembang Perangkat Lunak (Kualifikasi Analis Program \/ Program Analyst)]

    - Badan Nasional Sertifikasi Profesi (BNSP) & Lembaga Sertifikasi Profesi (LSP UBSI)

  ],
  [
    Sep 2025 – Sep 2028

  ],
)

#regular-entry(
  [
    #strong[PCAP — Programming Essentials in Python]

    - Python Institute (OpenEDG) & Cisco Networking Academy

  ],
  [
    Jan 2024

  ],
)

#regular-entry(
  [
    #strong[Belajar Dasar Pemrograman Web]

    - Dicoding Indonesia (41 Jam Pembelajaran)

  ],
  [
    Des 2024 – Des 2027

  ],
)

#regular-entry(
  [
    #strong[Fundamental Cyber Security]

    - Coding Studio

  ],
  [
    Jul 2024

  ],
)

== Leadership and Activities

#regular-entry(
  [
    #strong[Pemateri Seminar WIB: Pengenalan Website Sederhana untuk Siswa SMA]

    - Himpunan Mahasiswa Informatika (HIMAIF UBSI) — Lokasi: SMA Taman Madya 1 Jakarta

  ],
  [
    Agu 2024

  ],
)

#regular-entry(
  [
    #strong[Sie. Sosial Kemasyarakatan — Himpunan Mahasiswa Informatika UBSI]

    - Penerima Piagam Penghargaan Kontribusi Kepengurusan Resmi dari Rektorat Universitas Bina Sarana Informatika

  ],
  [
    Jan 2024 – Des 2024

  ],
)
