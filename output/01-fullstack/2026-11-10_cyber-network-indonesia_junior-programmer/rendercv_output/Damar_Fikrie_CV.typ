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
    day: 26,
  ),
)


= Damar Fikrie

  #headline([Junior Programmer])

#connections(
  [#connection-with-icon("location-dot")[Jakarta Selatan, Indonesia]],
  [#link("mailto:damarfikrie@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[damarfikrie\@gmail.com]]],
  [#link("tel:+62-851-5648-7577", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[0851-5648-7577]]],
  [#link("https://profildmr.devplay.online/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[profildmr.devplay.online]]],
  [#link("https://github.com/KarmaSenzu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[KarmaSenzu]]],
  [#link("https://linkedin.com/in/damar-fikrie", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[damar-fikrie]]],
)


== Summary

Junior Programmer lulusan Sarjana Komputer (S.Kom., IPK 3.85) dengan Sertifikasi Resmi PCAP Python (Python Institute & Cisco) dan BNSP Analis Program. Menguasai pengembangan aplikasi web modern (React.js), backend REST API (Python FastAPI & Go), database relasional (MySQL & PostgreSQL), lingkungan server Linux, dan orkestrasi Docker.

== Experience

#regular-entry(
  [
    #strong[Mentari Solusi Indonesia], Full Stack Developer

    - Mengembangkan aplikasi web full stack dan arsitektur REST API menggunakan React.js, TypeScript, PHP, dan database MySQL

    - Membangun form inventaris pintar dengan kategorisasi dinamis, penomoran kode barang otomatis, dan validasi real-time

    - Mengonfigurasi deployment server produksi pada Linux VPS menggunakan kontainer Docker dan reverse proxy Nginx

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

    - Mengembangkan aplikasi web siap produksi dan arsitektur RESTful API terstandarisasi dengan autentikasi aman

    - Merancang dan mengoptimasi skema database relasional MySQL dan PostgreSQL untuk alur transaksi bisnis

    - Mengelola deployment dan pemeliharaan server Linux VPS dengan Nginx reverse proxy, PM2, dan Docker Compose

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
    #strong[Auto-Subtitle-AI — Backend Automasi AI Berbasis Python FastAPI]

    - Merancang backend pengolahan audio-ke-teks otomatis menggunakan Python, FastAPI, Faster-Whisper, dan pipeline FFmpeg

    - Menerapkan arsitektur kode OOP modular, validasi data Pydantic, dan eksekusi tugas background asinkron

    - #link("https://github.com/KarmaSenzu")[Repository Link]

  ],
  [
    Jun 2024 – Sep 2024

  ],
)

#regular-entry(
  [
    #strong[Dmrxai — Multi-Model AI Web Platform & Antarmuka Interaktif]

    - Membangun antarmuka web interaktif modern berbasis Next.js, React, TypeScript, dan integrasi multi-model AI API

    - Mengelola kontainerisasi Docker Compose dan konfigurasi server Linux untuk deployment aplikasi yang stabil

    - #link("https://github.com/KarmaSenzu/Dmrxai")[Repository Link]

  ],
  [
    Mei 2024 – Agu 2024

  ],
)

#regular-entry(
  [
    #strong[ServerMonitoring — Observabilitas Linux VPS & Pemantauan Host]

    - Membangun platform pemantauan multi-host Linux memantau utilisasi hardware real-time dan manajemen proses

    - Mengelola reverse proxy Nginx, konfigurasi port jaringan, dan version control Git secara aktif

    - #link("https://github.com/KarmaSenzu/ServerMonitoring")[Repository Link]

  ],
  [
    Sep 2024 – Nov 2024

  ],
)

== Technical Skills

#strong[Core Competencies:] Arsitektur Backend & Full Stack, Clean Architecture, Desain RESTful API, Pemodelan Database Relasional, Kontainerisasi Docker

#strong[Programming Languages:] Go (Golang), JavaScript, TypeScript, Python, PHP, Java, SQL, Linux Shell, HTML, CSS

#strong[Frameworks & Libraries:] React.js, Next.js, Node.js, Express.js, FastAPI, Gin, Tailwind CSS, Zustand, Electron

#strong[Databases & Cloud Infra:] PostgreSQL, MySQL, Redis, Linux VPS, Docker, Docker Compose, Nginx, PM2, Cloudflare Tunnel, Git

== Education

#education-entry(
  [
    #strong[Universitas Bina Sarana Informatika]

    #emph[Sarjana Komputer (S.Kom. \/ S1) — Fresh Graduate (Lulus) — Teknik Informatika]

    - IPK: 3.85 \/ 4.00

    - Fokus: Rekayasa Perangkat Lunak, Arsitektur Backend & Sistem Database

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
    #strong[Sertifikat Kompetensi Pengembang Perangkat Lunak (Kualifikasi Analis Program)]

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
