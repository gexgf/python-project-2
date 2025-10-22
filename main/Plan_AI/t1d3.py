

def get_number(a):
    while True:
        try:
            return float(input(a).strip().replace(",", "."))
        except ValueError:
            print('TYLKO liczby, sprobuj ponownie')

def liczenie(a,b):
    operacje = {
        'Dodawanie': lambda x, y: a + b,
        'Odejmowanie': lambda x, y: a - b,
        'Mnozenie': lambda x, y: a * b,
        'Dzielenie': lambda x, y: a / b,
        'Dzielenie calkowite': lambda x, y: a // b,
        'Reszta z dzielenia': lambda x, y: a % b,
        'Potegowanie': lambda x, y: a ** b,
    }
    for name, blast in operacje.items():
        try:
            print(f'{name}: {a} i {b} = {blast(a,b):.2f}')
        except ZeroDivisionError:
            print(f'{name}: Blad, nie dzielimy przez 0')




x = get_number('Prosze podac liczbe nr1: ')
y = get_number('Prosze podac liczbe nr2: ')

liczenie(x,y)