// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.3.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Damar Fikrie",
  title: "Damar Fikrie - CV",
  footer: context { [#emph[Damar Fikrie -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Last updated in Nov 2026] ],
  locale-catalog-language: "en",
  text-direction: ltr,
  page-size: "a4",
  page-top-margin: 1.5cm,
  page-bottom-margin: 1.5cm,
  page-left-margin: 1.5cm,
  page-right-margin: 1.5cm,
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
  typography-font-size-body: 10pt,
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
  section-titles-space-above: 0.5cm,
  section-titles-space-below: 0.3cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.3em,
  sections-space-between-regular-entries: 1.2em,
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
    day: 11,
  ),
)


= Damar Fikrie

  #headline([Junior Data Engineer])

#connections(
  [#connection-with-icon("location-dot")[Jakarta Selatan, Indonesia]],
  [#link("mailto:damarfikrie@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[damarfikrie\@gmail.com]]],
  [#link("tel:+62-851-5648-7577", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[0851-5648-7577]]],
  [#link("https://profildmr.devplay.online/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[profildmr.devplay.online]]],
  [#link("https://github.com/KarmaSenzu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[KarmaSenzu]]],
  [#link("https://linkedin.com/in/damar-fikrie", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[damar-fikrie]]],
)


== Summary

Junior Data & Backend Engineer lulusan S.Kom Cum Laude (IPK 3.85) dengan sertifikasi BNSP. Menguasai scripting Python, perancangan pipeline data otomatis (ETL), pemodelan database relasional SQL (PostgreSQL), serta pengawasan utilisasi server Linux.

== Experience

#regular-entry(
  [
    #strong[Mentari Solusi Indonesia], Full Stack & IT Systems Specialist

    - Mengembangkan aplikasi web dan sistem inventaris pergudangan terintegrasi database relasional

    - Merancang modul formulir barang dinamis, penomoran kode stok otomatis, dan validasi data transaksi real-time

    - Mengonfigurasi deployment containerized pada Linux VPS dan reverse proxy Nginx untuk keandalan akses server

  ],
  [
    Jakarta, Indonesia

    Jun 2025 – Nov 2025

    

    6 months

  ],
)

#regular-entry(
  [
    #strong[Freelance IT], Software & Technical Specialist

    - Mengembangkan aplikasi web, sistem kasir\/POS desktop, dan RESTful API terstruktur untuk kebutuhan bisnis klien

    - Melakukan instalasi perangkat keras\/lunak, setup jaringan LAN\/WiFi, dan pemeliharaan sistem komputer

    - Mengelola dan memelihara server Linux VPS dengan Nginx, PM2, Docker Compose, dan backup berkala

  ],
  [
    Jakarta Selatan, Indonesia

    Jan 2022 – Sekarang

    

    4 years 11 months

  ],
)

== Featured Projects

#regular-entry(
  [
    #strong[HERMES-PT.-ASISTEN-DMR — Multi-Source Autonomous AI Data Pipeline]

    - Mengembangkan sistem pipeline pengumpulan data otomatis yang berfungsi memindai, menyaring, dan merangkum riset AI dari arXiv, HuggingFace, & GitHub

    - Menerapkan parsing data terstruktur, transformasi JSON, deduplikasi berita, dan otomasi distribusi terjadwal via Linux Cron ke Telegram

    - #link("https://github.com/KarmaSenzu/HERMES-PT.-ASISTEN-DMR")[Repository Link]

  ],
  [
    Jul 2024 – Sep 2024

  ],
)

#regular-entry(
  [
    #strong[Auto-Subtitle-AI — Automated Speech-to-Text & Data Processing Pipeline]

    - Merancang pipeline pemrosesan audio-ke-teks otomatis yang berfungsi mentranskripsikan dialog video menggunakan model deep learning Faster-Whisper

    - Menyusun sinkronisasi timestamp berkas takarir format ASS dan mengotomatisasi rendering hardsub via pipeline FFmpeg di backend FastAPI Python

    - \[Local Directory Portfolio: Auto Subtitle Editing\]

  ],
  [
    Apr 2024 – Jun 2024

  ],
)

#regular-entry(
  [
    #strong[Golang-Finance — Relational Database Schema & Data Integrity Engine]

    - Merancang skema relasional, optimasi query transaksi keuangan, dan memastikan kepatuhan ACID guna menjaga konsistensi data finansial

    - Menerapkan filtering, pagination berkinerja tinggi, dan penanganan relasi database relasional PostgreSQL & MySQL

    - #link("https://github.com/KarmaSenzu/Golang-Finance")[Repository Link]

  ],
  [
    Feb 2024 – Apr 2024

  ],
)

== Technical Skills

#strong[Kompetensi Utama:] Python, SQL, PostgreSQL, MySQL, Data Pipeline (ETL), Cron Automation, Git, Linux VPS

#strong[Bahasa & Framework:] Python, SQL, Go (Golang), Shell\/Bash Scripting, JavaScript

#strong[Sistem & Infrastruktur:] PostgreSQL, MySQL, Timeseries Data, Docker, Linux Server, Git, REST API Integration

== Education

#education-entry(
  [
    #strong[Universitas Bina Sarana Informatika]

    #emph[Sarjana Komputer (S.Kom.), Jurusan Teknik Informatika]

    - IPK: 3.85 \/ 4.00 (Dengan Pujian \/ Cum Laude)

    - Fokus: Rekayasa Perangkat Lunak, Arsitektur Sistem, Basis Data, & Jaringan Komputer

  ],
  [
    Jakarta Selatan, Indonesia

    Agu 2022 – Okt 2026

  ],
)

#education-entry(
  [
    #strong[SMK Wisata Indonesia]

    #emph[SMK \/ Sekolah Menengah Kejuruan, Jurusan Teknik Komputer dan Jaringan (TKJ)]

  ],
  [
    Jakarta Selatan, Indonesia

    Jul 2019 – Jun 2022

  ],
)

== Certifications

#regular-entry(
  [
    #strong[Sertifikat Kompetensi — Pengembang Perangkat Lunak (Program Analyst)]

    - Badan Nasional Sertifikasi Profesi (BNSP) & LSP UBSI

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
