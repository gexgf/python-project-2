import sys
print('--- Ksiazka kontaktow ---')

menu = ('\nMenu:\n'
        '1. Dodaj kontakt\n'
        '2. Pokaz wszystkie kontakty\n'
        '3. Wyszukaj kontakt po imieniu\n'
        '4. Usun kontakt\n'
        '5. Edytuj kontakt\n'
        '6. Zapisz do pliku\n'
        '7. Zakoncz')

kontakty = {}

try:
    with open("C:\gry\QWE.txt", "r") as f:
        for linia in f:
            linia = linia.strip()
            if not linia:
                continue
            imie, telefon, email = linia.split(";")
            kontakty[imie] = {"telefon": telefon, "email": email}
except FileNotFoundError:
    print("Brak pliku z kontaktami - zaczynam od pustej książki.")

while True:
    print(menu)
    email_check = 0
    choose = input('->:')

    if choose == "1":
        while True:
            imie = input('Podaj imie: ').strip()
            if not imie:
                print('- Wpis nie moze byc pusty!!')
                continue
            break

        if imie in kontakty.keys():
            input('Takie imie juz istnieje!! Wcisnij ENTER by kontynuowac\n')
            continue

        while True:
            tel = input('Podaj telefon (ciag 9 liczb): ')
            if len(tel) == 9 and tel.isdigit():
                break
            else:
                print('- Niepoprawny numer!!')

        while email_check == 0:
            email = input('Podaj email: ')
            for a in email:
                if a == "@":
                    email_check += 1
                    break
            if email_check == 0:
                print('Niepoprawny email')

        kontakty[imie] = {'telefon': tel, 'email': email}
        print(f'{imie} - Pomyslnie dodano')

    if choose == "2":
        print('Wszystkie kontakty:\n')
        for a, b in kontakty.items():
            print(f'Imie: {a} - Telefon: {b["telefon"]} - Mail: {b["email"]}')

        if not kontakty.keys():
            print('Pusto tutaj :(')

    if choose == "3":
        search = input('Podaj imie: ')
        if search not in kontakty.keys():
            input('Nie ma takiej osoby na liscie!! Wcisnij ENTER by kontynuowac\n')
            continue
        else:
            for a, b in kontakty.items():
                if a == search:
                    print(f'Znaleziono: ', a,'\nTelefon: ', b['telefon'], '\nMail: ', b['email'])
                    input(f'Wcisnij ENTER by kontynuowac\n')

    if choose == "4":
        usun = input('Usuwamy kontakt\nPodaj imie: ')
        if usun not in kontakty.keys():
            input('Nie ma takiej osoby na liscie!! Wcisnij ENTER by kontynuowac\n')
            continue
        else:
            kontakty.pop(usun)
            print(f'kontakt: ', usun,' :zostal pomyslnie usuniety z listy')
            input('Wcisnij ENTER by kontynuowac\n')

    if choose == "5":
        edit_check = input('Edycja kontaktu, podaj imie: ')
        if edit_check not in kontakty.keys():
            input('Nie ma takiej osoby na liscie!! Wcisnij ENTER by kontynuowac\n')
            continue
        else:
            print(f'Kontakt: {edit_check} :zostal pomyslne zaladowany')
            edit = input(f'Wybierz co edytowac \n1. Imie\n2. Telefon\n3. Email\n->:')
            if edit == "1":
                new_name = input('Podaj nowe imie: ')
                kontakty[new_name] = kontakty.pop(edit_check)
                print('Imie zostalo pomyslnie zmienione!!')
            elif edit == "2":
                while True:
                    new_tel = input('Podaj nowy telefon (ciag 9 liczb): ')
                    if len(new_tel) == 9 and new_tel.isdigit():
                        kontakty[edit_check]["telefon"] = new_tel
                        print('Telefon zostal pomyslnie zmieniony!!')
                        break
                    else:
                        print('- Niepoprawny numer!!')
            elif edit == "3":
                while email_check == 0:
                    new_email = input('Podaj nowy adres email: ')
                    for a in new_email:
                        if a == "@":
                            email_check += 1
                            kontakty[edit_check]["email"] = new_email
                            print('Email zostal pomyslnie zmieniony!!')
                    if email_check == 0:
                        print('- Niepoprawny email!!')
            else:
                input('Niepoprawny wybor!!  Wcisnij ENTER by kontynuowac\n')

    if choose == "6":
        with open("kontakty.txt", 'w') as x:
            for a, b in kontakty.items():
                x.write(f"{a};{b['telefon']};{b['email']}\n")
        print('Pomyslnie zapisano\n')


    if choose == "7":
        print('\nKoniec programu')
        sys.exit()




