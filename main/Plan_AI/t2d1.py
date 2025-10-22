
zdanie = input('Napisz mi zdanie: ')
zdaniesplit = zdanie.split()


znaki = [a for a in zdanie]
slowa = [a.lower() for a in zdaniesplit]
liczba_slow = len(slowa)
liczba_liter = 0
liczba_cyfr = 0
liczba_spacji = 0
znaki_spec = 0
specjalne_znaki2 = set('!@#$%^&*()_+-=[]{};:,.<>?/')


# for a in zdanie:
#     znaki.append(a)

# for a in zdaniesplit:
#     slowa.append(a.lower())

slowa_dict = {}


for a in slowa:
    if a in slowa_dict:
        slowa_dict[a] += 1
    else: 
        slowa_dict[a] = 1


# for a, b in slowa_dict.items():
#     if b == 1:
#         print(f'"{a}"', '->', f'{b} raz')
#     else:
#         print(f'"{a}"', '->', f'{b} razy')

for a, b in slowa_dict.items():
    print(f'"{a}" -> {b} raz{"y" if b > 1 else ""}')


for a in zdanie:
    if a.isalpha():
        liczba_liter += 1
    elif a.isdigit():
        liczba_cyfr += 1
    elif a.isspace():
        liczba_spacji += 1
    else:
        znaki_spec += 1
    

print(f'liczba slow: ', liczba_slow)
print(f'liczba liter: ', liczba_liter)
print(f'liczba cyfr: ', liczba_cyfr)
print(f'liczba spacji: ', liczba_spacji)
print(f'liczba znakow specjalnych: ', znaki_spec)

max_slowo = None
max_ilosc = 0
for a in slowa:
    if slowa_dict[a] > max_ilosc:
        max_ilosc = slowa_dict[a]
        max_slowo = a

print(f'\nTop slowo :{max_slowo}: {max_ilosc} razy')

najdluzsze = None
max_len = 0
for a in slowa:
    if len(a) > max_len:
        max_len = len(a)
        najdluzsze = a

print(f'Najdluzsze slowo: {najdluzsze}: liczba znakow: {max_len}')




