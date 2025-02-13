import xlrd
import openpyxl
import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_excel('sport.xlsx', header=None)

x = dane.iloc[:,1]
y = dane.iloc[:,0]
plt.pie(x,labels=y, autopct="%1.0f%%", explode=[0.1,0,0,0,0,0])
plt.title("Popularnosc sportow w grupie nastolatkow")
plt.annotate("158016",[-1,1])
plt.savefig("zad2.jpg")
plt.show()

