
slowa = "kotek kotek kotek ma mlotek"

slowa_dict = {}

for a in slowa:
    if a in slowa_dict:
        slowa_dict[a] += 1
    else:
        slowa_dict[a] = 1


max_slowo = None
max_ilosc = 0
for a in slowa:
    if slowa_dict[a] > max_ilosc:
        max_ilosc = slowa_dict[a]
        max_slowo = a

print(max_ilosc)
print(max_slowo)