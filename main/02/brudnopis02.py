word = "ola ma kota ma"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1


print(counter)




# for a in slowa:
#     if a in slowa_dict:
#         slowa_dict[a] += 1
#     else: 
#         slowa_dict[a] = 1
