import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2015', periods=10))
print(ts)

ts.plot()
plt.show()

data = {'Kraj': ['Belgia',  'Indie',  'Brazylia', 'Polska'],
'Stolica': ['Bruksela',  'New Delhi',  'Brasilia', 'Warszawa'],
'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data, columns=['Kraj',  'Stolica', 'Kontynent', 'Populacja'])
print(df)

grupa = df.groupby(["Kontynent"]).agg({'Populacja': ['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel("MlD")
wykres.set_xlabel("Kontynent")
legenda = wykres.legend()
legenda.remove()
plt.title("Populacja z podziałem na kontynenty")
plt.show()

# import matplotlib.pyplot as plt

# df = pd.read_csv("zamowienia.csv", delimiter=';')
# print(df)
#
# grupa = df.groupby(["Sprzedawca"]).agg({'Utarg':['sum']})
# print(grupa)
#
#
# wykres = grupa.plot.pie(subplots=True,pctdistance=0.8,labeldistance=None, autopct='%.2f %%',explode=[0,0.1,0,0,0.1,0,0,0,0], fontsize=7, figsize=(6,6) )
# plt.gca().legend(loc='lower left', ncol=1, bbox_to_anchor=(0.9,0.3))
#
# plt.title("Suma zamowien dla sprzedawcy")
# plt.show()
#
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
# ts = ts.cumsum()
# df = pd.DataFrame(ts)
# df['MA'] = df.rolling(window=10).mean()
# df.plot()
# plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile("Imiona.xlsx")
df = pd.read_excel(xlsx,"Arkusz1")
print(df)

zad1 = df.groupby(["Rok"]).agg({'Liczba': ['sum']})
# x = zad1.index
# y = zad1.values
# plt.plot(x,y)
wykres = zad1.plot()
# plt.axis([2000,2019,200000,700000])
plt.ylabel('Liczba urodzonych dzieci')
wykres.set_ylabel('Liczba dzieci')
plt.show()

# zad2 = df.groupby(["Płeć"]).agg({'Liczba': ['sum']})
# zad2.plot.bar()
# plt.title("Liczba urodzin M i K ")
# plt.gca().legend(loc='center', ncol=1,title="OK")
#
# plt.xticks(rotation=0)
# plt.show()

# dane_wyk_1 = df.groupby(['Płeć']).agg({'Liczba': 'sum'}).reset_index()
# dane_wyk_2 = df.groupby(['Płeć', 'Rok']).agg({'Liczba': 'sum'}).reset_index()
# dane_wyk_3 = df.groupby(['Rok']).agg({'Liczba': 'sum'}).reset_index()
# plt.subplot(1,3,1)
# plt.bar(dane_wyk_1['Płeć'], dane_wyk_1['Liczba'])
# plt.subplot(1,3,2)
#
# plt.bar(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Płeć'] == 'K']['Liczba'], label='Kobiety')
# plt.bar(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Płeć'] == 'M']['Liczba'], label='Mężczyżni', bottom=dane_wyk_2[dane_wyk_2['Płeć'] == 'K']['Liczba'])
# #
# # plt.plot(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Płeć'] == 'K']['Liczba'], label='Kobiety')
# # plt.plot(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Płeć'] == 'M']['Liczba'], label='Mężczyżni', bottom=dane_wyk_2[dane_wyk_2['Płeć'] == 'K']['Liczba'])
# plt.legend()
# plt.subplot(1,3,3)
# plt.bar(dane_wyk_3['Rok'], dane_wyk_3['Liczba'])
# plt.show()
#



# lata = df[(df["Rok"] > 2014)]
# print(lata)
#
# zad3 = lata.groupby(["Płeć"]).agg({'Liczba': ['sum']})
# zad3.plot.pie(subplots=True, autopct='%.2f %%',figsize=(6,6))
# plt.gca().legend(loc='upper left', title='Legenda')
# plt.show()
#
# df = pd.read_csv("zamowienia.csv", sep=';')
# print(df)
# zad5 = df["Sprzedawca"].value_counts()
# print(zad5)
# zad5.plot.bar()
# plt.show()

# import pandas as pd
#
# # sample data
# df = pd.DataFrame({
#     'string_col':['foo','bar','baz','quux','bum','bam','blah'],
#     'x':[10,20,30,40,20,10,30],
#     'y':[1,3,1,1,4,5,8]
# })
#
# # plt.subplots returns an array of arrays. We can
# # directly assign those to variables directly
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
#
# # bar plot for column 'x'
# df.plot(y='x', kind='bar', ax=ax1)
#
# # horizontal bar plot for column 'y'
# df.plot(y='y', kind='bar', ax=ax2)
#
# # both columns in a scatter plot
# df.plot('x','y', kind='scatter', ax=ax3)
#
# # to have two lines, plot twice in the same axis
# df.plot(y='x', kind='line', ax=ax4)
# df.plot(y='y', kind='line', ax=ax4)
# plt.show()
