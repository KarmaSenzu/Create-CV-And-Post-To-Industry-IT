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

  #headline([Software Engineer])

#connections(
  [#connection-with-icon("location-dot")[Jakarta Selatan, Indonesia]],
  [#link("mailto:damarfikrie@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[damarfikrie\@gmail.com]]],
  [#link("tel:+62-851-5648-7577", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[0851-5648-7577]]],
  [#link("https://profildmr.devplay.online/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[profildmr.devplay.online]]],
  [#link("https://github.com/KarmaSenzu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[KarmaSenzu]]],
  [#link("https://linkedin.com/in/damar-fikrie", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[damar-fikrie]]],
)


== Summary

Software Engineer lulusan Sarjana Komputer (S.Kom., IPK 3.85 \/ 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Berpengalaman membangun aplikasi web berbasis backend PHP\/Laravel dan Go, perancangan dan optimasi kueri basis data relasional PostgreSQL & MySQL, arsitektur RESTful API, serta manajemen deployment server Linux VPS.

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

    - Mengembangkan platform web responsif modern, integrasi backend API asinkron, dan manajemen database relasional

    - Mengonfigurasi server Linux VPS (Ubuntu), deployment containerized via Docker & Docker Compose, serta automasi pipeline

    - Menulis dokumentasi teknis komprehensif, implementasi pengujian unit, serta pemeliharaan keandalan sistem produksi

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
    #strong[Mentari-Smart-Warehouse — Aplikasi Web Bisnis & RESTful API (PHP & MySQL)]

    - Mengembangkan aplikasi web inventaris fullstack dengan PHP, React.js, arsitektur REST API, dan MySQL

    - Membangun fitur validasi data transaksional real-time dan konfigurasi server Linux VPS dengan Nginx

    - #link("https://github.com/KarmaSenzu")[Repository Link]

  ],
  [
    Jun 2025 – Nov 2025

  ],
)

#regular-entry(
  [
    #strong[Golang-Finance — Pemodelan Basis Data Relasional PostgreSQL & REST API]

    - Merancang skema database relasional PostgreSQL terindeks dan kueri transaksional berkinerja tinggi

    - Menerapkan pengujian unit terotomatisasi, autentikasi aman JWT, dan kepatuhan prinsip Clean Code

    - #link("https://github.com/KarmaSenzu/Golang-Finance")[Repository Link]

  ],
  [
    Feb 2024 – Apr 2024

  ],
)

#regular-entry(
  [
    #strong[Dmrxai — Multi-Model AI Web Platform & Antarmuka Interaktif]

    - Membangun antarmuka web interaktif modern berbasis React, Next.js 14, TypeScript, dan Tailwind CSS

    - Mengintegrasikan state management responsif dengan backend RESTful API dan kontainer Docker

    - #link("https://github.com/KarmaSenzu/Dmrxai")[Repository Link]

  ],
  [
    Mei 2024 – Agu 2024

  ],
)

== Technical Skills

#strong[Core Competencies:] Full Stack Web Development, Backend RESTful API, Database Design, Clean Architecture, Server Administration

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
