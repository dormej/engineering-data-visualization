import numpy as np

# # inicjalizacja tablicy
# a = np.arange(2)
# print(a)
#
# #wypisanie typu zmiennej tablicy (nie jej elementow) - ndarray
# print(type(a))
#
# #sprawdzanie typu danych
# print(a.dtype)

#inicjalizacja tablicy z konkretnym typem danych
# a = np.arange(2, dtype='int64')
# print(a.dtype) #możemy typy danych modfikowac, ale wiąże się to z tworzeniem
# # kolejnej tablicy, kolejnego obiektu, ktory bedzie trzymal ten nowy typ
#
# #zapisanie kopii tablicy jako tablicy z innnym typem
# b = a.astype('float') # do tego sluzy metoda stype. Czyli tę motodę wywołujemy
# #na obiekcie typu numpy.ndarray i mozemy przekonwertowac te dane na float'a. Wtedy
# #nastepuje kopiowanie tej tablicy. Tablica a , mimo że wywołujemy na niej metodę,
# #ona wygeneruje druga tablice b
# print(b)
# print(a)
# #wypisanie rozmiarow tablicy
# print(b.shape) # kształ tablicy. Zwraca krotke, pokazuje jaki mamy wymiar na kazdym
# #z wymiarow. mamy jednowymiarowa tablice z dwoma elem w jednym wymiarze
#
# #sprawdza ilosc wymiarow tablicy
# print(b.ndim) # mamy jednowymiarowa tablice
#
# #tworzenie tablicy wielowymiarowej
# m = np.array([np.arange(2), np.arange(2)]) #generujemy 2 rzedy
# print(m) #typ to ndarray
# print(m.shape) # dwuwymiarowa tablica, w kazdym z dwoch wymiarow mamy po dwa elem
# print(m.ndim) # mamy dwuwymiarowa tablice

# #mozemy stworzyc macierz danego rozmiaru
# zera = np.zeros((5,5))
# print(zera)
# jedynki = np.ones((4,4))
# print(jedynki)
# print(jedynki.dtype)
# pusta = np.empty((2,2))
# print(pusta)
#
# #do elem tablic odwolujemy sie podajac indeksy
# poz_1 = pusta[1,1]
# poz_2 = pusta[0,1]
# print(poz_2)

# #f-kcja arange tworzy również ciągi liczb zmiennoprzecinkowych
# liczby = np.arange(1,2,0.1)
# print(liczby)
# #podobne działanie f=kcji linspace, ktorej dzialanie jest rownowazne tej samej f-kcji
# #w MatLAB-ie
# liczby_lin = np.linspace(1,2,5) # piszemy ile elementow ma być wygenerowanych z tego
# #przedzialu
# print(liczby_lin)
#
#generwujemy dwie macierze. Najpierw wart są iterowane w kolumnie, potem w wierszu
z = np.indices((5,3)) # wywołania f-kcji indicesi i podajemy argumenty - krotke,
print(z)
#wielowymiarowe macierze mozemy rowniez generowac f-kcja mgrid
x,y = np.mgrid[0:5, 0:5] #na poczatku te same wart w wierszach, a potem w kolumnach
print(x,y)
#
# #macierze diagonalne
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# mat_diag2 = np.diag([a for a in range(5)], -2) # -2 okresla indeks przekatnej macierzy
# #wzgledem głównej przekatnej. Macierz powiekszy sie o dwa aby zmiescic wszystkie wartosci
# print(mat_diag2)

# #generujemy tablice z obiektu ktory mozemy iteratowac
# z = np.fromiter(range(5), dtype='int32')
# print(z) # mamy macierz jednowymiarowa

# #dzięki f-kcji frombuffer tworzymy tablice znakow, stringow
# marcin = b'Marcin' # zainicjowane jako ciąg bajtow
# mar = np.frombuffer(marcin, dtype='S1') # dtype = 'Snumber' nmber wskazuje na ilosc
# #elementow w podzialce
# #f-kcja powoduje, ze trzeba jawnie określić iż ciąg znaków przekazujemy jako ciąg bajtów
# #co osiągamy przez podanie litery 'b' przed wartoscią zmiennej tekstowej.
# print(mar)
# #Inny sposob na osiągnięcie tego samego
marcin = 'Marcin' # zwykly string
#
mar_2 = np.array(list(marcin))
print(mar_2)
mar_3 = np.array(list(b'Marcin'))
print(mar_3)
mar_4 = np.fromiter(marcin, dtype='U1')
# print(mar_4)
marcin = 'Marcin'
a = np.array(list(marcin))
print(a)


# #dzialanie na tablicach
# mat = np.ones((2,2))
# mat2 = np.ones((2,2))
# mat = mat + mat2
# print(mat)
# print(mat - mat2)
# print(mat*mat)
# print(mat/mat)
#
# #cięcie (slicing) tablic numpy można wykonać za pomocą wartości z funkcji slice lub range
# a  = np.arange(10)
# s = slice(2,7,2)
# print(a)
# print(s)
# print(a[s]) # z tab a bierzemy pzedzial zgodby z s
# s = range(2,7,2)
# print(a[s])
# print(a[1:])
# print(a[2:5])
# # # w podobny sposob postepujemy w przypadku tablic wielowymiarowych
# mat = np.arange(25) # jeden rzad 25 elem
# # #teraz zmieniamy ksztalt tablicy jednowymiarowej na macierz 5x5
# mat = mat.reshape((5,5)) # 5 rzedow po 5
# # print(mat)
# print(mat[1:]) # od drugiego wiersza (brak pierwszego)
# print(mat[:,1]) # druga kolumna jako wektor, jest wyswietlona
# # : (wszystkie elementy), 1 (z kolumny 1 )
# print(mat[...,1]) # to samo z wykorzystaniem ellipse(...)
# print(mat[:,1:2]) # druga kolumna jako ndarray tworzymy kolejny rząd do naszej
# #iteracji
# print(mat[:,-1:])
# print(mat[1:3, 2:4])
# print(mat)
# #inicjujemy dane
# a = np.array( [20,30,30,50])
# b = np.arange(4)#tworzy liste [0,1,2,3]
# print(a)
# print(b)
# #wykonujemy operacje i zapisujemy na nowej zmiennej
# c = a-b
# print(c)
# print(b**2)
# a+=b
# print(a)
# a-=b
# print(a) # działamy na kopii
#
# # konkretne dzialania na konkretnych osiach
# b = np.arange(12).reshape(3,4)
# print(b)
# #suma całej macierzy
# print(b.sum())
# #suma każdej z kolumn
# print(b.sum(axis=0))
# #minimum każdego rzędu/wiersza
# print(b.sum(axis=1))
# #skumulowana suma dla rzędu (axis=0) dla kolumny
# print(b.cumsum(axis=1))
# #
# #inicjujemy dane
# a = np.arange(3)
# b = np.arange(3)
# print(a.dot(b)) #iloczyn macierzy
# print(np.dot(a,b)) # to samo inny sposob. funkcja dot pobiera dwa arg
# #
# # macierz całkowita
# a = np.ones(3, dtype=np.int32)
# print(a.dtype.name)
# #macierz zmiennoprzecinkowa
# b = np.linspace(0,np.pi,3)
# print(b.dtype.name)
# c = a+b
# print(c) # wynik jest macierza zmiennoprzecinkowa
# print(c.dtype.name)
# d = np.exp(c*1j)
# print(d)
# print(d.dtype.name)
#
# # #mozliwosc wywowylania funkcji
#
# b = np.arange(3)
# print(b)
# print(np.exp(b))  #to nie są metody na obiekcie, wywołujemy funkcję exp z pakietu
# #numpy na b
#
# #generujemy macierz 3x2
# b = np.arange(6).reshape(3,2)
# print(b)
# #iterujemy wzdłóż pierwszej osi
# for a in b:
#     print(a)
# for a in b.flat:
#     print(a)  # iterujemy jakby to była macierz płaska, nie wazne jak sa poukladane
#     # interesuja nas same wartosci
#
# #iterujemy macierz 1x6
# b = np.arange(6)
# for a in b.flat:
#     print(a)
# print(b)
# print(b.shape) #krotka
# c = np.array([np.arange(3), np.arange(3), np.arange(3)])
# print(c)
# print(c.shape) # na kazdym rzedzie mamy 3 elem i mamy 3 rzedy
#
# d = b.reshape((2,3)) #iloczyn argumentow w krotce to iloczyn ilosci wygenerowa
# print(d)
# print(d.shape)
# e = d.ravel() # spłaszczamy macierz, zyskując pierwotny kształt ze zmiennej b
# print(e)
# print(e.shape)
#
# #transpozycja macierzy
# f = d.T
# print(f)
# print(f.shape)
#
#
#
# # a = np.zeros(3)
# # z = np.zeros(10)
# # print(a)
# # print(type(a))
# # z.shape = (10, 1)
# # print(z)
# # z = np.ones(10)
# # print(z)
# # z = np.linspace(2, 10, 5) #from 2 to 10, with 5 elements
# # z = np.array([10,20])
# # print(z)
# # a_list = [1,2,3,4,5,6,7]
# # z = np.array([a_list])
# # print(z)
# # np.random.seed(0)
# # z1 = np.random.randint(10, size=6)
# # print(z1)
# # print(z1[-2])