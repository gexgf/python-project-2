import sys

kursy = {
    "PLN": 1,
    "USD": 3.67,
    "EUR": 4.27,
    "GBP": 4.96,
}

x = []

for a in kursy.keys():
    x.append(a)

def licz(kwota, zrodlowa, docelowa):
    x = kwota * zrodlowa
    wynik = x / docelowa
    return print(round(wynik, 2))




while True:
    try:
        kwota = float(input('Podaj kwote: '))
    except ValueError:
        print('Niepoprwana kwota')
        continue
        
    while True:
        waluta_zrodlowa = input(f'Podaj walute zrodlowa {x}: ')
        if waluta_zrodlowa in x:
            break
        else:
            print('Niepoprawna waluta')
          
    while True:  
        waluta_docelowa = input(f'Podaj walute docelowa {x}: ')
        if waluta_docelowa in x:
            break
        else:
            print('Niepoprawna waluta')

    licz(kwota, kursy[waluta_zrodlowa], kursy[waluta_docelowa])

    ask = input('Kontynuowac? (q = wyjście): ENTER')
    if ask == "q":
        sys.exit()


            
    


