import urllib.request
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://bosshire.co.id/_next/static/chunks/2gfjhxgvkn5k3.js"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode("utf-8", errors="ignore")

# Find occurrences of '/jobs' or 'baseURL' or 'axios' or 'NEXT_PUBLIC'
for pattern in [r".{0,100}baseURL.{0,100}", r".{0,100}NEXT_PUBLIC.{0,100}", r".{0,100}/jobs/recommendations.{0,100}", r".{0,100}jobs/hot-list.{0,100}"]:
    print(f"=== Pattern: {pattern} ===")
    matches = list(re.finditer(pattern, code))
    print(f"Matches: {len(matches)}")
    for m in matches[:5]:
        print(m.group(0))
        print("-" * 40)

