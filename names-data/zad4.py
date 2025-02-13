# #seria danych jednowymiarowa tablica
# # #random.randn(1000)
# # periods = kazdy dzien z  1000 dni ma przyporzadkowana liczbe z rozkladu naturalnego ??
# #
# # tworzymy przedzial, jezeli nie pasują to są wywalane
# header[0] = naglowek w 1 wierszu
# header None = brak naglowka
#
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
# # f-kcja biblioteki pandas generująca skumulowana sumę kolejnych elementow
# ts = ts.cumsum() # konsola
# print(ts)
# ts.plot()
# plt.show() # wykres

# data = {'Kraj':['Belgia', 'Indie', 'Brazylia','Polska'],
#         'Stolica':['Bruksela','New Delhi', 'Brasilia','Warszawa'],
#         'Populacja': [11190846, 130317035, 207847528,38000000],
#         'Kontynent': ['Europa', 'Azja','Ameryka Południowa', 'Europa']}
#
# df = pd.DataFrame(data,columns=['Kraj','Stolica','Kontynent','Populacja'])
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
# wykres = grupa.plot.bar() # bar słupki , pie koło
# wykres.set_ylabel('Mld')
# wykres.set_xlabel('Kontynent')
# wykres.legend()
# plt.title('Populacja z podziałem na kontynenty')
# plt.show()
#
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
# # f-kcja biblioteki pandas generująca skumulowana sumę kolejnych elementow
# ts = ts.cumsum() # konsola
# df = pd.DataFrame(ts)
# df['MA'] = df.rolling(window=50).mean()
# print(ts)
# df.plot()
# plt.show() # wykres
#
import xlrd
import openpyxl
# Excel - wymagana biblioteka xlrd oraz openpxl

xlsx = pd.ExcelFile('Imiona.xlsx') # nazwa pliku
df = pd.read_excel(xlsx,'Arkusz1')# nazwa arkusza w Excel
print(df)
grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
grupa.plot()

plec = df.groupby(['Płeć']).agg({'Liczba': ['sum']})
wykres = plec.plot.bar()
wykres.plot()
plt.show()







