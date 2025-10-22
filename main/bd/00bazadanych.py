import sqlite3
conn = sqlite3.connect("moja_baza.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS produkty (id INTEGER PRIMARY KEY, nazwa TEXT)")
cursor.execute("INSERT INTO produkty (nazwa) VALUES (?)", ("Chleb",))
conn.commit()
conn.close()
