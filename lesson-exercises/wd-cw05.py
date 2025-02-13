# print("zad1")
#
# class Material():
#     def __init__(self):
#         self.rodz = 'bawelna'
#         self.dl = '2'
#         self.szer = '1'
#     def wyswietl_nazwe(self):
#         return self.rodz,self.dl,self.szer
#
# class Ubrania(Material):
#     def __init__(self):
#         super().__init__()
#         self.rozm = 'S'
#         self.kolor = 'szary'
#         self.dla_kogo = 'K'
#     def wyswietl_dane(self):
#         return self.rozm,self.kolor,self.dla_kogo
#
# class Sweter(Ubrania):
#     def __init__(self):
#         super().__init__()
#         self.rodz = 'golf'
#     def wyswietl_dane2(self):
#         return self.rodz
#
# ubrania = Ubrania()
# sweter = Sweter()
# print("Rodz swetra: ",sweter.wyswietl_dane2())
# print("Dane: ", sweter.wyswietl_dane())
# print("Material: ",ubrania.rodz)
#
class Ksztalty:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x
    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
    def __add__(self, other):
        return Kwadrat(self.x+other.x)
    def __ge__(self, other):
        return self.x >= other.x
    def __gt__(self, other):
        return self.x > other.x
    def __lt__(self, other):
        return self.x < other.x
    def __le__(self, other):
        return self.x <= other.x

kw = Kwadrat(5)
kw1 = Kwadrat(7)
print(kw)
print(kw+kw)


