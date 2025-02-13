# import pandas as pd
# import numpy as np
#
# s = pd.Series ([3,-5,7,4])
# print(s)
# print(s.values)
# t = np.sort(s.values)
# print(t)
# print(s.index)
# s = pd.Series([3,-5,7,4], index=['a','b','c','d'])
# print(s)
# print(s[s>=4])
# print(np.sin(s))
#
# d = {'key1': 350, 'key2':700,'key3':70}
# s = pd.Series(d)
# print(s)
# k = ['key0','key2','key3','key1']
# s = pd.Series(d, index=k)
# print(s)
# print(pd.notnull(s))
# print(pd.isnull(s))
# print(s.isnull())
#
# s.name = 'Wartość'
# s.index.name = 'Klucz'
# print(s)
#
# data = {'Kraj': ['Belgia','Indie','Brazylia'], 'Stolica':['Bruksela','New Delhi','Brasilia'],'Populacja':[11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# df = pd.DataFrame(data, columns=['Kraj','Stolica','Populacja'])
# print(df)
# print(df.dtypes)
#
# # daty = pd.date_range('19990501',periods=5)
# # print(daty)
# #
# # df = pd.DataFrame(np.random.randn(5,2), index=daty, columns=list('AB'))
# # print(df)
# print(df[:1])
# print(df['Kraj'])
#
# print(df[['Kraj','Stolica']])
# print(df.iloc[1][1],df.iloc[0,1]) # jedna pozycja
# print(df.loc[1],['Kraj']) # pobiera cały wiersz
# print(df.at[0,'Kraj']) # index = 0 w Kolumnie
# print(df.at[1,'Stolica'])
# print(df["Stolica"])
#
# print('kraj: ' + df['Kraj'])
#
# print(df.sample()) # jeden losowy elem.
# print(df.sample(2)) # dwa losowe elementy
# print(df.sample(frac=0.5)) # ilość elementow procentowo, zaokrągla do góry
#
# print(df.sample(10, replace=True ))
#
# print(df.head(1)) # od gory
# print(df.tail(2)) # od dołu
#
# print(df.describe()) # statystyka dla wartosci
#
# print(df.T)
#
# seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
#
# print(seria[(seria>10)])
# print(seria.where(seria>10, 'nie pasuje'))
#
# seria2 = seria.copy()
# seria2.where(seria2>10, inplace=True)
# print(seria2)
#
# print(seria[~(seria>10)])
# print(seria.where(~(seria>10)))
#
# # Warunki pobierania danych dla DataFrame
#
# print(df[df['Populacja'] > 1200000000])
# print(df[((df.Populacja > 100000000) & (df.index.isin([0,1])))])
#
# print("______________________")
# szukaj = ['Belgia','Brasilia']
# print(df.isin(szukaj))
# df.loc[4] = 'dodane'
# print(df)
# df.loc['nowy']=(['Polska','Warszawa',13000000])
# print(df)
#
# # usuwanie danych można wykonać przez funkcję drop, ale pamiętajmy, że operacja nie wykonuje się in-place więc
# # zwracana jest kopia DataFrame z usuniętymi wartościami
#
# # new_df = df.drop([4]) #inplace = Truejeżeli chcemy zmienić pierwotny zbiór
# # print(new_df)
# # print(df)
# df = df.drop([4])
# print(df)
#
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
# print(df)
# print(df.sort_values(by='Kraj'))
# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO000OOOO")
# grupa = df.groupby(['Kontynent'])
# print(grupa.get_group('Europa'))
#
# print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
# print("_____sumy częściowe___________")
# tabela = pd.pivot_table(df, values=['Populacja'], index=["Kontynent"],columns=["Stolica"],aggfunc=sum, margins=True )
# print(tabela.stack('Stolica'))

#
print("ZADANIE 2 WD_CW08")

import pandas as pd
import numpy as np
import xlrd
import openpyxl

plik = pd.ExcelFile('Imiona.xlsx')
df = pd.read_excel(plik, 'Arkusz1')
print(df)
print(df[df['Liczba'] > 1000])
print(df[df.Imię == 'DOROTA'])
print(df.groupby(['Rok']).agg({"Liczba":['sum']}))
r = (df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)])
print(r)
print(r['Liczba'].sum())
print("Suma urodzonych chłopców i dziewczynek")
print(df.groupby(['Płeć']).agg({"Liczba":['sum']}))

print("------------------------------------------------------------------")
print(df.groupby(['Rok', 'Płeć']).head(1))
print("------------------------------------------------------------------")

# t = df.groupby(['Płeć']).agg({'Liczba':['max']})
# print(t)
# print(df["Imię"][(df["Liczba"] == 17399)])
# print(df["Imię"][(df["Liczba"] == 18612)])

k = (df[(df['Płeć'] == 'K')]['Liczba'].max())
m = (df[(df['Płeć'] == 'M')]['Liczba'].max())

print(df["Imię"] [ (df.Liczba == k )])
print(df["Imię"] [ (df.Liczba == m )])


# print(df.groupby(['Rok']).agg({'Liczba': ['max']}))
#
# import numpy as np
# import pandas as pd
#
# df = pd.read_csv('zamowienia.csv',sep=';' )
# print(df)
# print(df.iloc[0,0])
# #
# # grupa = df.groupby(["Sprzedawca"])
# # print(grupa)
#
# g = df.sort_values(by='Utarg',ascending=False).head(5)
# print(g["Utarg"])
# # print(df.groupby(['Sprzedawca']).agg({'Utarg':['sum']}))
# # print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))#wart zamowien dla kazdego kraju
#
# g1 = df.groupby(["Sprzedawca"]).size()
# print(g1.index)
# print(g1)
#
# g2 = df.groupby(["Kraj"]).size()
# print(g2)
#
# print("###################################################################")
# from datetime import date
# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# zam_2005 = (df [ ( df['Data zamowienia'] < pd.Timestamp(date(2006,1,1)) ) & (df["Data zamowienia"] > pd.Timestamp(date(2004,12,31)) ) ] )
#
# print(zam_2005)
# ileP = (zam_2005["idZamowienia"] [(zam_2005["Kraj"] == "Polska")]) .count()
# print(ileP)
# ileN = (zam_2005["idZamowienia"] [(zam_2005["Kraj"] == "Niemcy")]) .count()
# print(ileN)
# print("#################################################################")
# print("SREDNIA KWOTA ZAMOWIENIA W 2004")
# zam_2004 = (df [ (df["Data zamowienia"] < pd.Timestamp(date(2005,1,1))) & (df['Data zamowienia'] > pd.Timestamp(date(2003,12,31))) ] )
# srednia = zam_2004["Utarg"].mean()
# print(srednia)
#
# zamowienie_2004 = df[ (df["Data zamowienia"] < pd.Timestamp(date(2005,1,1))) & (df["Data zamowienia"] > pd.Timestamp(date(2003,12,31))) ]
# zamowienie_2005 = df[ (df["Data zamowienia"] < pd.Timestamp(date(2006,1,1))) & (df["Data zamowienia"] > pd.Timestamp(date(2004,12,31))) ]
#
# zamowienie_2004.to_csv("zamowienie_2004.csv")
# zamowienie_2005.to_csv("zamowienie_2005.csv",index= True)

