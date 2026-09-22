import requests

url = "https://www.fca.org.uk/news/news-stories/2025-fines"
headers = {"User-Agent": "Mozilla/5.0 (FCA fines research project)"}

response = requests.get(url, headers=headers)

print(response.status_code)

print(len(response.text))

with open("raw/2025.html", "w", encoding="utf-8") as f:
    f.write(response.text)