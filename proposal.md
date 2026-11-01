# Final Project Proposal

**By: Michael Chow**

## Question

Which industries sponsored top League of Legends organizations from 2019 to 2026, and what type of categories are prominent over the years?

## Intro

Sponsorship is the main source of revenue for most esports teams, more than prize money, league revenue sharing or merchandise sales. Who pays the teams shapes who they depend on and what they are able to do that year. I chose to focus on League of Legends because its franchise league is one of the longest and most prominent franchise leagues in esports and year over year, many of the same organizations will stay and choose to field a team in the esports scene.

## Who would care?

Esports business researchers and team partnership staff tracking where the money comes from, as well as journalists and regulators, would want to know the trends that happened throughout the years and what we are going into 2027. League operators like Riot Games would also like to know what sponsors are going on around the scene so they can set rules on which sponsor categories are allowed.

## What I expect

I expect the early theme of energy drinks, hardware and other consumer brands to dominate early on in the years and the eventual crypto and Web3 surge to happen around 2021–2022 when they were prominent. After the FTX crash, I expect a lot of these forms of currency to not be prominent until recently, in late 2024 to early 2025, where betting and prediction market sponsors will become more prominent. It would surprise me if the industry mix stayed stable, or if crypto sponsors stayed on team pages well after 2023.

## The exact source

Archived copies of each organization's "Partners" and/or "Sponsors" page in the Internet Archive's Wayback Machine will be used to capture and document the changes that happened throughout the different years of each esports organization.

## How I will get it

I will be using techniques from Week 7: Archived web pages and the Wayback Machine, specifically to access the Wayback Machine and to get the necessary information through the Availability API and CDX API. This is where techniques from Week 6: Parsing static web pages will come into play. We will use Beautiful Soup to parse through the different websites and return the list of sponsors or their logos so we can see what is happening. We will potentially have to use skills from Week 8, where we used Playwright or Selenium to look at pages that have JavaScript.

## The scope

I want to target about 10 organizations that I know from exterior research have been in the League of Legends franchise system since 2019: Team Liquid, Cloud9, FlyQuest, G2 Esports, Fnatic, Team Vitality, SK Gaming, T1, Gen.G and Dplus KIA. I will use two captures per organization per year, the first in January–February and the last in November–December, to show the change over time. This will make around 20 captures per year and about 160 captures in total.

## Analysis

I'll code each sponsor into one industry by hand, using categories like crypto/Web3, betting, energy drinks and food, PC hardware and peripherals, telecom and tech, apparel, automotive, finance, and more.

Then I'll produce some graphs like:

- Each industry's share of sponsor slots by year (a stacked bar chart, 2019–2025).
- The number of crypto and betting sponsors per year, by region (line chart).
- Findings: how many sponsors each organization adds and drops each year, and which industries the newly added sponsors come from.

## Terms of service

The CDX and Availability APIs are public APIs that the Internet Archive documents for researchers, and its Terms of Use allow scholarly and research use. I'll collect from the archive, not the live team sites, so I won't put any load on those sites. I'll still note what each team site's own `robots.txt` says, because the archive respects site owners' exclusion requests. To stay within limits, every request will send a User-Agent that identifies me and the class.

## Personal information

Partner pages list companies, not people. Some show player photos or names in banners, so I'll extract only the brand names and logo link domains and discard everything else. The final dataset will have no personal information.

## One record, retrieved

Code (also in [`code/retrieve_one_record.py`](code/retrieve_one_record.py)):

```python
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
```

Result:

```
Request URL: https://web.archive.org/cdx/search/cdx?url=cloud9.gg%2Fpartners&output=json&from=2019&to=2025&collapse=timestamp%3A4&filter=statuscode%3A200&fl=timestamp%2Coriginal%2Cstatuscode%2Cmimetype%2Clength
Status code: 200

Raw response:
[
 ["timestamp", "original", "statuscode", "mimetype", "length"],
 ["20200512035029", "https://cloud9.gg/partners/", "200", "text/html", "12208"],
 ["20210122102619", "https://www.cloud9.gg/partners/", "200", "text/html", "14235"],
 ["20220128032719", "https://cloud9.gg/partners/", "200", "text/html", "16242"],
 ["20230204130650", "https://cloud9.gg/partners/", "200", "text/html", "15289"],
 ["20240204212203", "https://cloud9.gg/partners/", "200", "text/html", "21280"],
 ["20250114224212", "https://cloud9.gg/partners/", "200", "text/html", "23454"]
]

6 captures found:
2020 200 12208 https://web.archive.org/web/20200512035029/https://cloud9.gg/partners/
2021 200 14235 https://web.archive.org/web/20210122102619/https://www.cloud9.gg/partners/
2022 200 16242 https://web.archive.org/web/20220128032719/https://cloud9.gg/partners/
2023 200 15289 https://web.archive.org/web/20230204130650/https://cloud9.gg/partners/
2024 200 21280 https://web.archive.org/web/20240204212203/https://cloud9.gg/partners/
2025 200 23454 https://web.archive.org/web/20250114224212/https://cloud9.gg/partners/
```

## The biggest risk

The biggest risk is that the websites, and specifically the partner pages, are inconsistent or have changed names. URLs sometimes change, and because these esports organizations get title sponsors, they sometimes change their URLs. Additionally, the Wayback Machine sometimes misses a capture, so I will fix these gaps by using a capture as close as possible to the desired dates.

One fallback that could be useful is Liquipedia, an esports wiki, using the Liquipedia MediaWiki Action API to pull the sponsor list for each year.

## AI use

Claude was used to flesh out my idea for this project and identify any gaps in the thought process. All ideas used in this project were my own. Additionally, the code used in the first record was debugged with the help of Claude, using code from previous class notebooks.
