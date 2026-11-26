import urllib.request
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

with open("scratch/glints_candidates.json", "r", encoding="utf-8") as f:
    glints_urls = json.load(f)

# Targets to check
target_terms = [
    "fullstack-developer-golang-react-js",
    "backend-developer-golang",
    "software-engineer-front-end-developer",
    "full-stack-developer",
    "backend-developer-nodejs-expressjs",
    "software-engineer-project-based",
    "junior-software-engineer"
]

selected_urls = []
for u in glints_urls:
    for t in target_terms:
        if t in u.lower():
            selected_urls.append(u)
            break

print(f"Inspecting {len(selected_urls)} matched URLs:")

for u in selected_urls[:15]:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            m = re.search(r"<script id=\"__NEXT_DATA__\" type=\"application/json\">(.*?)</script>", html)
            if m:
                data = json.loads(m.group(1))
                job = data.get("props", {}).get("pageProps", {}).get("initialData", {}).get("data", {})
                title = job.get("title")
                status = job.get("status")
                company = job.get("company", {}).get("name")
                loc = job.get("location", {})
                city = loc.get("formattedName") if isinstance(loc, dict) else str(loc)
                sals = job.get("salaries", [])
                sal_str = "Tidak Ditampilkan"
                if sals:
                    sal_str = f"Rp {sals[0].get('minAmount'):,} - {sals[0].get('maxAmount'):,}"
                skills = [s.get("skill", {}).get("name") for s in job.get("skills", []) if s.get("skill")]
                min_exp = job.get("minYearsOfExperience")
                max_exp = job.get("maxYearsOfExperience")
                
                # desc
                desc_json = job.get("descriptionJsonString")
                desc_text = ""
                if desc_json:
                    try:
                        desc_obj = json.loads(desc_json)
                        blocks = desc_obj.get("blocks", [])
                        desc_text = " ".join([b.get("text", "") for b in blocks if b.get("text")])
                    except:
                        desc_text = desc_json[:150]

                print(f"URL: {u}")
                print(f"Company: {company} | Title: {title} | Status: {status} | Loc: {city} | Sal: {sal_str} | Exp: {min_exp}-{max_exp}")
                print(f"Skills: {skills}")
                print(f"Desc: {desc_text[:200]}...")
                print("-" * 60)
    except Exception as e:
        print(f"Err {u}: {e}")

