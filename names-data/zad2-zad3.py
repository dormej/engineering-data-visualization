import pandas as pd
import numpy as np
import xlrd
import openpyxl

# plik = pd.ExcelFile("Imiona.xlsx")
# df = pd.read_excel(plik, "Arkusz1")
# df.to_excel("Nowy plik.xlsx", sheet_name="Arkusz2")
 # print(df)
#
# print(df[df["Liczba"] > 1000])
# print(df[df["Imię"] == 'DOROTA'])
# print("Lizba ur dzieci: ", df["Liczba"].sum())
# a = df[ (df["Rok"] >= 2000) & (df["Rok"] <= 2005)]
# print(a["Liczba"].sum())
# print(df.groupby(["Płeć"]).agg({"Liczba": ['sum']}))
# b = df.loc[df.groupby(['Rok','Płeć']) ['Liczba'].idxmax()]
# print(b)
# c = df.loc[df.groupby(['Płeć'])['Liczba'].idxmax() ]
# print(c)

df = pd.read_csv("zamowienia.csv", sep=';')
print(df)

print(".............", df["Sprzedawca"].value_counts())
a = (df.groupby(["Sprzedawca"]).size()) # ilosc sprzedazy dla kazdego sprzedawcy
print(a)
b = pd.Series(a.index)
print(b.values) # konwert na liste
print(df.sort_values(by='Utarg', ascending=False).head(5))
print(df.groupby(["Kraj"]).size())

from datetime import date

df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
zam_2005 = df[ (df['Data zamowienia'] < pd.Timestamp(date(2006,1,1))) & (df['Data zamowienia'] > pd.Timestamp(date(2004,12,31))) ]
print("Ilość zamówieiń PL w 2005: ",zam_2005["idZamowienia"] [ (zam_2005["Kraj"] == 'Polska')].count())
print("Wart zamowien Pl w 2005: ",zam_2005['Utarg'][(zam_2005['Kraj']=='Polska')] .sum() )

zam_2004 = df[ (df["Data zamowienia"] < pd.Timestamp(date(2005,1,1))) & (df["Data zamowienia"] > pd.Timestamp(date(2003,12,31))) ]
print(zam_2005["Utarg"].mean())

