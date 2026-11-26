import os
import glob
import subprocess
import re

workspace_dir = "/Users/damarfikrie/Desktop/Create CV And Post To Industry IT"
rendercv_bin = os.path.join(workspace_dir, ".venv/bin/rendercv")

folders = [
    "output/01-fullstack/2026-10-29_goto-tokopedia_junior-software-engineer",
    "output/02-backend/2026-10-29_flip-indonesia_junior-backend-engineer",
    "output/01-fullstack/2026-10-29_kitabisa_junior-full-stack-developer",
    "output/02-backend/2026-10-29_julo_junior-backend-developer",
    "output/04-mobile/2026-10-29_modal-rakyat_junior-mobile-developer",
    "output/03-frontend/2026-10-29_sirclo_junior-frontend-engineer",
    "output/01-fullstack/2026-10-29_koinworks_junior-web-developer",
    "output/01-fullstack/2026-10-29_turing_junior-full-stack-engineer",
    "output/02-backend/2026-10-29_bairesdev_junior-golang-developer",
    "output/02-backend/2026-10-29_codementor-arc_junior-python-backend-developer",
]

for rel_folder in folders:
    folder_path = os.path.join(workspace_dir, rel_folder)
    cv_yaml_path = os.path.join(folder_path, "cv.yaml")
    
    if not os.path.exists(cv_yaml_path):
        print(f"Skipping {rel_folder}: cv.yaml not found")
        continue

    with open(cv_yaml_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix indentation of education_entry main_column
    # Pattern to look for unindented lines after main_column: |-
    content_fixed = re.sub(
        r"main_column: \|-\n\s*\*\*INSTITUTION\*\*\n\*([^\n]+)\*\nHIGHLIGHTS",
        r"main_column: |-\n        **INSTITUTION**\n        *\1*\n        HIGHLIGHTS",
        content
    )

    with open(cv_yaml_path, "w", encoding="utf-8") as f:
        f.write(content_fixed)

    print(f"Rendering: {rel_folder}...")
    res = subprocess.run([rendercv_bin, "render", "cv.yaml"], cwd=folder_path, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  [ERROR] {rel_folder}: {res.stderr}")
    else:
        print(f"  [SUCCESS] {rel_folder}")
        # Look for PDF in rendercv_output
        pdf_matches = glob.glob(os.path.join(folder_path, "rendercv_output", "*.pdf"))
        for p in pdf_matches:
            dest = os.path.join(folder_path, os.path.basename(p))
            subprocess.run(["cp", p, dest])
            print(f"  Copied PDF to: {dest}")

print("Done processing all folders!")
