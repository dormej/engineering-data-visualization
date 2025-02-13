# testy do zadan. Potraktujcie to jako wstępne testy jednostkowe
import sys

import zad_1
import zad_2
import zad_3
import zad_4
import pliki
from pliki import *
from io import StringIO
from unittest.mock import patch
from unittest import TestCase

# nie radzę tego kopiować bo to nie jest rozwiązanie do zadania ;)

x1, y1 = 1, 1
x2, y2 = 0, 0
Object = lambda **kwargs: type("Object", (), kwargs)
owoc1 = Object(x=x1, y=x1, food=1)
owoc2 = Object(x=x2, y=y2, food=1)
robaczek = Object( x=x2, y=y2, speed=1, level=1, hunger=1)
if ('Obiekt' in dir(zad3)):
    print('[OK]klasa Obiekt istnieje')
else:
    print('[ERROR]klasa Obiekt nie istnieje')

if ('Robaczek' in dir(zad3)):
    print('[OK]klasa Robaczek istnieje')
    try:
        robaczek = zad3.Robaczek(x2, y2, 1, 1, 1)
        if(issubclass(zad3.Robaczek, zad3.Obiekt)):
            print('[OK]Robaczek dziedziczy po Obiekt')
        else:
            print('[ERROR]Robaczek nie dziedziczy po Obiekt')
        if(issubclass(zad3.Owoc, zad3.Obiekt)):
            print('[OK]Owoc dziedziczy po Obiekt')
        else:
            print('[ERROR]Owoc nie dziedziczy po Obiekt')
        print('[OK]obiekt klasy Robaczek zainicjowany')
    except Exception as e:
       print(f'[ERROR]klasa Robaczek nie może zostac zainicjowana: {e}')
else:
    print('[ERROR]klasa Robaczek nie istnieje')

if ('Owoc' in dir(zad3)):
    print('[OK]klasa Owoc istnieje')
    try:
        owoc1 = zad3.Owoc(x1, y1, 1, 'jablko')
        owoc2 = zad3.Owoc(x2, y2, 1, 'pomarancza')
        print('[OK]obiekt klasy Owoc zainicjowany')
    except Exception as e:
       print(f'[ERROR]klasa Owoc nie może zostac zainicjowana: {e}')
else:
    print('[ERROR]klasa Owoc nie istnieje')

if ('toSamoPole' in dir(zad1)):
    print('[OK]funkcja toSamoPole istnieje')
    try:
        if ( zad1.toSamoPole(robaczek, owoc1) != True ):
            print('[OK]funkcja toSamoPole działa ok dla innych współrzędnych ')
        else:
            print('[ERROR]funkcja toSamoPole nie działa ok dla innych współrzędnych ')
        if ( zad1.toSamoPole(robaczek, owoc2) == True ):
            print('[OK]funkcja toSamoPole działa ok dla tych samych współrzędnych ')
        else:
            print('[ERROR]funkcja toSamoPole nie działa ok dla tych samych współrzędnych ')
    except:
       print('[ERROR]problem z funkcją toSamoPole')
else:
    print('[ERROR]funkcja toSamoPole nie istnieje')

if ('zapisy' in dir(pliki)):
    print('[OK]moduł zapisy istnieje')
    try:
        data = zapisy.wczytaj('coords.txt')
        print('[OK]funkcja wczytaj się uruchomiła')
        if(data['robaczek']['x'] == 1 and data['robaczek']['y'] == 2):
            print('[OK]funkcja wczytaj zwróciła prawidłowe dane robaczka')
        else:
            print('[ERROR]funkcja wczytaj nie zwróciła prawidłowych danych')
        if(data['owoce'][0]['x'] == 1 and data['owoce'][0]['y'] == 1):
            print('[OK]funkcja wczytaj zwróciła prawidłowe dane pierwszego owoca')
        else:
            print('[ERROR]funkcja wczytaj nie zwróciła prawidłowych danych')
    except Exception as e:
        print(f'[ERROR]funkcja wczytaj nie działa: {e}')
else:
    print('[ERROR]moduł zapisy nie istnieje')
sys.stdin = StringIO("S\nA\n")
dane = zad4.ruch(robaczek, [owoc1])
print(dane)
dane = zad4.ruch(dane['robaczek'], dane['owoce'])
try:
    if(len(dane['owoce'])==0):
        print('[OK]Funkcja ruch zdaje się działać prawidłowo')
    else:
        print('[ERROR]Funkcja ruch zdaje się nie działać prawidłowo')
except:
    print('[ERROR]Funkcja ruch zdaje się nie działać prawidłowo')
print('[ALERT]To nie wszystkie testy!!! \nMa to na celu zweryfikwoać czy będę w stanie uruchomić własne testy. \n aplikacja może działać nieprawidłowo nawet jeżeli wszedzie jest OK')
