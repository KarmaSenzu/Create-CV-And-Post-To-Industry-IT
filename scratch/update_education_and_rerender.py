import os
import glob
import subprocess
import re

workspace_dir = "/Users/damarfikrie/Desktop/Create CV And Post To Industry IT"
rendercv_bin = os.path.join(workspace_dir, ".venv/bin/rendercv")

folders = sorted(glob.glob(os.path.join(workspace_dir, "output/*/*")))
print(f"Total folders found: {len(folders)}")

for folder_path in folders:
    rel_folder = os.path.relpath(folder_path, workspace_dir)
    cv_yaml_path = os.path.join(folder_path, "cv.yaml")
    
    if not os.path.exists(cv_yaml_path):
        print(f"Skipping {rel_folder}: no cv.yaml")
        continue

    with open(cv_yaml_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine if English or Indonesian
    is_english = "Bachelor of Science" in content or "Informatics Engineering" in content or "Worldwide" in content

    if is_english:
        # English replacements
        content = re.sub(
            r"degree:\s*Bachelor of Science\s*\(In Progress\)",
            "degree: Bachelor of Computer Science (S.Kom.) — Fresh Graduate",
            content
        )
        content = re.sub(
            r"degree:\s*Bachelor of Science[^\n]*",
            "degree: Bachelor of Computer Science (S.Kom.) — Fresh Graduate",
            content
        )
        content = re.sub(
            r'-\s*"GPA:\s*3\.85\s*/\s*4\.00[^\n]*"',
            '- "GPA: 3.85 / 4.00 (Cum Laude)"',
            content
        )
        # Template indentation check
        content = re.sub(
            r"main_column:\s*\|-\n\s*\*\*INSTITUTION\*\*\n\*([^\n]+)\*\nHIGHLIGHTS",
            r"main_column: |-\n        **INSTITUTION**\n        *\1*\n        HIGHLIGHTS",
            content
        )
    else:
        # Indonesian replacements
        content = re.sub(
            r"degree:\s*Sarjana\s*\(S1\)\s*—\s*Sedang Berjalan",
            "degree: Sarjana Komputer (S.Kom.) — Fresh Graduate",
            content
        )
        content = re.sub(
            r"degree:\s*Sarjana\s*\(S1\)[^\n]*",
            "degree: Sarjana Komputer (S.Kom.) — Fresh Graduate",
            content
        )
        content = re.sub(
            r'-\s*"IPK:\s*3,85\s*/\s*4,00[^\n]*"',
            '- "IPK: 3,85 / 4,00 (Cum Laude)"',
            content
        )
        # Template indentation check
        content = re.sub(
            r"main_column:\s*\|-\n\s*\*\*INSTITUTION\*\*\n\*([^\n]+)\*\nHIGHLIGHTS",
            r"main_column: |-\n        **INSTITUTION**\n        *\1*\n        HIGHLIGHTS",
            content
        )

    with open(cv_yaml_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Rendering {rel_folder}...")
    res = subprocess.run([rendercv_bin, "render", "cv.yaml"], cwd=folder_path, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  [ERROR] {rel_folder}: {res.stderr}")
    else:
        # Copy output PDF to folder root
        pdf_matches = glob.glob(os.path.join(folder_path, "rendercv_output", "*.pdf"))
        for p in pdf_matches:
            dest = os.path.join(folder_path, os.path.basename(p))
            subprocess.run(["cp", p, dest])
            print(f"  [SUCCESS] Copied: {os.path.basename(dest)}")

print("\n--- ALL FOLDERS UPDATED AND RENDERED ---")
