import urllib.request
import re
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Let's inspect all chunks for 'baseURL' or 'api' or 'jobs'
req = urllib.request.Request("https://bosshire.co.id/id/jobs", headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

chunks = list(set(re.findall(r"/_next/static/chunks/[a-zA-Z0-9_\-\.]+\.js", html)))

for c in sorted(chunks):
    chunk_url = "https://bosshire.co.id" + c
    creq = urllib.request.Request(chunk_url, headers=headers)
    with urllib.request.urlopen(creq) as cresp:
        code = cresp.read().decode("utf-8", errors="ignore")
    
    # search for backend host or api path
    hosts = set(re.findall(r"https?://[a-zA-Z0-9\-\.]+(?::\d+)?(?:/api[a-zA-Z0-9_\-/]*)?", code))
    hosts = [h for h in hosts if "cloudflare" not in h and "google" not in h and "w3.org" not in h and "tiktok" not in h and "schema.org" not in h]
    if hosts:
        print(f"[{c}] Hosts/APIs: {hosts}")

    # search for axios / fetch with job
    job_calls = re.findall(r"[\"'\`]([a-zA-Z0-9_\-/]*job[a-zA-Z0-9_\-/]*)[\"'\`]", code, re.IGNORECASE)
    job_calls = list(set([j for j in job_calls if len(j) > 4 and ("/" in j or "-" in j)]))
    if job_calls:
        print(f"[{c}] Job paths: {job_calls[:10]}")

