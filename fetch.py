import requests

headers = {"User-Agent": "Mozilla/5.0 (FCA fines research project)"}

import time

for year in range(2016, 2027):
    url = f"https://www.fca.org.uk/news/news-stories/{year}-fines"
    response = requests.get(url, headers=headers)
    print(year, response.status_code, len(response.text))

    with open(f"raw/{year}.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    time.sleep(1)