import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_dataframe (path):
    df = pd.read_csv(path, sep=',', header=None)
    df.columns = ['name', 'landmass', 'zone', 'area', 'population', 'language', 'religion', 'bars', 'stripes',
                  'colours', 'red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'circles',
                  'crosses', 'saltires', 'quarters', 'sunstars', 'crescent', 'triangle', 'icon', 'animate', 'text',
                  'topleft', 'botright']
    df['landmass'] = df['landmass'].replace([1,2,3,4,5,6], ['N.America', 'S.America', 'Europe', 'Africa', 'Asia', 'Oceania'])
    df['zone'] = df['zone'].replace([1,2,3,4],['NE','SE','SW','NW'])
    df['language'] = df['language'].replace([1,2,3,4,5,6,7,8,9,10],['English', 'Spanish', 'French', 'German', 'Slavic', 'Other Indo-European', 'Chinese', 'Arabic', 'Japanese/Turkish/Finnish/Magyar', 'Others'])
    df['religion'] = df['religion'].replace([0,1,2,3,4,5,6,7],['Catholic', 'Other Christian', 'Muslim', 'Buddhist', 'Hindu', 'Ethnic', 'Marxist', 'Others'])
    return df

def group_by_landmass(df, landmass_name):
    return df.groupby(['landmass']).get_group(landmass_name)

def info_country(df, country_name):
    x = df[['name', 'landmass','zone','area','population','language','religion']][df['name'] == country_name]
    return x

def info_landmass(df, l_name):
    x = df[['name', 'landmass','zone','area','population','language','religion']][df['landmass'] == l_name]
    return x

def flag_content(df,elem_name):
    # print(df[df[elem_name] == 1])
    # print(df.groupby([df[elem_name] == 1]).size())
    wykres = df.groupby([df[elem_name] == 1]).size()
    plt.title("Number of flags containing " + elem_name)
    plt.ylabel("Number of flags.")
    plt.xticks(rotation=0)
    wykres.plot.bar(color = 'lightblue')
    plt.show()

def flag_color (df, col):
    orr = (df['orange'] == 1).sum()
    bl =  (df['black'] == 1).sum()
    whi = (df['white'] == 1).sum()
    gold = (df['gold'] == 1).sum()
    blue = (df['blue'] == 1).sum()
    green = (df['green'] == 1).sum()
    red = (df['red'] == 1).sum()

    x = ['orange','black','white','gold','blue','green','red']
    y = [orr,bl,whi,gold,blue,green,red]
    plt.scatter(x,y,color = x)
    plt.gca().set_facecolor('lightgrey')
    plt.title("The number of the different colours on the flags. ")
    plt.show()

data = read_dataframe('flag.csv')

print('\nSOME BASIC INFORMATION\n')
print('MENU\n')
print('1 - FLAGS')
print('2 - BASIC INFO ABOUT COUNTRY')
print('3 - BASIC INFO ABOUT LANDMASS')
print('Q - wyjdź')

choice = input('Enter to start ')

while choice != 'Q':
    choice = input('CHOOSE: ')

    if choice == '1':
        print("\nFLAG CONTENT\n")
        print('text: t')
        print('animate: a')
        print('icon: i:')
        print('triangle: tr:')
        print('crescent: c')
        print('colors: col:')

        choice1 = input("\nchoice1:")
        if choice1 == 't':
            flag_content(data, 'text')
        elif choice1 == 'a':
            flag_content(data,'animate')
        elif choice1 == 'i':
            flag_content(data, 'icon')
        elif choice1 == 'tr':
            flag_content(data, 'triangle')
        elif choice1 == 'c':
            flag_content(data, 'crescent')
        elif choice1 == 'col':
            flag_color(data,'colours')

    elif choice == '2':
        country_name = input("Input a country: ")
        print(info_country(data, country_name))

    elif choice == '3':
        print("Population: a: ")
        print("Religions : b: ")
        print("Area: c: ")
        choice3 = input("Choose: ")

        if choice3 == 'a' :
            a = data.groupby(['landmass']).agg({'population':['sum']})
            # wykres2 = x.groupby(['name']).agg({'population': ['sum']})
            a.plot.bar(figsize = (10,7), color = 'lightblue')
            plt.title("Population", weight='bold', size=12)
            plt.gca().legend_.remove()
            plt.xticks(rotation=0)
            plt.ylabel("MLN")
            plt.xlabel('')
            plt.show()
            # print(a)

        elif choice3 == 'b':
            l_name = input("Input a landmass: ")
            x = info_landmass(data, l_name)
            b = x.groupby(['religion']).size()
            wykres2 = b.plot.pie(label = '',subplots=True, autopct='%.2f%%',pctdistance=0.8, fontsize=8 )
            plt.title("Religions", weight='bold', size=12)
            plt.show()
            # print(b)

        elif choice3 == 'c':
            c = data.groupby(['landmass']).agg({'area': ['sum']})
            c.plot.bar(figsize=(10, 7), color='lightgreen')
            plt.title("Area", weight='bold', size=12)
            plt.gca().legend_.remove()
            plt.xticks(rotation =0)
            plt.ylabel("in thousands of square km")
            plt.xlabel('')
            plt.show()
            # print(c)
    else:
        if choice == 'Q':
            break
        else:
            print("Wrong. Try again")
