import sqlite3

conn = sqlite3.connect("fines.db")
cur = conn.cursor()

cur.execute("""
SELECT name, amount_gbp, date_iso
FROM fines
ORDER BY amount_gbp DESC
LIMIT 10
""")

for row in cur.fetchall():
    print(row)

conn.close()