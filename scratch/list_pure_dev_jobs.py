import urllib.request
import urllib.parse
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def clean_html(text):
    if not text:
        return ""
    clean = re.sub(r"<[^>]+>", " ", text)
    clean = clean.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", clean).strip()

keywords = ["developer", "software", "fullstack", "backend", "frontend", "golang", "engineer", "programmer"]

all_jobs = {}
for kw in keywords:
    page = 1
    while True:
        params = {"page": page, "size": 20, "text": kw}
        url = f"https://bosshire.co.id/api/jobs?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                data = res.get("data", [])
                total = res.get("totalData", 0)
                for j in data:
                    all_jobs[j.get("id")] = j
                if len(data) < 20 or page * 20 >= total:
                    break
                page += 1
        except Exception:
            break

print(f"Total jobs: {len(all_jobs)}")

dev_jobs = []
for jid, j in all_jobs.items():
    title = j.get("title", "")
    t_lower = title.lower()
    
    # Exclude non-software jobs (sales, civil, electrical, hvac, mandarin translator, hr)
    if any(ex in t_lower for ex in ["hvac", "civil", "sales", "geotechnical", "electrical", "translator", "mandarin speaker", "business dev", "netsuite", "accounting"]):
        continue
    if any(inc in t_lower for inc in ["developer", "software", "programmer", "full-stack", "fullstack", "backend", "frontend", "golang", "web"]):
        dev_jobs.append(j)

print(f"Found {len(dev_jobs)} pure developer jobs on BossHire:")
for j in dev_jobs:
    sal_min = j.get("minSalaryAmount")
    sal_max = j.get("maxSalaryAmount")
    sal_str = f"Rp {sal_min:,} - {sal_max:,}" if sal_min and sal_max else "Tidak Ditampilkan"
    print(f"- [{j.get('id')}] {j.get('title')} @ {j.get('company')} ({j.get('city')}) | {sal_str} | Exp: {j.get('experienceYear')}")

