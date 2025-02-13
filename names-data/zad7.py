import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# major tick - element podziałki, większy skok, (wart całkowita)
# minor tick - mniejszy sok (wart rzeczywista)

# spines - szkielet
#grid - siatka

# plt.plot([1,2,3,4],[10,20,30,40],'r--') # jezeli nie przekazemy dziedziny, to plot sama ją wybierze
# #indeksuje domyslnie od 0
# plt.ylabel('jakies liczby')
# plt.show()

# plt.plot([1,2,3,4], [1,4,9,16], 'ro-')
# plt.axis([0,6,0,20]) # dokladne zakresy wszystkich etykiet na osi x(0-6) i y(0-20)
# plt.annotate('max', xy=(4, 16), xytext=(4.5, 12.5),arrowprops=dict(facecolor='red', shrink=1))
# plt.show()

#
# t = np.arange(0.,5.,0.2)
# print(t)
#
# plt.plot(t,t,'r--',t,t**2, 'bs',t,t**3,'g^') # dziedzina, wartosci dziedziny,
# plt.show()
# #
# x = np.linspace(0,2,100)
# print(x[:10])
# plt.plot(x,x,label='liniowa')
# plt.plot(x,x**2,label='kwadratowa')
# plt.plot(x,x**3,label='szescienna')
#
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# plt.title('Prosty wykres')
#
# plt.legend(loc='center')
# plt.show()
# #
# data = {'a': np.arange(50),
#         'c': np.random.randint(0,50,50),
#         'd': np.random.randn(50)} # 50 wart z rozkladu naturalnego
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# print(data)
#
# plt.scatter('a','b',c='c',s='d',data=data) #dziedzina, wartosc, kolor, size znajduje
# # w kluczy 'd' , slownik wskazujemy data.
# plt.xlabel('wartosc a')
# plt.ylabel('wartosc b')
# plt.show()

#WIELOWYKRESY to wiz wielu wykresow z czego kazdy wykres jest w innym oknie na
#jednym płutnie

# x1 = np.arange(0.0,2.0,0.02)
# x2 = np.arange(0.0,2.0,0.02)
#
# y1 = np.sin(2*np.pi*x1)
# y2 = np.cos(2*np.pi*x2)
#
# print(x1[:10])
#
# plt.subplot(2,1,1)
# plt.plot(x1,y1,'--')
# plt.title('Dwa wykresy')
# plt.ylabel('sin(x)')
#
# plt.subplot(2,1,1)
# plt.plot(x2,y2,'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
#
# plt.show()
#
# etykiety = ['K', 'M']
# wartosci = [345, 435]
#
# plt.bar(etykiety, wartosci)
#
# plt.xticks(rotation=45)
# plt.ylabel('Ilosc narodzin')
# plt.xlabel('płec')
# plt.show()
# #
#
#HISTOGRAM
#
# x = np.random.randn(10000)
# print(x[:5])
#
# plt.hist(x,bins=50, facecolor = 'g', alpha=0.75, density=True) #chcemy 50 slupkow
# # alpha - przezroczystosc, density -
# plt.xlabel('Wart.')
# plt.ylabel('Prawdopodobienstwo wyst.')
# plt.title('Histogram')
# plt.grid(True)
# plt.show()
#
# zawodnicy = ['Messi', 'Suarez', 'Dembele','Continho']
# bramki = [40,25,13,11]
#
# wedges, texts, autotexts = plt.pie(bramki,labels=zawodnicy,autopct=lambda pct:'{:.1f}%'.format(pct), textprops=dict(color='black') )
# # udzial procentowy autopct ....
# plt.setp(autotexts,size = 10, weight='bold')
# plt.title('Tytuł: Pierwsza')
#
# plt.legend(title='Zawodnicy', loc='upper left')
# plt.show()
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv('zamowienia.csv', delimiter=';')
grupa = df.groupby(['Sprzedawca']).agg({'Utarg': ['sum']})
print(grupa)
print(len(grupa))
explode = [0,0,0,0.1,0,0,0,0,0]
wykres = grupa.plot.pie(subplots=True, autopct='%.1f %%', explode=explode, fontsize=7, figsize=(6,6),shadow=True)
legenda = plt.legend()
legenda.remove()
plt.show()
