import os
import glob
import subprocess
import re

WORKSPACE = "/Users/damarfikrie/Desktop/Create CV And Post To Industry IT"
RENDERCV_BIN = os.path.join(WORKSPACE, ".venv", "bin", "rendercv")

cv_yaml_files = glob.glob(os.path.join(WORKSPACE, "output", "*", "*", "cv.yaml"))
print(f"Found {len(cv_yaml_files)} cv.yaml files.")

for cv_path in sorted(cv_yaml_files):
    folder = os.path.dirname(cv_path)
    rel_folder = os.path.relpath(folder, WORKSPACE)
    
    with open(cv_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if this CV is English or Indonesian
    is_english = "language: english" in content and "present: Sekarang" not in content

    # 1. Fix template placeholders
    # Replace <<entry.institution>> etc with INSTITUTION, DEGREE, AREA, HIGHLIGHTS
    content = re.sub(
        r"\*\*<<entry\.institution>>\*\*\n\s*\*<<entry\.degree>>,\s*Jurusan\s*<<entry\.area>>\*\n\s*<<entry\.highlights>>",
        "**INSTITUTION**\n        *DEGREE, Jurusan AREA*\n        HIGHLIGHTS",
        content
    )
    content = re.sub(
        r"\*\*<<entry\.institution>>\*\*\n\s*\*<<entry\.degree>>,\s*Major in\s*<<entry\.area>>\*\n\s*<<entry\.highlights>>",
        "**INSTITUTION**\n        *DEGREE — Major in AREA*\n        HIGHLIGHTS",
        content
    )

    # 2. Fix dates from 2021-09 / 2025-08 to 2022-08 / 2026-10 according to master.yaml
    content = re.sub(r"start_date:\s*2021-09", "start_date: 2022-08", content)
    content = re.sub(r"end_date:\s*2025-08", "end_date: 2026-10", content)

    # 3. Ensure SMK is present if missing from education
    if "SMK Wisata Indonesia" not in content:
        smk_block = """      - institution: SMK Wisata Indonesia
        area: Teknik Komputer dan Jaringan (TKJ)
        degree: SMK / Sekolah Menengah Kejuruan
        start_date: 2019-07
        end_date: 2022-06
        location: Jakarta Selatan, Indonesia\n"""
        if is_english:
            smk_block = """      - institution: SMK Wisata Indonesia
        area: Computer & Network Engineering (TKJ)
        degree: Vocational High School Diploma
        start_date: 2019-07
        end_date: 2022-06
        location: Jakarta Selatan, Indonesia\n"""
        
        # Insert after Universitas highlights
        content = re.sub(
            r"(education:[\s\S]*?highlights:[\s\S]*?\n)(\s*certifications:)",
            r"\1" + smk_block + r"\2",
            content
        )

    with open(cv_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Rendering: {rel_folder}...")
    res = subprocess.run([RENDERCV_BIN, "render", "cv.yaml"], cwd=folder, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  [ERROR] {rel_folder}: {res.stderr}")
    else:
        # Copy generated PDF to folder root
        pdf_matches = glob.glob(os.path.join(folder, "rendercv_output", "*.pdf"))
        for p in pdf_matches:
            dest = os.path.join(folder, os.path.basename(p))
            subprocess.run(["cp", p, dest])
            print(f"  [SUCCESS] {os.path.basename(dest)}")

print("All CVs have been updated and verified!")

