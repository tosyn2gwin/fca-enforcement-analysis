from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sqlite3
from datetime import datetime

def clean_amount(text):
    digits = ""
    for ch in text:
        if ch.isdigit() or ch == ".":
            digits = digits + ch
    if digits == "":
        return None
    return float(digits)


def clean_date(text):
    try:
        return datetime.strptime(text, "%d/%m/%Y").date().isoformat()
    except ValueError:
        return None
with open("raw/2025.html", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

tables = soup.find_all("table")
print(len(tables))

table = tables[0]
rows = table.find_all("tr")
print(len(rows))

fines = []

for row in rows:
    cells = row.find_all("td")
    if len(cells) < 4:
        continue

    name = cells[0].get_text(strip=True)
    date = cells[1].get_text(strip=True)
    amount = cells[2].get_text(strip=True)
    reason = cells[3].get_text(strip=True)

    link = cells[0].find("a")
    if link:
        url = urljoin("https://www.fca.org.uk", link["href"])
    else:
        url = ""

    fines.append({
        "name": name,
        "date": date,
        "amount": amount,
        "reason": reason,
        "url": url,
    })

print(len(fines))
print(fines[0])

conn = sqlite3.connect("fines.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS fines")

cur.execute("""
CREATE TABLE fines (
    id INTEGER PRIMARY KEY,
    year INTEGER,
    name TEXT,
    date_raw TEXT,
    date_iso TEXT,
    amount_raw TEXT,
    amount_gbp REAL,
    is_court_fine INTEGER,
    reason TEXT,
    url TEXT
)
""")

for fine in fines:
    amount_gbp = clean_amount(fine["amount"])
    date_iso = clean_date(fine["date"])
    is_court_fine = 1 if "court fine" in fine["amount"].lower() else 0

    cur.execute(
        "INSERT INTO fines (year, name, date_raw, date_iso, amount_raw, amount_gbp, is_court_fine, reason, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (2025, fine["name"], fine["date"], date_iso, fine["amount"], amount_gbp, is_court_fine, fine["reason"], fine["url"])
    )
conn.commit()
conn.close()

print("Saved to fines.db")