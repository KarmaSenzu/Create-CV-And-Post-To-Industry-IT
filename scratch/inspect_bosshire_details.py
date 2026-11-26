import urllib.request
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

target_ids = [
    "D9GU6S6DDD4S73FAN4I0", # Software Engineer - PT Suvarna Media Informatika
    "D8FQBB40FEPC73EL8F0G", # Full Stack Junior Programmer - Pharos Indonesia
    "D913AJ5UMSUS73FIM62G", # Full-Stack Engineer - Bosshire
    "D8FTLT40FEPC73EL8NO0", # Java Backend Developer - Pembiayaan Digital Indonesia
    "DBG4AVCLP0MS73D12FUG", # Let's see what this is
]

def clean_html(text):
    if not text:
        return ""
    # remove html tags
    clean = re.sub(r"<[^>]+>", " ", text)
    clean = clean.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", clean).strip()

for jid in target_ids:
    url = f"https://bosshire.co.id/api/jobs/{jid}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            job = raw.get("data", {})
            title = job.get("title")
            comp = job.get("company", {}).get("name") if isinstance(job.get("company"), dict) else job.get("company")
            status = job.get("jobStatus", {}).get("text") if isinstance(job.get("jobStatus"), dict) else job.get("jobStatus")
            city = job.get("city", {}).get("text") if isinstance(job.get("city"), dict) else job.get("city")
            sal_min = job.get("minSalaryAmount")
            sal_max = job.get("maxSalaryAmount")
            curr = job.get("minSalaryCurrency") or "IDR"
            sal_str = f"{curr} {sal_min:,} - {sal_max:,}" if sal_min and sal_max else "Tidak Ditampilkan"
            exp = job.get("experienceYear", {}).get("text") if isinstance(job.get("experienceYear"), dict) else job.get("experienceYear")
            work_type = job.get("workingType", {}).get("text") if isinstance(job.get("workingType"), dict) else job.get("workingType")
            skills = [s.get("name") if isinstance(s, dict) else s for s in job.get("skills", [])]
            desc = clean_html(job.get("description"))
            reqs = clean_html(job.get("jobRequirements"))
            
            print(f"ID: {jid}")
            print(f"Title: {title}")
            print(f"Company: {comp} | Location: {city} | Status: {status}")
            print(f"Salary: {sal_str} | Work Type: {work_type} | Exp: {exp}")
            print(f"Skills: {skills}")
            print(f"Description:\n{desc[:300]}...")
            print(f"Requirements:\n{reqs[:300]}...")
            print("=" * 70)
    except Exception as e:
        print(f"Error {jid}: {e}")

