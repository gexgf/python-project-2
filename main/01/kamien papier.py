
win_1 = 0
win_2 = 0

print("Gra kamien/papier/nozyczki do 3")
opcje = ['kamien', 'papier', 'nozyczki']

def choose(gracz):
    while True:
        abc = input(f"{gracz} wybiera: ")
        if abc in opcje:
            return abc

def check(a,b):
    if gracz_1 == "papier" and gracz_2 == 'kamien' \
    or gracz_1 == "kamien" and gracz_2 == 'nozyczki' \
    or gracz_1 == "nozyczki" and gracz_2 == 'papier':
        print('Gracz 1 zdobywa punkt:')
        return 1
    elif gracz_1 == gracz_2:
        print('REMIS')
        return 0
    else:
        print("Gracz 2 zdobywa punkt:")
        return -1



while win_1 != 3 and win_2 != 3:

    gracz_1 = choose('Gracz1')
    gracz_2 = choose('Gracz2')
    wynik = check(gracz_1, gracz_2)

    if wynik == 1:
        win_1 += 1
    elif wynik == -1:
        win_2 += 1

if win_1 > win_2:
    print(' Gre wygrywa Gracz1')
else:
    print(' Gre wygrywa Gracz2')


print('Koniec gry')



