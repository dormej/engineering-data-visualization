














# l_name = input("Input a landmass: ")
# print(info_landmass(data, l_name))


# x = info_country(data,country_name)
# print(x)
#
# d = x['landmass']
# print(d)

# x = data[['name', 'landmass', 'zone', 'area', 'population', 'language', 'religion']][data['name'] == country_name]
#
#
#
# a = data[ ['zone'][(data['landmass'] == x['landmass']  )]]
#
# print(a)


# print(data)
#
#
# g = data.groupby(['name'])[data.landmass == x.landmass].agg({'population': ['sum']})
# g.plot.bar()
# plt.show()
#



# wyk = data_ladnmass(data,l_name)
# wyk.plot.bar()
# plt.show()

# print(porownaj(data, country_name))

# print(data)
# plt.subplot(1,3,1)
# wykres = data.groupby(['name']).agg({'population':['sum']}).head(5)
# wykres.plot.bar()
# plt.xticks(rotation=45)
# plt.show()

# choice = input('CHOICE THE OPTIONS: ')

# if choice == '1' :
#     x = input("Input a landmass: ")
#     print(group_by_landmass(data, x))
#     y = input("Input a zone: ")
#     print(group_by_zone(data, y))
# else:
#     print("Try again")