

def get_int(a):
    while True:
        try:
            return int(input(a).strip())
        except ValueError: print('Blad, sprobuj ponownie')


def get_str(a):
    while True:
        s = input(a).strip()
        if s:
            return s
        print('Tekst nie moze byc pusty')

def get_float(a):
    while True:
        try:
            return float(input(a).strip().replace(',','.'))
        except ValueError:
            print('Blad, sprobuj ponownie')



liczba = get_int('Podaj liczbe calkowita: ')
tekst = get_str('Podaj tekst: ')
liczba_z_przecinkiem = get_float('Podaj liczbe z przecinkiem: ')


print(f'int: {liczba} | float: {liczba_z_przecinkiem:.2f} | str: {tekst}')