def czysc(a):
    czyste_ubranie = a.replace('brudne', 'czyste')
    czyste_ubranie = czyste_ubranie.replace('brudna', 'czysta')
    return czyste_ubranie


def pralka(*args, proszek):
    print(args)
    print(proszek)
    czyste_ubrania = []
    for b in args:
        czyste_ubrania.append(czysc(b))
    return czyste_ubrania


brudne_giry = [
    'brudne gacie',
    'brudne skarpety',
    'brudna koszula',
]

wynik = pralka(*brudne_giry, proszek=('od chajzera'))

print(wynik)

