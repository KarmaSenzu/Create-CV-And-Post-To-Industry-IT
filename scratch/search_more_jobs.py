import urllib.request
import urllib.parse
import re
import json
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 1. Load existing URLs from jobs.csv
existing_urls = set()
with open("jobs/jobs.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        u = r.get("job_url", "").strip()
        if u:
            existing_urls.add(u)

print(f"Existing tracked URLs: {len(existing_urls)}")

# 2. Search Glints explore pages
glints_explore = [
    "https://glints.com/id/explore/junior-developer/in-dki-jakarta",
    "https://glints.com/id/explore/web-developer/in-dki-jakarta",
    "https://glints.com/id/explore/react-developer/in-dki-jakarta",
    "https://glints.com/id/explore/backend-developer/in-dki-jakarta",
    "https://glints.com/id/explore/full-stack-developer/in-dki-jakarta",
    "https://glints.com/id/explore/software-engineer/in-dki-jakarta",
    "https://glints.com/id/explore/software-developer/in-dki-jakarta",
    "https://glints.com/id/explore/developers/in-tangerang",
    "https://glints.com/id/explore/developers/in-bekasi",
]

glints_candidates = set()
for eu in glints_explore:
    try:
        req = urllib.request.Request(eu, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            jobs = set(re.findall(r"/opportunities/jobs/[a-zA-Z0-9\-]+/[a-f0-9\-]+", html))
            for j in jobs:
                full_url = "https://glints.com/id" + j
                if full_url not in existing_urls:
                    glints_candidates.add(full_url)
    except Exception as e:
        print(f"Err {eu}: {e}")

print(f"Found {len(glints_candidates)} new candidate Glints URLs")

# 3. Search BossHire API
bosshire_keywords = [
    "developer", "software", "fullstack", "backend", "frontend", "golang", "web",
    "react", "node", "laravel", "python", "programmer", "api", "junior"
]

bosshire_candidates = {}
for kw in bosshire_keywords:
    page = 1
    while True:
        params = {"page": page, "size": 20, "text": kw}
        url = f"https://bosshire.co.id/api/jobs?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                data = res.get("data", [])
                total = res.get("totalData", 0)
                for j in data:
                    jid = j.get("id")
                    job_url = f"https://bosshire.co.id/id/jobs/detail/{jid}"
                    if job_url not in existing_urls and jid not in bosshire_candidates:
                        bosshire_candidates[jid] = j
                if len(data) < 20 or page * 20 >= total:
                    break
                page += 1
        except Exception as e:
            break

print(f"Found {len(bosshire_candidates)} new candidate BossHire jobs")

# Save candidates to inspect
with open("scratch/glints_candidates.json", "w", encoding="utf-8") as f:
    json.dump(list(glints_candidates), f, indent=2)

with open("scratch/bosshire_candidates.json", "w", encoding="utf-8") as f:
    json.dump(bosshire_candidates, f, indent=2)

