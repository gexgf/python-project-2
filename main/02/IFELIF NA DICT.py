
def first():
    print('TO JE 1st')

def second():
    print('to jest 2nd')

def third():
    print('to je 3rd')

def default():
    print('To je defult')

a = 0

bla = {
    0 : first,
    1 : second,
    2 : third,
}

# print(type(bla))

final = bla.get(a, default)
final()