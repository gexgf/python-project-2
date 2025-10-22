import random

print('Zgadnij cyfre od 1 do 100')
liczba = random.randint(1, 100)
live = 10


while live > 0:
    print(f'Prob: {live} / 10')
    try:

        zgadula = int(input('->:'))

        if zgadula > liczba:
            print('Za duzo!')
            live -= 1
            continue
        elif zgadula < liczba:
            print('Za malo')
            live -= 1
            continue
        else:
            print('DANG YO')
            break
    except ValueError:
        print('TYLKO CYFRY')
        live -= 1
    


if live == 0:
    print(f'Prob: {live} / 10')
    print('Przegrales !!')
else:
    print('!!WYGRALES!!')