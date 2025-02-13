# Przygotuj grę, w której poruszasz się postacią Robaczek.
# Gra ma zawierać:
# X1. 2 Klasy: Robaczek i Owoc dziedziczące po klasie Obiekt
# X2. Klasa obiekt ma posiadać atrybuty x i y , które są współrzędnymi obiektu
# X3. Klasa Robaczek ma posiadać atrybuty zawierające: prędkość, poziom i najedzenie
# X4. Owoc posiada parametr jedzenie o losowej wartości z przedziału 1-5
# X5. Klasa robaczek ma posiadać metody zjedzOwoc przyjmujące obiekt typu Owoc(dodanie  wartości z owocu do parametru najedzenie i usunięcie elementu z listy) oraz metodę  sprawdź poziom, która ustawia poziom Robaczka jeżeli zje odpowiednią ilość owoców
# X6. Funkcję, która przyjmuje 2 argumenty: typu Robaczek oraz Owoc, która ma sprawdzać czy znajdują się na tym samym polu
# X7. Dane na start wczytujemy z pliku(współrzędne obiektów)
# X8. Na start aplikacji podajemy informacje o wszystkich obiektach w grze(współrzędne i inne atrybuty)
# X9. Użytkownik wpisuje na klawiaturze gdzie ma poruszać się robaczek
# X10. Aplikacja ma reagować na dane wejściowe od użytkownika
# X11. Działanie aplikacji kończy się jak lista owoców jest pusta
import random
import sys
import time
import os


class Obiekt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        pass


class Robaczek(Obiekt):
    def __init__(self, x, y, predkosc, poziom, najedzenie):
        super().__init__(x, y)
        self.predkosc = predkosc
        self.poziom = poziom
        self.najedzenie = najedzenie

    def zjedzOwoc(self, owoc):
        self.najedzenie = self.najedzenie + owoc.jedzenie
        owoc.__del__()

    def sprawdz_poziom(self):
        self.poziom = self.poziom + self.najedzenie // 10


class Owoc(Obiekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.jedzenie = random.randrange(5) + 1


def to_samo_pole(robaczek, owoc):
    if robaczek.x == owoc.x and robaczek.y == owoc.y:
        return True
    else:
        return False


gracz = Robaczek(0, 0, 1, 1, 1)
lista_owocow = []
pierwsza_linia = True
with open("robak.txt", "r") as plik:
    for linia in plik:
        linia = linia.replace('\n', '')
        linia = linia.split(',')
        if pierwsza_linia == True:
            gracz.x = int(linia[0])
            gracz.y = int(linia[1])
            pierwsza_linia = False
        else:
            lista_owocow.append(Owoc(int(linia[0]), int(linia[1])))

####################################################################
for i in range(0, 5, 1):
    print('GRA ROZPOCZNIE SIĘ ZA ' + str(5 - i) + ' sekund')
    print('!!! INFORMACJE NA START !!!')
    print('gracz:')
    print(' * pozycja x =', gracz.x)
    print(' * pozycja y =', gracz.y)
    print(' * predkosc gracza =', gracz.predkosc)
    print(' * najedzenie gracza =', gracz.najedzenie)
    print(' * poziom gracza =', gracz.poziom)
    print('wszystkie owoce: ')
    for i in range(0, len(lista_owocow), 1):
        print(' ' + str(i + 1) + ') pozycja x =', lista_owocow[i].x, 'pozycja y =', lista_owocow[i].y, 'jedzenie =',
              lista_owocow[i].jedzenie)
    time.sleep(1)
    os.system('cls')
####################################################################
i = 0
while i < len(lista_owocow):
    if to_samo_pole(gracz, lista_owocow[i]):
        gracz.zjedzOwoc(lista_owocow[i])
        del lista_owocow[i]
    i = i + 1
####################################################################
x = 0
y = 0
while len(lista_owocow) != 0:
    ###############################################################################
    # wyświetlanie planszy
    ###############################################################################
    print('#######################')
    for i in range(0, 11, 1):
        print('#', end='')
        for j in range(0, 21, 1):
            czy_owoc = False
            for k in lista_owocow:
                if ((int(gracz.x) - 10 + j) == int(k.x)) and ((int(gracz.y) + 5 - i) == int(k.y)):
                    print('O', end='')
                    czy_owoc = True
            if czy_owoc == False:
                if i == 5 and j == 10:
                    print('G', end='')
                else:
                    print(' ', end='')
        print('#')
    print('#######################')
    print('#  PAWEŁ  MAJOROWSKI  #')
    print('#######################')
    print('gracz:')
    print(' pozycja x =', gracz.x, 'pozycja y =', gracz.y)
    print(' najedzenie =', gracz.najedzenie, ' poziom = ', gracz.poziom)
    print('pozostałe owoce:')
    for i in lista_owocow:
        print('(' + str(i.x) + ', ' + str(i.y) + ')', end=' ')
    print()
    ###############################################################################
    ###############################################################################
    print('podaj pozycje na która chcesz się udać')
    gracz.x = int(input('podaj współrzędną x: '))
    gracz.y = int(input('podaj współrzędną y: '))
    os.system('cls')

    i = 0
    while i < len(lista_owocow):
        if to_samo_pole(gracz, lista_owocow[i]):
            gracz.zjedzOwoc(lista_owocow[i])
            del lista_owocow[i]
        i = i + 1
    gracz.sprawdz_poziom()

print('!!! Koniec gry !!!')
print('Robak zjadł wszystkie owoce z planszy')
print('gracz:')
print(' * najedzenie gracza =', gracz.najedzenie)
print(' * poziom gracza =', gracz.poziom)
input('Naciśnij Enter aby wyjść z programu...')