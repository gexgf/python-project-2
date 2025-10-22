

znak_check = True

while znak_check:
    znak = input('Podaj znak dziala (+, -, * lub / ): ')
    if znak in ('+', '-', '*', '/'):
        print(f"Twoj znak dzialania to '{znak}'")
        znak_check = False
    else:
        print(f'Twoj znak dzialania "{znak}" jest nie wlasciwy, podaj jeszcze raz')


a = float(input('Podaj 1st liczbe: '))
b = float(input('Podaj 2nd liczbe: '))





def licz(znak, a, b):
    if znak == "+":
        print(f'Wynik to', round(a+b, 2))
    elif znak == "-":
        print(f'Wynik to', round(a - b, 2))
    elif znak == "*":
        print(f'Wynik to', round(a * b, 2))
    elif znak == "/":
        print(f'Wynik to', round(a / b, 2))


licz(znak, a, b)


# if znak == "+":
#     licz(znak, a, b)
# elif znak == "-":
#     licz(znak, a, b)
# elif znak == "*":
#     licz(znak, a, b)
# elif znak == "/":
#     licz(znak, a, b)
# else:
#     print(f'{znak} jest nie wlasciwy')