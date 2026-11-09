# Who Pays the Teams? Sponsorship in League of Legends Esports, 2019–2026

**Michael Chow**

## Research question

Which industries sponsored top League of Legends organizations from 2019 to 2026, and which categories were most prominent over time? Sponsorship is the main source of revenue for most esports teams, so who pays them shapes what they can do. Using archived copies of the "Partners" and "Sponsors" pages of 10 long-running franchise organizations (Team Liquid, Cloud9, FlyQuest, G2 Esports, Fnatic, Team Vitality, SK Gaming, T1, Gen.G and Dplus KIA) from the Internet Archive's Wayback Machine, I will code every sponsor by industry and track how the mix changed. I expect energy drink and hardware brands early on, a crypto and Web3 surge in 2021–2022, a drop after the FTX crash, and a rise in betting and prediction market sponsors from late 2024. Full details are in [`proposal.md`](proposal.md).

## Data

**Source.** Archived copies of each organization's partner or sponsor page in the [Internet Archive's Wayback Machine](https://web.archive.org/). I found the pages and their captures with the [Wayback CDX API](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) and downloaded each selected capture in its original archived form (`/web/<timestamp>id_/<url>`). The team websites themselves were never contacted.

**Collection.** I ran [`collect_and_clean.ipynb`](collect_and_clean.ipynb) on **November 8, 2026**, making **266** requests (154 CDX searches and 112 page downloads). Every request sent a User-Agent naming the project with a contact address, waited at least 5 seconds after the previous one, backed off on errors, and was cached so nothing was downloaded twice.

**Records.**

| | Count |
| --- | --- |
| Organizations with at least one capture | 9 of 10 (none found for Dplus KIA) |
| Captures selected (2 per organization per year, 2019–2026) | 112 of 160 (48 missing) |
| Captures from the target months (Jan–Feb, Nov–Dec) | 81 |
| Raw sponsor mentions parsed | 2,053 |
| Clean rows (organization × year × period × sponsor) | 1,007 |
| Distinct sponsors | 240 |

**Cleaning.** Sponsor names come from logo link domains (`redbull.com` → `redbull`) or logo alt text. Spellings are merged with [`data/brand_aliases.csv`](data/brand_aliases.csv), duplicates on a page are counted once, and each sponsor is hand-coded into an industry in [`data/industry_codes.csv`](data/industry_codes.csv). Links that aren't sponsors (ticket sites, news articles) are coded `not_a_sponsor` and removed. Every field is described in [`data/data_dictionary.md`](data/data_dictionary.md).

**In this repository:** a 60-row sample of the clean dataset ([`data/sample/sponsors_sample.csv`](data/sample/sponsors_sample.csv)), the list of every capture used ([`data/sample/captures.csv`](data/sample/captures.csv)), and the hand-coding files.

**Left out, and why:**
- **Archived HTML pages (`data/raw/html/`).** The pages are the teams' copyrighted website content, served by the Internet Archive for viewing and research, not for redistribution. They are also large. Anyone can view each page through the `snapshot_url` in the data.
- **Raw CDX responses and parsed mentions (`data/raw/cdx/`, `data/interim/`).** These are intermediate files that the notebook rebuilds. Some pages include player names and photos in banners, and only brand names are kept.
- **The full clean dataset (`data/clean/`).** The assignment asks for a sample. The notebook rebuilds the full file in seconds from its cache, or in about 20–30 minutes from scratch.

## Methods

*To come.*

## Findings

*To come.*

## How to reproduce

```bash
pip install -r requirements.txt
jupyter notebook collect_and_clean.ipynb   # run all cells from the repository folder
```

A first run takes about 20–30 minutes because of the 5-second pause between requests. To rerun the original test request: `python3 code/retrieve_one_record.py`.

## Repository contents

| Path | What it is |
| --- | --- |
| `proposal.md` | Project proposal |
| `collect_and_clean.ipynb` | Collection and cleaning notebook |
| `analysis.ipynb` | Analysis notebook (placeholder) |
| `report.md` | Final write-up (placeholder) |
| `code/` | Test CDX request from the proposal |
| `data/` | Data sample, hand-coding files and data dictionary |
| `requirements.txt` | Python packages needed |
