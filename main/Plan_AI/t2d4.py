import random,sys

lista_slow = ["python", "kot", "samochód", "programowanie"]

do_zgadniecia = random.choice(lista_slow)
word = []
used = []
hp = 6

for a in do_zgadniecia:
    word.append('_')

print('Zgaduj!!\n', '_ '* len(do_zgadniecia))

while True:
    zgadula = input('->:')
    if len(zgadula) > 1:
        print('TYLKO JEDNA LITERKA!!')
        continue

    if zgadula not in used:
        used.append(zgadula)
    else:
        print(f'Ta literka juz byla uzyta!!\n{used}')
        continue

    if zgadula not in do_zgadniecia:
        hp -= 1
        if hp == 0:
            print(f'PUDLO! HP:{hp}/6\nPRZEGRALES!! KONIEC GRY')
            sys.exit()
        print(f'PUDLO! Tracisz zycie HP:{hp}/6\nuzyte litery: {used}')
        print(*word)
        continue
    else:
        for a, b in enumerate(do_zgadniecia):
            if zgadula == b:
                word[a] = zgadula
        print(*word)
        if ''.join(word) == do_zgadniecia:
            print(f"YOU WIN - SLOWO TO :{do_zgadniecia}:")
            sys.exit()



