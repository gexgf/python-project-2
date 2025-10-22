
uczniowie = {}

try:
    with open('oceny.csv', encoding='utf-8') as file:
        x = file.read().splitlines()
except FileNotFoundError:
    print('BRAK PLIKU !!')

for a in x:
    id, imie, nazwisko, oceny = a.split(';')
    uczniowie[id] = {'imie':imie, 'nazwisko':nazwisko, 'oceny':oceny}

print(uczniowie)
