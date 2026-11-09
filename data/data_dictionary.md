# Data dictionary

All files are produced by [`collect_and_clean.ipynb`](../collect_and_clean.ipynb). The repository holds only `data/sample/` and the two hand-edited files (`industry_codes.csv`, `brand_aliases.csv`).

## `sponsors_clean.csv` (sample: `sample/sponsors_sample.csv`)

One row per **organization × year × period × sponsor**: a sponsor shown on an organization's partner page in one archived capture.

| Field | Type | Meaning |
| --- | --- | --- |
| `org` | text | Organization: Team Liquid, Cloud9, FlyQuest, G2 Esports, Fnatic, Team Vitality, SK Gaming, T1, Gen.G or Dplus KIA |
| `region` | text | Region where the organization's League team competes: North America, Europe or Korea |
| `year` | integer | Calendar year of the capture, 2019–2026 |
| `period` | text | `early` (capture from January–February, or March–May if none) or `late` (November–December, or August–October if none) |
| `capture_date` | date | Date the Wayback Machine archived the page (YYYY-MM-DD) |
| `sponsor_key` | text | Normalized sponsor identifier: lowercase letters and digits only (`redbull`). Used to match the same sponsor across pages |
| `sponsor_name` | text | Readable sponsor name, taken from the logo's alt text, `brand_aliases.csv`, or the sponsor's web domain |
| `sponsor_domain` | text | Website the sponsor's logo linked to (`redbull.com`). Blank when the logo had no link |
| `industry` | text | Hand-coded industry from `industry_codes.csv` (categories below). `uncoded` = not coded yet |
| `mention_types` | text | How the sponsor was found: `link` (link to the sponsor's site), `image` (logo in a partner section without a link), or both |
| `n_mentions` | integer | Number of times the sponsor appeared on that page before duplicates were removed |
| `snapshot_url` | text | Wayback Machine address of the capture, to check the row by eye |

## `captures.csv` (in `sample/`, full file)

One row per **organization × year × period**, including periods with no capture, so gaps are visible.

| Field | Type | Meaning |
| --- | --- | --- |
| `org`, `region`, `year`, `period` | | As above |
| `status` | text | `selected` (a capture was found) or `missing` (none in the allowed months) |
| `capture_date` | date | Date of the selected capture |
| `timestamp` | text | Wayback timestamp of the capture (YYYYMMDDhhmmss) |
| `page_url` | text | Original address of the archived partner page |
| `in_target_window` | true/false | `true` if the capture is from the target months (Jan–Feb or Nov–Dec); `false` if a fallback month was used |
| `days_from_target` | integer | Days between the capture and the target date (January 1 for early, December 31 for late) |
| `download` | text | `downloaded`, `cached` (already on disk) or `failed (status)` |
| `n_mentions` | integer | Raw sponsor mentions parsed from the page. `0` usually means the page was built with JavaScript |
| `n_sponsors` | integer | Sponsors in the clean dataset for this capture |
| `snapshot_url` | text | Wayback Machine address of the capture |

## `industry_codes.csv` (hand-coded)

One row per sponsor. The notebook adds new sponsors with a blank `industry`; I fill these in by hand.

| Field | Meaning |
| --- | --- |
| `sponsor_key`, `sponsor_name`, `sponsor_domain` | As above |
| `industry` | One of: `crypto_web3`, `betting` (including prediction markets), `energy_drink_food`, `pc_hardware_peripherals`, `telecom_tech`, `apparel`, `automotive`, `finance`, `other`, `not_a_sponsor` (removed from the clean data) |
| `notes` | Why a code was chosen, when it isn't obvious |

## `brand_aliases.csv` (hand-edited)

Merges different spellings of one sponsor.

| Field | Meaning |
| --- | --- |
| `raw_key` | Key as produced from a page (`redbullgaming`) |
| `sponsor_key` | Key to merge it into (`redbull`) |
| `sponsor_name` | Display name to use (`Red Bull`) |
