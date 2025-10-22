class Auto:
    def __init__(self, kolor):
        self.kolor = kolor
        self.paliwo = 7
        self.distance_100 = 12

    def zasieg(self):
        zasieg = round((self.paliwo / self.distance_100) * 100, 2)
        print(f'Na obecnej ilosci paliwa przejedziesz: {zasieg}km')


    def hamuj(self):
        pass


# def wylicz(fuel, dist_100):
#     a = fuel / dist_100
#     b = round(a * 100, 2)
#     print(f'Na obecnej ilosci paliwa przejedziesz: {b}km')


bmw1 = Auto('zielone')
bmw2 = Auto('czarne')

bmw1.paliwo += 3

bmw1.zasieg()
bmw2.zasieg()