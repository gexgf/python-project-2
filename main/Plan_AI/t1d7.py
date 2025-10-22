

print('Witaj w Twojej liscie zakupow')
menu = ('Menu: \n'
        '1. Pokaz liste \n'
        '2. Dodaj do listy \n'
        '3. Usun z listy \n'
        '4. Zamiana produktu na inny po numerze \n'
        '5. Zakoncz \n'
)
print(menu)
zakupy = []
empty = ('W tej chwili twoja lista jest pusta!!')


def show_list(a):
    for nr, name in enumerate(a):
        print(f'{nr+1}. {name}')



def choose(a):
    if a == '1':
        print('--------- Twoja Lista --------- ')
        if not zakupy:
            print(empty)
            return
        show_list(zakupy)
        print('')

    elif a == '2':
        dodaj = input('Co dodajemy?\n->:')
        if not dodaj:
            print('Nie mozna dodac pustej nazwy!! Wcisnij by kontynuowac ...')
            input('')
            return
        if dodaj in zakupy:
            print(f'{dodaj} juz wystepuje na liscie, wcisnij by kontynuowac ...')
            input('')
            return
        zakupy.append(dodaj) 
        print(f'"{dodaj}" pomyslnie dodano do listy')
        show_list(zakupy)

    elif a == '3':
        if not zakupy:
            print(empty)
            return
        show_list(zakupy)
        try:
            usun = int(input('ktory numer usuwamy z listy? \n->:')) -1
            print(zakupy.pop(usun) + ' :usuwam')
        except ValueError:
            print('Blad! tylko NUMER z listy, wcisnij by kontynuowac ...')
            input('')
            return
        except IndexError:
            print(f'Blad! numer {usun} nie ma na liscie!! Wcisnij by kontynuowac ...')
            input('')
            return

    elif a == '4':
        if not zakupy:
            print(empty)
            return
        show_list(zakupy)
        try:
            zamiana_index = int(input('Ktory numer zamieniamy?\n->:')) -1
            if zamiana_index + 1 > len(zakupy):
                print(f'Blad! numer {zamiana_index +1} nie ma na liscie!! Wcisnij by kontynuowac ...')
                input('')
                return
        except ValueError:
            print('Blad! tylko NUMER z listy, wcisnij by kontynuowac ...')
            input('')
            return
        zamiana_item = input('Na co zamieniamy\n->:')
        if zamiana_item in zakupy:
            print(f'{zamiana_item} juz wystepuje na liscie, wcisnij by kontynuowac ...')
            input('')
            return
        zakupy.pop(zamiana_index)
        zakupy.insert(zamiana_index , zamiana_item)
        print('Pomyslnie dodano: ', zamiana_item)
        
    elif a == '5':
        print('\n!!Koniec programu!! \n')
    else:
        print(' zly wybor')
    



while True:
    

    x = input('->:')
    print('---')

    if not x:
        print('PUSTE POLE!! Sprobuj ponownie')
        continue
    
    choose(x)

    if x == '5':
        break


    print('---')
    print(menu)
    print(*zakupy, sep=', ')
