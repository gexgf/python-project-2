class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

class Auto(Pojazd):
    def __init__(self,silnik,kolor):
        self.silnik = silnik
        super().__init__(kolor)

class Silnik:
    def __init__(self,pojemnosc):
        self.pojemnosc = pojemnosc

x = Silnik(123)
a = Auto(x,'blue')

print(a.silnik.pojemnosc, a.kolor)

