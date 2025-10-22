import string
from collections import Counter

try:
    with open(r'/main/Plan_AI/tekst.txt', encoding='utf-8') as f:
        file = f.read()
except FileNotFoundError:
    print('BRAK PLIKU!!')
    exit()

linie = file.splitlines()

slowa = [s.strip(string.punctuation).lower() for s in file.split()]
slowa = [s for s in slowa if s.isalpha()]
# print(slowa)


liczba_linii = len(linie)
liczba_liter = sum(ch.isalpha() for ch in file)
liczba_cyfr = sum(ch.isdigit() for ch in file)
liczba_spacji = sum(ch.isspace() for ch in file)
znaki_spec = len(file) - (liczba_liter + liczba_cyfr + liczba_spacji)

counter = Counter(slowa)
najczestsze = counter.most_common(5)

slowo_max = max(slowa, key=len) if slowa else None

print(f"Liczba linii: {liczba_linii}")
print(f"Liczba liter: {liczba_liter}")
print(f"Liczba cyfr: {liczba_cyfr}")
print(f"Liczba spacji: {liczba_spacji}")
print(f"Znaki specjalne: {znaki_spec}")
print(f"Liczba słów: {len(slowa)}")
print(f"Najdłuższe słowo: {slowo_max} ({len(slowo_max)} znaków)")
print(f"Najczęściej występujące słowo: {najczestsze[0][0]} ({najczestsze[0][1]} razy)")
print("TOP 5 słów:")
for slowo, licznik in najczestsze:
    print(f"{slowo}: {licznik}")

