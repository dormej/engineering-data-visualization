
# przygotuj funkcję ruch przyjmującą jako pierwszy argument obiekt klasy robaczek oraz listę owoców oraz userinput() zwracającą wybór użytkownika
#8. Na start aplikacji podajemy informacje o wszystkich obiektach w grze(współrzędne i inne atrybuty)
#9. Użytkownik wpisuje na klawiaturze gdzie ma poruszać się robaczek WSAD
#10. Aplikacja ma reagować na dane wejściowe od użytkownika
# po wykonaniu kazdego ruchu aplikacja ma informowac na standardowym wyjsciu o aktualnym stanie robaczka, jezeli zostanie zjedzony owoc to nalezy podac jego nazwe
#11. Działanie aplikacji kończy się jak lista owoców jest pusta lub użytkownik wpisze Q
# na koniec działania funkcji ruch otrzymujemy słownik jak w zadaniu 2 z aktualnym stanem gry: { robaczek: {x:, y:}, owoce: [ {x:,y:,jedzenie:,nazwa:}..... ]}
from zad_1 import *
from zad_2 import *
from zad_3 import *

from pliki import *


def ruch(rob, lista):
    for owoc_lista in lista:
        if toSamoPole(rob, owoc_lista) is True:
            owoc_obiekt = Owoc(owoc_lista['x'], owoc_lista['y'], owoc_lista['jedzenie'], owoc_lista['nazwa'])
            rob.zjedzOwoc(owoc_obiekt)
            lista.remove(owoc_lista)
    rob.SprawdzPoziom()
    print(dane)

def userinput():
    return input("Podaj literę: ")

path = input("Podaj nazwę pliku z współrzędnymi owoców(data.txt) ")
dane = zapisy.wczytaj(path)
print(dane)
owoce = dane['owoce']

poziom = int(input("Podaj poziom startowy: "))
najedzenie = int(input("Podaj najedzenie startowe: "))
predkosc = int(input("Podaj prędkość startową: "))

robak = Robaczek(dane['robaczek']['x'], dane['robaczek']['y'], poziom, najedzenie, predkosc)

while len(owoce) != 0:
    print("Twoja pozycja to: [%(x)d, %(y)d]" % {'x': robak.getX(), 'y': robak.getY()})
    print("Użyj WSAD aby się poruszyć (Q żeby przerwać, N żeby wyświetlić informację o robaczku)")
    litera = userinput()
    if litera == 'Q' or litera == 'q':
        break
    elif litera == 'a' or litera == 'A':
        print('Poruszasz się w lewo!')
        robak.setX(robak.getX() - 1)
        dane['robaczek']['x'] -= 1
        ruch(robak, owoce)
    elif litera == 'd' or litera == 'D':
        print('Poruszasz się w prawo!')
        robak.setX(robak.getX() + 1)
        dane['robaczek']['x'] += 1
        ruch(robak, owoce)
    elif litera == 'w' or litera == 'W':
        print('Poruszasz się do przodu!')
        robak.setY(robak.getY() + 1)
        dane['robaczek']['y'] += 1
        ruch(robak, owoce)
    elif litera == 'S' or litera == 's':
        print('Poruszasz się do tyłu!')
        robak.setY(robak.getY() - 1)
        dane['robaczek']['y'] -= 1
        ruch(robak, owoce)
    else:
        print("Ta litera jest niepoprawna, podaj inną!")