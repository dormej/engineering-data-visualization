
# Stwórz 2 Klasy: Robaczek i Owoc dziedziczące po klasie Obiekt
# 2. Klasa obiekt ma posiadać atrybuty x i y , które są współrzędnymi obiektu
# 3. Klasa Robaczek ma posiadać atrybuty zawierające: prędkość, poziom i najedzenie
# 4. Owoc posiada parametr jedzenie o losowej wartości z przedziału 1-5
# 5. Klasa robaczek ma posiadać metody zjedzOwoc przyjmujące obiekt typu Owoc(dodanie  wartości z owocu do parametru najedzenie i usunięcie elementu z listy) oraz metodę  sprawdź poziom, która ustawia poziom Robaczka jeżeli zje odpowiednią ilość owoców
import random

class Obiekt:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Robaczek(Obiekt):
    def __init__(self, x, y, poziom, najedzenie, predkosc):
        super().__init__(x, y)
        self.poziom = poziom
        self.najedzenie = najedzenie
        self.predkosc = predkosc

    def zjedzOwoc(self, owoc):
        self.najedzenie += owoc.pobierzJedzenie()
        print('Zjadasz owoc o poziomie najedzenia: ', owoc.pobierzJedzenie())
        print('Zjadasz owoc o nazwie: ', owoc.nazwa)
        print('Twój poziom najedzenia: ', self.najedzenie, '/5')

    def SprawdzPoziom(self):
        if self.najedzenie >= 5:
            self.najedzenie = 5-self.najedzenie
            self.poziom += 1
            print('Poziom: ', self.poziom)


class Owoc(Obiekt):
    def __init__(self, x, y, jedzenie, nazwa):
        super().__init__(x, y)
        random.seed()
        self.jedzenie = random.randint(1, 5)
        self.jedzenie = jedzenie
        self.nazwa = nazwa

    def pobierzJedzenie(self):
        return self.jedzenie