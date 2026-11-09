# Data

| Path | In repo? | Contents |
| --- | --- | --- |
| `sample/sponsors_sample.csv` | Yes | 60 random rows of the clean dataset |
| `sample/captures.csv` | Yes | Every organization × year × period, with the capture used (or `missing`) |
| `industry_codes.csv` | Yes | Hand-coded industry for each sponsor |
| `brand_aliases.csv` | Yes | Hand-made merges of sponsor spellings |
| `data_dictionary.md` | Yes | What every field means |
| `raw/` | No | CDX API responses and archived HTML pages |
| `interim/` | No | Candidate pages and raw sponsor mentions |
| `clean/` | No | Full clean dataset (`sponsors_clean.csv`, `captures.csv`) |

Run `collect_and_clean.ipynb` to rebuild everything that isn't in the repository.
