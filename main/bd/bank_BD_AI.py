import pandas as pd

# ID pliku z Google Sheets (przykład)
file_id = "1iI8xuBdl4Ro_8ewssr62c46urvBnQK9ETyj4XlOTSp0"
sheet_gid = "0"
csv_url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv&gid={sheet_gid}"

# Wczytaj dane z arkusza
df = pd.read_csv(csv_url)
df.columns = df.columns.str.strip()  # usuń spacje z nagłówków

print('*****# Twoj bank ABC #*****')

login_check = True
bank_acc = 0
history = []

while True:
    while login_check:
        a = input('Login: ')
        b = input('Password: ')

        # Sprawdzenie czy konto istnieje w danych z arkusza
        row = df[(df["Login"] == a) & (df["Password"] == b)]
        if not row.empty:
            print('Prawidlowe logowanie')
            # print(f'Witaj {df[df["Nazwisko"]]}')
            print(f'Witaj {str(row.iloc[0]["Nazwisko"])} {str(row.iloc[0]["Imie"])}')
            login_check = False
            bank_acc = int(row.iloc[0]["Saldo"])  # ustaw saldo z arkusza
            break
        else:
            print('Nieprawidlowe logowanie, sprobuj ponownie')

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
            print('!!Operacja NIEUDANA!!, kwota wyplaty PRZEKRACZA saldo konta')
        else:
            bank_acc -= out
            history.append(f'-{out}')
            print(f'Kwota  {out} zostala pomyslnie wyplacona')
    elif a == '4':
        if history == []:
            print('Brak historii transakcji')
        else:
            for a1 in history:
                print(a1)
    elif a == "5":
        print('Wylogowano')
        login_check = True
        print('..')
