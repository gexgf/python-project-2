zdanie = input('Napisz mi zdanie: ')
slowa = [s.lower() for s in zdanie.split()]

# słownik słów
slowa_dict = {}
for s in slowa:
    slowa_dict[s] = slowa_dict.get(s, 0) + 1

# wypisanie ile razy każde słowo
for s, count in slowa_dict.items():
    print(f'"{s}" -> {count} raz{"y" if count > 1 else ""}')

# znajdź najczęściej używane słowo (z uwzględnieniem kolejności)
najczestsze = None
naj_wystapien = 0
for s in slowa:  # ważne: iterujemy po oryginalnej liście slowa, nie po dict!
    if slowa_dict[s] > naj_wystapien:
        naj_wystapien = slowa_dict[s]
        najczestsze = s

print(f'\nNajczęściej używane słowo: "{najczestsze}" -> {naj_wystapien} razy')

# liczenie znaków
litery = cyfry = spacje = specjalne = 0
for z in zdanie:
    if z.isalpha():
        litery += 1
    elif z.isdigit():
        cyfry += 1
    elif z.isspace():
        spacje += 1
    else:
        specjalne += 1

print("\nStatystyki:")
print("liczba słów:", len(slowa))
print("liczba liter:", litery)
print("liczba cyfr:", cyfry)
print("liczba spacji:", spacje)
print("liczba znaków specjalnych:", specjalne)
