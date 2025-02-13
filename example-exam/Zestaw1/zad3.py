import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("wyksz.csv")
print(df)

wyzsze = df[df['Wykształcenie']=='wyższe']
srednie = df[df['Wykształcenie']=='średnie']
podstawowe = df[df['Wykształcenie']=='podstawowe']

x = np.arange(0,len(wyzsze))
plt.bar(x-0.25,wyzsze['Liczebność'], width=0.25, label='wyzsze', color='darkblue')
plt.bar(x,srednie['Liczebność'], width=0.25, label='średnie', color='green')
plt.bar(x+0.25,podstawowe['Liczebność'], width=0.25, label='podstawowe', color='darkred')
plt.xticks(x,(podstawowe['Wiek']))
plt.xlabel("Przedział wiekowy")
plt.ylabel("Liczebność")
plt.legend(loc=7)
plt.show()

