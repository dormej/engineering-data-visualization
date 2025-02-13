import random

class Obiekt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Robaczek(Obiekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.poziom = 1
        self.najedzenie = 0
        self.predkosc = 1

    def zjedzOwoc(self, owoc, lista):
        self.najedzenie += owoc.pobierzJedzenie()
        print('Zjadasz owoc o poziomie najedzenia: ', owoc.pobierzJedzenie())
        print('Twój poziom najedzenia: ', self.najedzenie, '/5')
        lista.remove(owoc)

    def SprawdzPoziom(self):
        if self.najedzenie >= 5:
            self.najedzenie = 5-self.najedzenie
            self.poziom += 1
            print('Awansujesz na poziom ', self.poziom)


class Owoc(Obiekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        random.seed()
        self.jedzenie = random.randint(1, 5)

    def pobierzJedzenie(self):
        return self.jedzenie


def PobierzOwoce(path):
    lista = []
    file = open(path, 'r')
    linie = file.readlines()
    for linia in linie:
        aftersplit = linia.split(',')
        owocnowy = Owoc(aftersplit[0], aftersplit[1])
        lista.append(owocnowy)
    return lista

def sprawdzPozycje(rob, ow):
    if int(rob.x) == int(ow.x) and int(ow.y) == int(rob.y):
        return True
    return False


def sprawdz(robak, owoce):
    for owoc in owoce:
        if sprawdzPozycje(robak, owoc) is True:
            robak.zjedzOwoc(owoc, owoce)
    robak.SprawdzPoziom()

path = input("Wczytaj plik ze wsp. owoców: (wsp_owocow.txt): ")
owoce = PobierzOwoce(path)

robak = Robaczek(0,0)
print("Pozycja robaczka: Rx:",robak.x," Ry:",robak.y)

print("Umiejscowienie owoców: ") #Tylko do pokazania wspołrzędnych
for i in range(0, len(lista), 1):
    print('Ox' +str(i+1) +':', lista[i].x, 'Oy'+str(i+1)+':',lista[i].y,)

print("Poruszasz się WSAD")
while len(owoce) != 0:
    ruch = input('Wykonaj ruch: ')
    if ruch == 'W' or ruch == 'w':
        robak.y +=1
        print('Twoja pozycja x: ',robak.x,'y:',robak.y)
        sprawdz(robak, owoce)
    elif ruch == 'S' or ruch == 's':
        robak.y -= 1
        print('Pozycja x: ', robak.x, 'y:', robak.y)
    elif ruch == 'D' or ruch == 'd':
        robak.x += 1
        print('Pozycja x: ', robak.x, 'y:', robak.y)
    elif ruch == 'A' or ruch == 'a':
        robak.x -= 1
        print('Pozycja x: ', robak.x, 'y:', robak.y)
    elif ruch == 'N' or ruch == 'n':
        print("Poziom: ", robak.poziom)
        print("Poziom najedzenia: ", robak.najedzenie, "/", '5')
        print("Prędkość: ", robak.predkosc)
    else:
        print("Sprobuj ponownie.")
