class Obiekt:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __del__(self):
        pass

class Robaczek:
    def __init__(self, x, y, predkosc, poziom, najedzenie):
        super().__init__(x, y)
        self.predkosc = predkosc
        self.poziom = poziom
        self.najedzenie = najedzenie

    def zjedzOwoc(self, owoc):
        self.najedzenie = self.najedzenie + owoc.jedzenie
        owoc.__del__()

    def sprawdz_poziom(self):
        self.poziom = self.poziom + self.najedzenie

class Owoc(Obiekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.jedzenie = random.randrange(1,6)

def to_samo_pole(robaczek, owoc):
    if robaczek.x == owoc.x and robaczek.y == owoc.y:
        return True
    else:
        return False

