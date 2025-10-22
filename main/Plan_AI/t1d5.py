

def get_number(a):
    while True:
        try:
            return float(input(a).strip().replace(',','.'))
        except ValueError: print('Wymagana liczba, sprobuj ponownie!')


operacje = ('+', '-', '*', '/')


# def licz(a, b, c):
#     if a == "+":
#         return round(b+c, 2)
#     elif a == "-":
#         return round(b-c, 2)
#     elif a == "*":
#         return round(b*c, 2)
#     elif a == "/":
#         return round(b/c, 2)
    

def licz2(a,b,c):
    dzialania = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y, 
    }
    return round(dzialania[a](b, c), 2)




liczba1 = get_number('Podaj liczbe nr1: ')
a = 0

while a == 0:

    while True:
        znak = input('Podaj znak operacji +, -, * lub / : ')
        if znak in operacje:
            break
        else:
            print('Niepoprawna operacja, sprobuj ponownie')


    liczba2 = get_number('Podaj liczbe nr2: ')

    # if znak == "/" and liczba2 == float("0.0"):
    #     print('Nie dzielimy przez 0, sprobuj ponownie')
    #     continue

    try:
        c = licz2(znak, liczba1, liczba2)
    except ZeroDivisionError:
        print('Nie dzielimy przez 0, sprobuj ponownie')
        continue
    
    
    print(c)


    while True:
        check1 = input('Czy chcesz użyć wyniku jako pierwszej liczby w kolejnym działaniu?  Y/N: ')
        if check1 in ('Y', 'y', 'tak', 'yes'):
            liczba1 = c
            break
        elif check1 == "N":
            print("Koniec zadania")
            a += 1
            break
        else:
            print('Zla komenda, sprobuj ponownie')

