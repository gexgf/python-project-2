# with open("kontakty.txt", "r") as f:
#         for linia in f:
#             linia = linia.strip()
#             if not linia:
#                 continue
#             imie, telefon, email = linia.split(";")
#             kontakty[imie] = {"telefon": telefon, "email": email}


lista = ["BOB;123123123;@jfgriejtir@", "Ela;123123123;eweawewa@", "BOBUS;435456432;gprotp@"]

for a in lista:
    a = a.strip()
    imie, telefon, email = a.split(";")


# imie, telefon, email = lista.split(";")

print(imie)
print(telefon)
print(email)


