
print('Witaj w Walidator hasla. \nHaslo musi zawierac: \n1. min. 8 znakow \n2. minimum 1 duza litere \n3. minimum 1 mala litere \n4. minimum 1 cyfre \n5. minimum 1 znak specjalny')

specjalne_znaki2 = set('!@#$%^&*()_+-=[]{};:,.<>?/')

def check_power(a):
    if len(a) < 11:
        print(f'Haslo zawiera {len(a)} znakow, sila hasla: slaba')
    elif len(a) < 16:
        print(f'Haslo zawiera {len(a)} znakow, sila hasla: srednia')
    else:
        print(f'Haslo zawiera {len(a)} znakow, sila hasla: silna ')



while True:
    main = 0
    duze_znaki = 0
    male_znaki = 0
    cyfry = 0
    znaki_spec = 0
    bledy = []


    password = input('Podaj haslo: ').strip()

    if len(password) <= 7:
        print('Za MALO znakow, sprobuj ponownie')
        continue

    for x in password:
        if x.isupper():
            duze_znaki += 1
        if x.islower():
            male_znaki += 1
        if x.isdigit():
            cyfry += 1
        if x in specjalne_znaki2:
            znaki_spec += 1
    
    if duze_znaki == 0:
        bledy.append('Minium 1 DUZA litera')
    else:
        main += 1

    if male_znaki == 0:
        bledy.append('Minium 1 MALA litera')
    else:
        main += 1

    if cyfry == 0:
        bledy.append('Minium 1 CYFRA')
    else:
        main += 1

    if znaki_spec == 0:
        bledy.append('Minium 1 ZNAK specjalny')
    else:
        main += 1
    
    if main == 4:
        break
    else:
        print('Haslo nie spelnia wymagan takich jak: ')
        for y in bledy:
            print(f'{y}')
        print('Sprobuj ponownie')


print(f'Super, udalo sie zrobic haslo: {password}')

check_power(password)
        
