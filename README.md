# What actually gets firms fined by the FCA

An analysis of 200 FCA enforcement outcomes published between 2016 and 2026:
what firms and individuals are fined for, how that has changed, and where
control failures concentrate.

## Data
Scraped from the FCA's annual fines pages
(`fca.org.uk/news/news-stories/<year>-fines`), 2016-2026.

## How to run
```
py fetch.py # downloads each year's page into raw/
py parse.py # parses the pages and builds fines.db
py query.py # runs a query against the database
```

## Files
- `fetch.py` - downloads the annual fines pages
- `parse.py` - parses the tables, cleans amounts and dates, loads SQLite
- `query.py` - SQL queries against fines.db
- `DECISIONS.md` - scope decisions and known limitations
- `raw/` - unmodified downloaded pages

## Status
Session 1 complete: data collected and loaded.