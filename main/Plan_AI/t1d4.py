

name = input('Podaj imie: ').strip()
liczba = float(input('Podaj ulubiona liczbe: ').strip())

print(f'{name}, masz oko do liczb' if int(liczba) % 2 == 0 else f'{name}, nie boisz się wyzwań!' )