import sys,random

pytania = {
    # 1: "bla",
    # 2: {"a": "gg", "b": "dd"},
}


try:
    with open("quiz.txt", encoding='utf-8') as f:
        for linia in f:
            linia = linia.strip()
            pytanie, a, b, c, d, odp = linia.split(';')
            pytania[pytanie] = {"a":a, "b":b, "c":c, "d":d, "odp":odp}
except FileNotFoundError:
    print('BRAK PLIKU QUIZ!!')

pytania_lista = []
for a in pytania.keys():
    pytania_lista.append(a)

pytanie_nr = 0
uzyte = []
score = 0

while pytanie_nr != 5:
    pytanie_nr += 1
    print('Pytanie nr:', pytanie_nr)
    x = random.choice(pytania_lista)
    if x not in uzyte:
        uzyte.append(x)
        print(f'{x}\n{pytania[x]["a"]}\n{pytania[x]["b"]}\n{pytania[x]["c"]}\n{pytania[x]["d"]}\n')
    else:
        continue

    while True:
        odp = input(">").capitalize()
        if odp not in ["A", "B", "C", "D"]:
            print('bla')
            continue
        if odp == pytania[x]["odp"]:
            score += 1
            break
        break

print(f"wynik: {score}/5")

