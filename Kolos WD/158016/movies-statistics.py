import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("movie.csv", sep=',')
print(df)

def get_statistical_params(df):
    return df.describe(include='all').T

print(get_statistical_params(df))

def add_actor_total_fb_likes(df):
    a1 = df["actor_1_facebook_likes"]
    a2 = df["actor_2_facebook_likes"]
    a3 = df["actor_3_facebook_likes"]
    df["actor_total_fb_likes"] = a1+a2+a3
    return df
print(add_actor_total_fb_likes(df))

def get_min_imdb_score(df):
    b = df.sort_values(by = 'imdb_score').head(10)
    return np.array(b['movie_title'])
print(get_min_imdb_score(df))

def get_rows_cols(df):
    x = 2
    y = 168
    z = 3
    return df.loc[1:,::z].iloc[range(x,y,z+x)]
print(get_rows_cols(df))

plt.grid(True)

plt.subplot(3,3,1)
dane_a = df.head(8)
plt.plot(dane_a["duration"])
plt.gca().legend(title="Legenda")
plt.title("Długość filmów")

import random
x = 2
y = 168
plt.subplot(3,3,5)
plt.title("wykres punktowy")
ax = df["actor_1_facebook_likes"]*random.randint(x,y)
ay = df["actor_3_facebook_likes"]*random.randint(x,y)
k = [random.randint(x,x*3)]
plt.xlabel("a1 FB like")
plt.ylabel("a3 FB like")
plt.scatter(ax,ay)


plt.subplot(3,3,9)
plt.title("Udział reżysera")
dane_c = (df["director_name"].value_counts()).head(8)
dane_c.plot.pie(subplots=True, autopct='%.2f %%',fontsize=4)
plt.show()





