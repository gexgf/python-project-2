ab = 'adamx'

sz = []
odsz = []

key_sz = {'a':'z', 'd':'u', 'm':'0'}
key_odsz = {'z':'a', 'u':'d', '0':'m'}


for a in ab:
    sz.append(key_sz.get(a,a))

print(sz)

for a in sz:
    odsz.append(key_odsz.get(a,a))

print(odsz)