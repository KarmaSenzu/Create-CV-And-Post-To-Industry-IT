import urllib.request
import urllib.parse
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

test_params = [
    {"page": 1, "size": 10, "text": "developer"},
    {"page": 1, "size": 10, "keyword": "developer"},
    {"page": 1, "size": 10, "search": "developer"},
    {"page": 1, "size": 10, "title": "developer"},
    {"page": 1, "size": 10, "q": "developer"},
]

for p in test_params:
    qs = urllib.parse.urlencode(p)
    url = f"https://bosshire.co.id/api/jobs?{qs}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            jobs = data.get("data", [])
            print(f"Param: {p} -> {len(jobs)} jobs. TotalData: {data.get('totalData')}")
            for j in jobs[:2]:
                print(f"   [{j.get('id')}] {j.get('title')} at {j.get('company')} ({j.get('city')})")
    except Exception as e:
        print(f"Param: {p} -> Error: {e}")

