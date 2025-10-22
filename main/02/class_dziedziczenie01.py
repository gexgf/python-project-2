class Auto:
    def __init__(self, waga, nazwa):
        self.waga = waga
        self.name = nazwa

    def go(self):
        print('jadee')


class AutoSpalinowe(Auto):
    def __init__(self, cylindrow, waga, nazwa):
        self.cylindrow = cylindrow
        super().__init__(waga, nazwa)

    def olej(self):
        print('olej is OK')
        # return 'olej is OK'


x = AutoSpalinowe(6, 1400, "bmw")

print(x.name, x.waga, x.cylindrow)
x.olej()

print(AutoSpalinowe.__mro__)



