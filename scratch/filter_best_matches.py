import json
import urllib.request
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 1. Filter Glints candidates
with open("scratch/glints_candidates.json", "r", encoding="utf-8") as f:
    glints_urls = json.load(f)

print(f"Total Glints candidates to check: {len(glints_urls)}")

# Filter relevant keywords in Glints URL slugs
relevant_glints = []
for u in glints_urls:
    slug = u.lower()
    if any(k in slug for k in ["fullstack", "full-stack", "backend", "golang", "software-engineer", "junior", "web-developer"]):
        if not any(ex in slug for ex in ["intern", "sales", "hr", "qa", "tester", "marketing", "android", "ios", "flutter", "devops"]):
            relevant_glints.append(u)

print(f"Filtered {len(relevant_glints)} high-priority Glints candidates.")

# Let's inspect details of first 15 Glints candidates
valid_glints = []
for u in relevant_glints[:20]:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            m = re.search(r"<script id=\"__NEXT_DATA__\" type=\"application/json\">(.*?)</script>", html)
            if m:
                data = json.loads(m.group(1))
                job = data.get("props", {}).get("pageProps", {}).get("initialData", {}).get("data", {})
                title = job.get("title")
                status = job.get("status")
                company = job.get("company", {}).get("name")
                city = job.get("city", {}).get("name")
                sals = job.get("salaries", [])
                sal_str = "Tidak Ditampilkan"
                if sals:
                    sal_str = f"Rp {sals[0].get('minAmount'):,} - {sals[0].get('maxAmount'):,}"
                skills = [s.get("skill", {}).get("name") for s in job.get("skills", []) if s.get("skill")]
                min_exp = job.get("minYearsOfExperience")
                max_exp = job.get("maxYearsOfExperience")
                if status == "OPEN":
                    valid_glints.append({
                        "url": u,
                        "title": title,
                        "company": company,
                        "city": city,
                        "salary": sal_str,
                        "skills": skills,
                        "exp": f"{min_exp}-{max_exp} yrs"
                    })
                    print(f"[GLINTS OPEN] {title} @ {company} ({city}) | {sal_str} | Exp: {min_exp}-{max_exp}")
    except Exception as e:
        pass

# 2. Filter BossHire candidates
with open("scratch/bosshire_candidates.json", "r", encoding="utf-8") as f:
    bosshire_dict = json.load(f)

print(f"\nTotal BossHire candidates: {len(bosshire_dict)}")
valid_bosshire = []
for jid, j in bosshire_dict.items():
    title = j.get("title", "")
    t_lower = title.lower()
    if any(k in t_lower for k in ["developer", "software", "programmer", "full-stack", "fullstack", "backend", "golang", "web"]):
        if not any(ex in t_lower for ex in ["hvac", "civil", "sales", "geotechnical", "electrical", "translator", "mandarin", "accounting", "japanese"]):
            sal_min = j.get("minSalaryAmount")
            sal_max = j.get("maxSalaryAmount")
            sal_str = f"Rp {sal_min:,} - {sal_max:,}" if sal_min and sal_max else "Tidak Ditampilkan"
            valid_bosshire.append({
                "id": jid,
                "url": f"https://bosshire.co.id/id/jobs/detail/{jid}",
                "title": title,
                "company": j.get("company"),
                "city": j.get("city"),
                "salary": sal_str,
                "exp": j.get("experienceYear")
            })
            print(f"[BOSSHIRE ACTIVE] {title} @ {j.get('company')} ({j.get('city')}) | {sal_str} | Exp: {j.get('experienceYear')}")

