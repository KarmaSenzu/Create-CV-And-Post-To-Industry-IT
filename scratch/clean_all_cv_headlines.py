#!/usr/bin/env python3
"""
Clean all CV headlines to simple, professional job titles.
Removes programming languages in parentheses and academic honors / certs from the headline line.
Re-renders all PDFs using RenderCV.
"""

import os
import glob
import re
import shutil
import subprocess

WORKSPACE = "/Users/damarfikrie/Desktop/Create CV And Post To Industry IT"
RENDERCV = os.path.join(WORKSPACE, ".venv", "bin", "rendercv")

def clean_headline(raw):
    clean = raw.strip().strip('"\'')
    # Remove pipe separated segments (e.g., "| S.Kom. (Cum Laude 3.85) | BNSP Certified")
    clean = clean.split('|')[0].strip()
    # Remove parenthetical details (e.g., "(React.js / Laravel / Node.js)")
    clean = re.sub(r'\s*\([^)]*\)', '', clean).strip()
    return clean

def main():
    files = sorted(glob.glob(os.path.join(WORKSPACE, 'output', '**', 'cv.yaml'), recursive=True))
    print(f"Found {len(files)} cv.yaml files.")

    success_count = 0
    for cv_path in files:
        job_dir = os.path.dirname(cv_path)
        with open(cv_path, 'r', encoding='utf-8') as fp:
            content = fp.read()

        m = re.search(r'^(\s*headline:\s*)(.+)$', content, re.MULTILINE)
        if not m:
            print(f"[SKIP] No headline found in {cv_path}")
            continue

        prefix = m.group(1)
        raw_val = m.group(2)
        cleaned_val = clean_headline(raw_val)

        new_headline_line = f'{prefix}"{cleaned_val}"'
        new_content = content[:m.start()] + new_headline_line + content[m.end():]

        with open(cv_path, 'w', encoding='utf-8') as fp:
            fp.write(new_content)

        print(f"\nProcessing {os.path.basename(job_dir)}:")
        print(f"  Old: {raw_val}")
        print(f"  New: {cleaned_val}")

        # Re-render via RenderCV
        res = subprocess.run([RENDERCV, "render", "cv.yaml"], cwd=job_dir, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  [ERROR] RenderCV failed:\n{res.stderr}")
            continue

        # Find rendered PDF and copy to root of job_dir
        out_dir = os.path.join(job_dir, "rendercv_output")
        pdfs = glob.glob(os.path.join(out_dir, "*.pdf"))
        if pdfs:
            latest_pdf = pdfs[0]
            target_pdf = os.path.join(job_dir, os.path.basename(latest_pdf))
            shutil.copy2(latest_pdf, target_pdf)
            print(f"  [SUCCESS] Rendered & copied PDF: {os.path.basename(target_pdf)}")
            success_count += 1
        else:
            print(f"  [WARNING] No PDF generated in {out_dir}")

    print(f"\n=== Completed: Successfully updated and rendered {success_count}/{len(files)} CVs! ===")

if __name__ == "__main__":
    main()

