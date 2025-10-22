import string

text = []
text_slow = []
liczba_linii = 0
liczba_liter = 0
liczba_cyfr = 0
liczba_spacji = 0
znaki_spec = 0

try:
    with open(r'/main/Plan_AI/tekst.txt', encoding='utf-8') as bla:
        for a in bla:
            text.append(a.strip())
        bla.seek(0)
        file = bla.read()
except FileNotFoundError:
    print('BRAK PLIKU!!')


for a in file.split():
    a = a.strip(string.punctuation).lower()
    if a.isalpha():
        text_slow.append(a)

for a in text:
    liczba_linii += 1
    for b in a:
        if b.isalpha():
            liczba_liter += 1
        elif b.isdigit():
            liczba_cyfr += 1
        elif b.isspace():
            liczba_spacji += 1
        else:
            znaki_spec += 1


dict_slow = {}

for a in text_slow:
    if a in dict_slow:
        dict_slow[a] += 1
    else:
        dict_slow[a] = 1

slowo_max = None
slowo_max_nr = 0
czesto = 0
czesto_slowo = None

for a, b in dict_slow.items():
    if len(a) > slowo_max_nr:
        slowo_max_nr = len(a)
        slowo_max = a
    if b > czesto:
        czesto = b
        czesto_slowo = a

sortowanie = sorted(dict_slow.items(), key=lambda x: x[1], reverse=True)


print(f'Liczba linii:', liczba_linii)
print('liczba liter:',liczba_liter)
print('liczba cyfr:',liczba_cyfr)
print('liczba spacji:',liczba_spacji)
print('znaki specjalne:',znaki_spec)
print('liczba slow:', len(text_slow))
print(f'Najdluzsze slowo: {slowo_max}\nliczba znakow: {slowo_max_nr}')
print(f'Najczejsciej wystepujace slowo: {czesto_slowo}\nliczba powtorzen: {czesto}')
print('TOP5 slow:')
for a, b in sortowanie[:5]:
    print(f'{a}:{b}')
