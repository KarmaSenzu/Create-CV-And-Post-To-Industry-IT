import urllib.request
import re
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

# 1. Fetch /id/jobs?text=developer
url = "https://bosshire.co.id/id/jobs?text=developer"
print(f"Fetching: {url}")
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    print("Fetched HTML length:", len(html))
    
    # search for job titles or cards
    # Look for /jobs/detail/ or /talent/job-openings/ in HTML
    detail_links = set(re.findall(r"/id/jobs/detail/[a-zA-Z0-9_\-]+", html))
    print(f"Found {len(detail_links)} job detail links in /id/jobs?text=developer:")
    for l in sorted(detail_links)[:10]:
        print("  ", l)

    # If no detail links directly, look for UUIDs or IDs
    uuids = set(re.findall(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", html))
    print(f"Found {len(uuids)} UUIDs in HTML.")

except Exception as e:
    print("Error fetching:", e)

