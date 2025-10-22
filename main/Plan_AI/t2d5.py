import sys

zadania = {}


try:
    with open('todo.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: # ??
                print('bla') # ??
            ID, todo, status = line.split(";")
            zadania[int(ID)] = {"todo": todo,"status": status}
except FileNotFoundError:
    print('BRAK PLIKU !!')



def show_all():
    for a, b in zadania.items():
        print(f'#{a} {b["todo"]} {b["status"]}')


def dalej():
    x = input('Kontynuuj (ENTER) ... ▶️ ')


while True:
    print('MENU:\n'
          '1. Dodaj nowe zadanie\n'
          '2. Wyswietl zadania\n'
          '3. Zmiana statusu\n'
          '4. Zapisz\n'
          '5. Reset listy\n'
          '6. Edytuj\n'
          '7. Zakoncz'
)
    wybor = input('->:')

    if wybor == "1":
        dodaj = input('Podaj zadanie: ')
        numerek = 0
        for a in zadania.keys():
            numerek += 1
        if dodaj not in zadania:
            zadania[numerek+1] = {"todo": dodaj,"status": "❌"}
            print('Dodano👍')

    if wybor == "2":
        print('Zadania:')
        show_all()
        dalej()

    if wybor == "3":
        show_all()
        try:
            done = int(input('Podaj nr zadania: '))
            if done not in zadania.keys():
                print('Nie ma takiego zadania')
                dalej()
                continue
            else:
                for a, b in zadania.items():
                    if done == a and b["status"] == "✔":
                        zadania[a]["status"] = "❌"
                        print('Zmieniono status na ❌')
                        dalej()
                        continue
                    if done == a:
                        zadania[a]["status"] = "✔"
                        print('Zmieniono status na ✔')
                        dalej()
        except ValueError:
            print('TYLKO CYFRY!!')
            dalej()
            continue

    if wybor == "4":
        with open("todo.txt", "w", encoding='utf-8') as Q:
            for a, b in zadania.items():
                Q.write(f'{a};{b["todo"]};{b["status"]}\n')
        print('Zapisano👍')

    if wybor == "5":
        reset = input("Potwierdz RESET listy (TAK/NIE): ")
        if reset == 'TAK':
            zadania.clear()
            print('Pomyslnie zresetowano liste👍')
            dalej()
        else:
            print('Anulowano')
            dalej()
            continue

    if wybor == "6":
        show_all()
        edit_id = int(input('Ktory nr zadania chcesz edytowac?: '))
        if edit_id not in zadania.keys():
            print('Nie ma takiego zadania')
            dalej()
            continue
        else:
            edit_txt = input('Podaj zadanie: ')
            for a, b in zadania.items():
                if a == edit_id:
                    zadania[a]["todo"] = edit_txt
                    print('Zapisano👍')
                    dalej()
                    continue


    if wybor == "7":
        print('\nKONIEC PROGRAMU\n')
        sys.exit()




    # print(zadania)




# for a, b in zadania.items():
#     print(a, b["status"])