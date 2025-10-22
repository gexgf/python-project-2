print('*****# Twoj bank ABC #*****')


acc_name = '12'
acc_password = '34'
login_check = True
bank_acc = 5000
history = []
while True:

    while login_check:
        a = input('Login: ')
        b = input('Password: ')
        if a == acc_name and b == acc_password:
            print('Prawidlowe logowanie')
            login_check = False
            break
        else:
            print('Nieprawidlowe logowanie, sprobuj ponownie')

#print(type(bank_acc))

    print('...')
    print('Menu glowne:')
    print('1: Sprawdz aktualne saldo \n'
            '2: Dodaj do konta \n'
            '3: Wyplac z konta \n'
            '4: Historia tranzakcji \n'
            '5: Wyloguj')
    a = input('-> ')
    if a == '1':
        print(f'Twoje aktualne saldo wynosi: {bank_acc}')
    elif a == '2':
        print('Podaj kwote: ')
        add = int(input('-> '))
        bank_acc += add
        history.append(f'+{add}')
        print(f'Kwota {add} zostala dodana pomyslnie do twojego konta')
    elif a == '3':
        print(f'Podaj kwote do wyplacenia: ')
        out = int(input('-> '))
        if out > bank_acc:
            print('!!Operacja NIEUDANA!!, kwota wyplaty PRZEKRACZA calkowite saldo konta bankowego')
        else:
            bank_acc -= out
            history.append(f'-{out}')
            print(f'Kwota  {out} zostala pomyslnie wyplacona')
    elif a == '4':
        if history == []:
            print('Pusciutko, brak danych :(')
        else:
            for a1 in history:
                print(a1)
            #print(f'{history}')
    elif a == "5":
        print('Wylogowano')
        login_check = True
        print('..')


