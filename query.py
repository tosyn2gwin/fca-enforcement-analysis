import sqlite3

conn = sqlite3.connect("fines.db")
cur = conn.cursor()

cur.execute("""
SELECT year, name, date_raw, amount_raw
FROM fines
WHERE amount_gbp IS NULL OR date_iso IS NULL
""")

for row in cur.fetchall():
    print(row)

conn.close()