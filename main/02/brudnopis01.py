

def policz_slowa(tekst: str) -> dict[str, int]:
    return {slowo: tekst.count(slowo) for slowo in tekst.split()}


print(policz_slowa('ola ma kota OLA ma kota'))


# a = 'bla'
#
# def bla(a: str) -> dict[str, int]:
#     return {abc: a.count(abc) for abc in a.split()}
#
# print(bla(input('Podaj cos: ')))
#
#
# kontakty = {
#     "Ola": {"telefon": "123456789", "email": "ola@example.com"},
# }
#
#
# print(kontakty)



