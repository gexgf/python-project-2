class Polo:
    def __init__(self):
        print(f'to jest')

    def hamuj(self):
        print('hamujeee')
        self.skrecaj('do rowa')

    def skrecaj(self, strona='lewo'):
        print(f'skrecam w {strona}')

    def paliwo(self):
        return '10 L'

    def info(self):
        print(self)
    # def __str__(self):
    #     return self


x = Polo()

x.info()
