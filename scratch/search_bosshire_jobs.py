import urllib.request
import urllib.parse
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

keywords = ["developer", "software", "fullstack", "full stack", "backend", "frontend", "golang", "web", "programmer", "engineer"]

all_jobs = {}

for kw in keywords:
    page = 1
    while True:
        params = {"page": page, "size": 20, "text": kw}
        qs = urllib.parse.urlencode(params)
        url = f"https://bosshire.co.id/api/jobs?{qs}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                data = res.get("data", [])
                total = res.get("totalData", 0)
                for j in data:
                    jid = j.get("id")
                    if jid not in all_jobs:
                        all_jobs[jid] = j
                if len(data) < 20 or page * 20 >= total:
                    break
                page += 1
        except Exception as e:
            print(f"Error {kw} p{page}: {e}")
            break

print(f"Total unique jobs found across all keywords: {len(all_jobs)}")

# Filter relevant IT/Software development jobs
relevant = []
for jid, j in all_jobs.items():
    title = j.get("title", "")
    industry = j.get("industry", "")
    city = j.get("city", "")
    comp = j.get("company", "")
    
    # Check if software/tech
    t_lower = title.lower()
    ind_lower = industry.lower()
    
    # Skip sales, civil, accounting, mandarin unless tech
    if any(k in t_lower for k in ["developer", "software", "frontend", "backend", "fullstack", "full stack", "golang", "web", "programmer", "it "]) or "it" in ind_lower or "software" in ind_lower or "information technology" in ind_lower:
        relevant.append(j)

print(f"Total relevant IT/Dev jobs: {len(relevant)}\n")
for j in relevant:
    sal_min = j.get("minSalaryAmount")
    sal_max = j.get("maxSalaryAmount")
    curr = j.get("minSalaryCurrency") or "IDR"
    sal_str = f"{curr} {sal_min:,} - {sal_max:,}" if sal_min and sal_max else "Tidak Ditampilkan"
    print(f"ID: {j.get('id')}")
    print(f"Title: {j.get('title')}")
    print(f"Company: {j.get('company')} | City: {j.get('city')}, {j.get('province')}")
    print(f"Industry: {j.get('industry')} | Level: {j.get('jobLevel')} | Work: {j.get('workingType')}")
    print(f"Salary: {sal_str} | Exp: {j.get('experienceYear')}")
    print(f"Public URL: https://bosshire.co.id/id/jobs/detail/{j.get('id')}")
    print("-" * 60)

