word = 'banan'

letter = input('Podaj litere: ')
letters = ['_ '] * len(word)


if letter in word:
    for i in range(len(word)):
        if word[i] == letter:
            letters[i] = letter

print(letters)

