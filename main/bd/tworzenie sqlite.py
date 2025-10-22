import sqlite3

# Otwórz plik .db
conn = sqlite3.connect("moja_baza.db")
cursor = conn.cursor()

# Zobacz listę tabel w bazie
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabele = cursor.fetchall()
print("Tabele w bazie:", tabele)

# Pobierz dane z jednej tabeli (np. 'users')
cursor.execute("SELECT * FROM produkty")
dane = cursor.fetchall()
# for wiersz in dane:
#     print(wiersz)
print(dane)

conn.close()