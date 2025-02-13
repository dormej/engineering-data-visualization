# print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are")
#
# import sys
# print("Python version")
# print(sys.version)
# print("Version info.")
# print(sys.version_info)
#
# import datetime
#
# now = datetime.datetime.now()
# print("Current date and time: ")
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
#
# from math import pi
#
# # r = float(input("Podaj promień koła: "))
# # print("Powierzchnia koła o promieniu " + str(r) + "to " + str(pi*r**2))
#
# # fname = input("Input your name: ")
# # lname = input("Input your last name: ")
# # print(lname +" "+ fname)
#
# # values = input("Input some comma seprated numbers: ")
# # list = values.split(",")
# # tuple = tuple(list)
# # print("List: ", list) # ,dla danych + dla stringów
# # print("Tuple: ", tuple)
#
# # filename = input("Input the filename: ")
# # f = filename.split('.') # tworzy listę
# # print("The extension od file is: " + str(f[-1])) # extension - rozszerzenie
#
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0]+ " " + color_list[-1])
# print("%s %s" %(color_list[0],color_list[-1]))
#
# exam_st_date = (11, 12, 2014)
# print("The examination will start from: %i/%i/%i" %(exam_st_date))
#
# # n = input("Input n: ")
# # nn = n*2
# # nnn = n*3
# # print("Result =", int(n)+int(nn)+int(nnn) )
# # n = int("%s" %n)
# # nn = int("%s%s" %(n,n))
# # nnn = int("%s%s%s" %(n,n,n))
# # print(n+nn+nnn)
#
# print(abs.__doc__)
# print(abs(123))
#
# # import calendar
# # y = int(input("Input the year: "))
# # m = int(input("Input the moth: "))
# # print(calendar.month(y,m))
#
# # print("""
# #     hajakak
# # kaka
# # """)
# #
# # from datetime import date
# #
# # date1 = date(2020,5,2)
# # date2 = date(2020,5,6)
# # print("Nb of days between dates: ", abs(date1-date2).days)
# #
# # r = 6
# # print("Valume: ", (4/3)*pi*(r**3))
# #
# #
# # def difference(n):
# #     if (n <= 17): return 17-n
# #     return 2*(n-17)
# #
# # n = int(input("Input the number: "))
# # print(difference(n))
#
# # def czy_się_zawiera(x):
# #     if ((x>1000) and (x<2000)): return True
# #
# # x = int(input("Input x: "))
# # print(czy_się_zawiera(x))
#
# # def suma(x):
# #     i = 0
# #     total = 0
# #     for i in range(0,len(x)-1):
# #         if(x[i] == x[i+1]):
# #             for i in range(0, len(x)):
# #                 total = total+int(x[i])
# #             return total*3
# #         else:
# #             for i in range(0, len(x)):
# #                 total = total+int(x[i])
# #             return total
# #
# #     # while (i < len(x)):
# #     #     total = total + int(x[i])
# #     #     i += 1
# #     # return total
# #
# # numbers = input("Input some number (,): ")
# # lista = numbers.split(",")
# # print(suma(lista))
#
# # s = input("Input some string: ")
# # lista = s.split(" ")
# # if ((lista[0] == "Is") or (lista[0] == "is")):
# #     print(s)
# # else:
# #     print("Is", s)
#
# def new_string(s):
#     if ((len(s) >= 2) and (s[:2] == 'Is')):
#         return s
#     return 'Is' + s
# print(new_string("Array"))
#
# def copy (str, n):
#     return str*n
# print(copy(",l.k89",5))
#
# def array(x):
#     i = 0
#     ile = 0
#     for i in range (len(x)):
#         if (4 == x[i]):
#             ile = ile + 1
#     return ile
# lista = [1,4,4,4,5]
# print("W liscie jest", array(lista), "liczb 4." )
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# def wypisz(x):
#     new_list = []
#     i = 0
#     for i in range (0,len(x)):
#         if x[i] == 237:
#             new_list.append(237)
#             break
#         if (x[i] % 2 == 0) :
#             new_list.append(x[i])
#     return new_list
# print(wypisz(numbers))
#
# color1 = set([1,2,3,4])
# color2 = set([3,4])
#
# print(color1.difference(color2))
#
# def NWD (x,y):
#     nwd = 0
#     if x%y == 0:
#         return y
#     for i in range (int(y),0,-1):
#         if (x%i == 0 and y%i == 0):
#             nwd = i
#             break
#     return nwd
# print("NWD to ", NWD(4,32))
#
# def LCM (x,y):
#     if x > y:
#         z = x
#     else:
#         z = y
#     while(True):
#         if ( (z % x == 0) and (z % y == 0)):
#             lcm = z
#             break
#         z = z +1
#     return lcm
# print(LCM(4,6))
#
# def funkcja(x):
#     i=0
#     suma = 0
#     for i in range (0,x):
#         suma = suma + i**3
#     return suma
# print(funkcja(6))
#
# str = 'kolano'
# str = str.ljust(10,'0')
# print(str)
#
# str1 = 'ABCDabcd234lka'
# print(any(c.islower() for c in str1))
#
#
# # program do opróżniania zmiennej
# n = 10
# k = {'x':200}
# l = [1,2,3]
# m = (5,7,8)
# print(type(n)())
# print(type(k)())
# print(type(l)())
# print(type(m)())
#
# x =            30
# print('Value od x is {}'.format(x)) # niszczy spacje
# x = 'True'
# x = int(x=='False')
# print(x)
#
#
# """---------------------------------------------------------------------------------------------------------"""
# def roznia_sie (x):
#     if len(x) == len(set(x)):
#         return True
#     else:
#         return False
# print(roznia_sie([1,2,3,4,5]))
# print(roznia_sie([0,0,0,7,8,]))
#
# lista = [1,2,5,6,6,7,8,1,1]
# print(set(lista))
#
#
#
# def funkcja(x):
#     ile = 0
#     lista = []
#     for a in range (len(x)):
#         for b in range (len(x)):
#             for c in range(len(x)):
#                 for d in range(len(x)):
#                     for e in range(len(x)):
#                         napis = x[a] + x[b] + x[c] + x[d] + x[e]
#                         lista.append(napis)
#
#     return lista
# import random
# print(funkcja('aeiuo'))
# list_item = random.choice(lista)
# print(list_item)
#
#
# # import random
# # char_list = ['a','e','i','o','u']
# # random.shuffle(char_list)
# # print(''.join(char_list))


a=5
b=1
print(a,b)
print(ord('A'))

napis = '0123456789567'
print(napis[2:6:2]) # od drugiego do 6 elem. co drugi element
print(napis[6::2]) # od 6 do końca co drugi elem.
lista_z_napisu = list(napis)
print(lista_z_napisu)

krotka = (1.0, 2, 'tekst')
print(krotka)
liczba = (1,)
print(liczba)

for x in range(0,100,10):
    print("%4i%6i%8i" % (x,x**2,x**3))
for i in range(-10,10):
    print(i)

s= ['ala','ma','kota']
t = ' '.join(s)
print(t)

d = "To jest napis"
d_new = d.replace('napis','nowy napis')
print(d_new)

# napis = input('Wpisz dowolny napis')
# for wyraz in napis.split():
#     lista = list(wyraz)
#     lista.reverse()
#     print(''.join(lista))

bohater = {"hans": "kloss", "james": "bond"}
ujemne = {7: -7, 3: -3}
print(vars()) # Specyficzny słownik zwraca funkcja vars().
# Zawiera on wszystkie dostępne aktualnie zmienne:

