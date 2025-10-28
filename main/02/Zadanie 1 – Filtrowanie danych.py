def filtruj_parzyste(a):
    new = []
    try:
        for i in a:
            if i % 2 == 0:
                new.append(int(i))
        print(new)
    except TypeError:
        print('Tylko liczby calkowite')


b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22.2, 24]

filtruj_parzyste(b)
