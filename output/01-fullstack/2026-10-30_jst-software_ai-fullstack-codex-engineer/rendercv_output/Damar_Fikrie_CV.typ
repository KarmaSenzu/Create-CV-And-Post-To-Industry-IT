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

  #headline([AI Full-Stack Engineer \/ Codex Engineer])

#connections(
  [#connection-with-icon("location-dot")[Jakarta Selatan, Indonesia]],
  [#link("mailto:damarfikrie@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[damarfikrie\@gmail.com]]],
  [#link("tel:+62-851-5648-7577", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[0851-5648-7577]]],
  [#link("https://profildmr.devplay.online/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[profildmr.devplay.online]]],
  [#link("https://github.com/KarmaSenzu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[KarmaSenzu]]],
  [#link("https://linkedin.com/in/damar-fikrie", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[damar-fikrie]]],
)


== Summary

Full Stack Developer and Informatics graduate (S.Kom., GPA 3.85 \/ 4.00) certified by BNSP as a Software Developer (Program Analyst). Proficient in high-velocity full-stack engineering across modern ecosystems (React.js, Next.js, Node.js, Go) and AI-driven workflows (autonomous AI agents, prompt engineering, and LLM integrations). Experienced in architecting robust RESTful APIs, relational databases (PostgreSQL & MySQL), and containerized deployments on Linux VPS.

== Experience

#regular-entry(
  [
    #strong[Mentari Solusi Indonesia], Full Stack Developer

    - Developed end-to-end full stack web applications and REST API architectures utilizing React.js, TypeScript, PHP, and MySQL

    - Engineered smart inventory management forms with dynamic categorization, automated stock coding, and real-time validation

    - Configured containerized production deployments on Linux VPS servers utilizing Docker and Nginx reverse proxy

  ],
  [
    Jakarta, Indonesia

    June 2025 – Nov 2025

    

    6 months

  ],
)

#regular-entry(
  [
    #strong[Freelance IT], Software & Technical Specialist

    - Architected production-ready web applications and structured RESTful APIs with standardized authentication using Node.js, Express.js, React.js, and PHP

    - Designed and optimized relational database schemas and queries in MySQL and PostgreSQL for transactional business operations

    - Built inventory tracking systems, cash register POS applications, and financial tools automating multi-item cataloging

    - Managed and maintained production Linux servers utilizing Nginx reverse proxy, PM2 process manager, and Docker Compose

  ],
  [
    Jakarta Selatan, Indonesia

    Jan 2022 – present

    

    5 years

  ],
)

== Featured Projects

#regular-entry(
  [
    #strong[Dmrxai — Self-Hosted Multi-Model AI Chat & Automation Platform]

    - Built a self-hosted multi-model AI platform using Next.js, TypeScript, and Docker Compose supporting document analysis and intelligent search

    - Integrated AI model APIs with structured prompt engineering, automated agent tooling, and responsive UI components

    - #link("https://github.com/KarmaSenzu/Dmrxai")[Repository Link]

  ],
  [
    May 2024 – Aug 2024

  ],
)

#regular-entry(
  [
    #strong[HERMES-PT.-ASISTEN-DMR — Autonomous AI Agent System & Pipeline]

    - Developed an autonomous 3-bot agent framework in Python automating multi-source AI research scanning (arXiv, HuggingFace, OpenAI, GitHub)

    - Implemented structured JSON data pipelines, deduplication logic, and scheduled dispatching via Linux Cron to Telegram

    - #link("https://github.com/KarmaSenzu/HERMES-PT.-ASISTEN-DMR")[Repository Link]

  ],
  [
    July 2024 – Sept 2024

  ],
)

#regular-entry(
  [
    #strong[Golang-Finance — RESTful Financial Transaction API & Clean Architecture]

    - Designed modular financial REST API applying Clean Architecture (handler -\> service -\> repository) with Go, Gin, and MySQL\/PostgreSQL

    - Implemented JWT authentication, multi-currency transaction filtering, pagination, rate limiting, and Docker Compose orchestration

    - #link("https://github.com/KarmaSenzu/Golang-Finance")[Repository Link]

  ],
  [
    Feb 2024 – Apr 2024

  ],
)

#regular-entry(
  [
    #strong[Golang-Rekam — Real-Time Video Streaming & Recording Platform]

    - Built full-stack real-time streaming platform with Go Gin backend, gorilla\/websocket hub, PostgreSQL 16, React 18, TypeScript, and Zustand

    - Implemented JWT authentication, MediaRecorder API video stream processing, and interactive recorded playback

    - #link("https://github.com/KarmaSenzu/golang-rekam")[Repository Link]

  ],
  [
    Aug 2024 – Oct 2024

  ],
)

== Technical Skills

#strong[Core Competencies:] AI-Assisted Development (Codex\/Copilot workflows), Full-Stack Architecture, RESTful API Design, Relational Database Modeling, System Observability

#strong[Programming Languages:] Go, JavaScript, TypeScript, Python, PHP, Java, SQL, Linux Shell, HTML, CSS

#strong[Frameworks & Libraries:] React.js, Next.js, Node.js, Express.js, FastAPI, Gin, Tailwind CSS, Zustand, Electron, Three.js

#strong[Databases & Cloud Infra:] PostgreSQL, MySQL, Redis, Linux VPS, Docker, Docker Compose, Nginx, PM2, Cloudflare Tunnel, Git

== Education

#education-entry(
  [
    #strong[Universitas Bina Sarana Informatika]

    #emph[Bachelor of Computer Science (Sarjana Komputer \/ S.Kom.) — Major in Informatics \/ Computer Science]

    - GPA: 3.85 \/ 4.00 (With Honors \/ )

    - Focus: Software Engineering, Full-Stack Architecture & Database Systems

  ],
  [
    Jakarta Selatan, Indonesia

    Aug 2022 – Oct 2026

  ],
)

#education-entry(
  [
    #strong[SMK Wisata Indonesia]

    #emph[Vocational High School Diploma — Major in Computer & Network Engineering (TKJ)]

  ],
  [
    Jakarta Selatan, Indonesia

    July 2019 – June 2022

  ],
)

== Certifications

#regular-entry(
  [
    #strong[Software Developer Competency Certificate (Program Analyst \/ Analis Program)]

    - Indonesian National Board for Professional Certification (BNSP) & LSP UBSI

  ],
  [
    Sept 2025 – Sept 2028

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
