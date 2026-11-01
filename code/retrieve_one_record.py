"""
One record, retrieved: Wayback CDX API lookup for Cloud9's Partners page,
one capture per year, 2019-2025.
"""
import json
import requests

CDX_ENDPOINT = "https://web.archive.org/cdx/search/cdx"

params = {
    "url": "cloud9.gg/partners",          # page to look up
    "output": "json",                     # JSON instead of plain text
    "from": "2019",                       # start year
    "to": "2025",                         # end year
    "collapse": "timestamp:4",            # keep one capture per year (first 4 digits = year)
    "filter": "statuscode:200",           # only successful captures
    "fl": "timestamp,original,statuscode,mimetype,length",  # fields to return
}

headers = {
    "User-Agent": "EsportsSponsorshipStudy/1.0 (student class project; contact: mich3094@colorado.edu)"
}

response = requests.get(CDX_ENDPOINT, params=params, headers=headers, timeout=60)

print("Request URL:", response.url)
print("Status code:", response.status_code)

rows = response.json()
print("\nRaw response:")
print(json.dumps(rows, indent=1))

header, captures = rows[0], rows[1:]
print(f"\n{len(captures)} captures found:")
for row in captures:
    record = dict(zip(header, row))
    snapshot_url = f"https://web.archive.org/web/{record['timestamp']}/{record['original']}"
    print(record["timestamp"][:4], record["statuscode"], record["length"], snapshot_url)
