from bs4 import BeautifulSoup
from urllib.parse import urljoin

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