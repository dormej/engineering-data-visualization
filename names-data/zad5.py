import pandas as pd
import numpy as np

# #series
#
# s = pd.Series([1,3,5,np.nan,6,8])
# print(s)
# s = pd.Series([10,12,8,14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
# print(s) # dane ktore sa w serii są indeksowane pod kątem tymi nazwami
# # nadanie nazw dla kolejnych elementów serii
#
# #DataFrame
# # tworzenie dataframe na podstawie słownika
# data = {'Kraj':['Belgia', 'Indie', 'Brazylia'],
#         'Stolica':['Bruksela','New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 130317035, 207847528]}
# df = pd.DataFrame(data,columns=['Kraj','Stolica','Populacja'])
# print(df)
# #DataFrame przechowuje typ dla każdej kolumny
# print(df.dtypes)


# #możemy również w prosty sposób stowrzyć serię danych - czyli próbki dla kolejnych
# #dat, pomiarów czasu
# daty = pd.date_range('20180401', periods=5) #generujemy zakres dat, początek i ilośc
# #generowanych dat
# print(daty)
#
# df = pd.DataFrame(np.random.randn(5,3), index=daty, columns=list('ABC'))
# print(df)

# biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrzych źródeł
#danych CSV, odczyt i zapis

import xlrd
# import openpyxl
# # Excel - wymagana biblioteka xlrd oraz openpxl
#
# xlsx = pd.ExcelFile('Imiona.xlsx') # nazwa pliku
# df = pd.read_excel(xlsx,'Arkusz1')# nazwa arkusza w Excel
# print(df)
# df.to_excel('z indeksami.xlsx', sheet_name='Wydatki z indeksami') # nazwa kopii pliku
# #, nazwa arkusza

data = {'Kraj':['Belgia', 'Indie', 'Brazylia'],
        'Stolica':['Bruksela','New Delhi', 'Brasilia'],
        'Populacja': [11190846, 130317035, 207847528]}
df = pd.DataFrame(data,columns=['Kraj','Stolica','Populacja'])
print(df)
print(df[1:]) # tak jak przy cięciu list

#kolumna po etykiecie
print(df['Populacja'])

#pobieranie pojedynczej wartosci po indeksie kolumny i wiersza
print(df.iloc[[0],[0]])

#pobieranie wartosci po indeksie wiersza i ettkiecie kolumny
print(df.loc[[0], ['Kraj']])
print(df.at[0, 'Kraj']) # pobiera wartosc, bez indeksu i etykiety

print('kraj moje: ' + df.Kraj)

# losowe pobieranie elementow lub w odniesieniu do procentowej wielkosci calego zbioru
#jeden losowy element
print(df.sample())
#n losowych elem
print(df.sample(2))
#ilosc elem procentowo - zaokrąglenia w góre
print(df.sample(frac=0.5))
#wiecej probek niz elem w zbiorze
#losowe z powtorzeniami
print(df.sample(n=10, replace=True))

print(df.head())
print(df.head(2)) # od początku
print(df.tail(1)) # od końca

print(df.describe()) # podaje zmiany oraz wart ktore mogą nas interesowac

print(df.T)


s = pd.Series([10,12,8,14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
print(s)
print(s[(s>10)])
print(s.where(s>10)) # to samo co wyzej ale wartosci nie spelniajace warunku
#uzupelnia wartością Nan
#możemy podac wartosc, ktora zostanie podstawiona za miat Nan
print(s.where(s>10, 'za duze'))
#inna wart where, modyfikowanie org zbioru , domyślnie zwracana jest kopia
seria2 = s.copy()
seria2.where(seria2 > 10, 'za duze', inplace=True ) # spowoduje zamiane serii 2 kopia
#ktora ma juz zamienione dane. Wyswietlone dane są już zapisane w tym obiekcie
print('##################')
print(seria2)

# wart nie mniejsza od 10
print(s[-(s>10)])
#warunki mozemy ze soba laczyc
print(s [ (s <13) & (s > 8)])

# warunki pobierania danych z DataFrame
print(df[df['Populacja']>120000000])
#bardziej skomplikowane warunki
print(df[((df.Populacja > 100000 ) & (df.index.isin([0,2])))])
print(df[df.Kraj == 'Indie'])

# przyklad z lista dopuszczalnych wart oraz isin zwracająca wartosci boolowskie
print('###########')
szukaj = ['Belgia', 'Brazylia', 'Brasilia']
print(df.isin(szukaj))

# w przypadku serii mozemy dadac/zmieniac wartosci poprzez odwolanie sie do elem serii
#przez klucz
s['Wiesiek']=15
print(s.Wiesiek)
print(s)

#podobna operacja dla DataFrame - wart ustawiona dla wszystkich kolumn
df.loc[3] = 'dodane'# Cały 4 rząd zawiera dane 'dodane'
# ze wzg na to, że DataFrame pracuje na całych listach danych
print(df)
#mozna dodac wiersz w postaci listy
df.loc[5] = ['Polska', 'Warszawa', 38000000]
print(df)

#usuwanie danych mozna wykonac przez funkcje drop, operacja nie wykonuje sie in=space
#zwracana jest kopia DataFrame z usunietymi wart
new_df = df.drop([3])
print(new_df)
df.drop([3], inplace=True)#jezeli chcemy zmienic pierwotny zbior dod parametr inplace = True
print(df)

# do DataFrame mozemy dodac kolumny zamiast wierszy
df['Kontynent'] = ['Europa', 'Azja','Ameryka Południowa', 'Europa']
print(df)
print("_____________________")
#Pandas ma rowniez własne f-kcje sortowania danych
print(df.sort_values(by='Kraj')) #sortujemy po kluczu

#grupowanie
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))

#mozna tez jak w SQL'u czy w Excelu uruchomić f-kcję agregującą na danej kolumnie
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
#gruujemy po Kontynencie i robimy agregacje czyli generujemy sume populacji


#podobny mechanizm to sumy czesciowe i tab przestawne
print('.....Sumy częściowe..........')
#jakie wartosci maja byc sumowane, po jakim indeksie chcemy dzialac,
# chcemy wys kolumny ktore pokaża nam co sumowalismy, podajemy argument ktory bedzie funkcja sumujaca

tabela = pd.pivot_table(df,values=['Populacja'], index=['Kontynent'],columns=['Kraj'],aggfunc=np.sum,margins=True)
print(tabela)
print(tabela.stack('Kraj'))




