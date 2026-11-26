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
    day: 26,
  ),
)


= Damar Fikrie

  #headline([IT Support Specialist])

#connections(
  [#connection-with-icon("location-dot")[Jakarta Selatan, Indonesia]],
  [#link("mailto:damarfikrie@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[damarfikrie\@gmail.com]]],
  [#link("tel:+62-851-5648-7577", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[0851-5648-7577]]],
  [#link("https://profildmr.devplay.online/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[profildmr.devplay.online]]],
  [#link("https://github.com/KarmaSenzu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[KarmaSenzu]]],
  [#link("https://linkedin.com/in/damar-fikrie", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[damar-fikrie]]],
)


== Summary

Tenaga IT Support profesional lulusan Sarjana Komputer (S.Kom., IPK 3.85) dengan sertifikasi BNSP. Berpengalaman menangani perakitan dan troubleshooting PC\/laptop, penarikan dan konfigurasi jaringan LAN\/WiFi kantor, administrasi OS Windows & Linux, serta pemeliharaan infrastruktur operasional.

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

    

    5 years

  ],
)

== Featured Projects

#regular-entry(
  [
    #strong[ServerMonitoring — Infrastructure & Host Monitoring Command Center]

    - Command center sentral yang berfungsi memantau utilisasi CPU, memori, disk, dan konektivitas jaringan multi-server secara real-time

    - Mengotomatisasi diagnosa kesehatan sistem operasi, eksekusi perintah perbaikan darurat via SSH, dan alerting instan lonjakan beban

    - #link("https://github.com/KarmaSenzu/ServerMonitoring")[Repository Link]

  ],
  [
    Jun 2024 – Okt 2024

  ],
)

#regular-entry(
  [
    #strong[Linux & Windows Infrastructure Administration & Office Networking]

    - Mengonfigurasi server Linux VPS, routing firewall, setup reverse proxy Nginx, dan manajemen akun pengguna jaringan kantor

    - Melakukan troubleshooting konektivitas jaringan LAN\/WLAN, penanganan error driver periferal, dan pemeliharaan sistem berkala

    - \[Infrastructure Portfolio: Self-Hosted Server & VPS\]

  ],
  [
    Jan 2023 – Sekarang

  ],
)

#regular-entry(
  [
    #strong[Hardware Diagnostic, PC Assembly, & Workstation Deployment]

    - Berpengalaman dalam perakitan PC dari nol, instalasi sistem operasi Windows & Linux, konfigurasi printer sharing, dan diagnosa komponen fisik

    - Memberikan dukungan teknis cepat (end-user support) untuk mengatasi kendala software maupun koneksi jaringan pengguna

    - \[Technical Support Operations\]

  ],
  [
    Jan 2022 – Sekarang

  ],
)

== Technical Skills

#strong[Kompetensi Utama:] Hardware Troubleshooting, LAN\/WLAN Networking, Windows & Linux OS, IT Helpdesk, Perawatan Periferal

#strong[Bahasa & Framework:] Shell Scripting, Command Line, PowerShell, Windows Desktop\/Server, Ubuntu Linux

#strong[Sistem & Infrastruktur:] TCP\/IP, DNS, DHCP, WiFi Router Setup, Remote Desktop (AnyDesk\/RDP), PC Assembly, Backup Data

== Education

#education-entry(
  [
    #strong[Universitas Bina Sarana Informatika]

    #emph[Sarjana Komputer (S.Kom.), Jurusan Teknik Informatika]

    - IPK: 3.85 \/ 4.00

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
