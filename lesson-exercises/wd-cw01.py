print("zad2")
a,b,c = 2,4,7
dzielenie1 = b/a
dzielenie2 = c/a
dzielenie_calkowite = c // a
reszta = c%a
mnozenie = b*c
dodawanie = a+c
potega = pow(a,b)
print(dzielenie1)
print(dzielenie2)
print(dzielenie_calkowite)
print(reszta)
print(mnozenie)
print(dodawanie)
print(potega)

print("\nzad3")
a+=1
b-=3
c%=7
print(a,b,c)

print("\nzad4")
import math as m
from fractions import Fraction
a=2.567
print(round(a))
print(m.pi)
print(m.sin(m.pi/2))
print(m.sqrt(9))
potega=m.e**10 #potega=(pow(math.e,10))
print(potega)
pierwiastek = pow(m.log(5+pow(m.sin(8),2),m.e),Fraction(1,6))
print(pierwiastek)
print(m.fabs(-3.55))
print(m.fabs(4.80))

print("\nzad5")
name="DOROTA"
surname="MEJŁUN"
print(name.capitalize(), surname.capitalize())

print("\nzad6")
my_string = """No, no, no, no, no, no, no (Oh mamma mia, mamma mia)
Mamma mia, let me go.
Beelzebub has a devil put aside for me, for me, for me."""
print(len(my_string.split("Oh"))-1) # liczy słowa

print("\nzad7")
string = "Galaktyka"
print(string[0], string[8])

print("\nzad8")
print(my_string.split())

print("\nzad9")
imie = "Jan"
print(imie, type (imie))
x = 10.3
print(x, type(x))
y = hex(23)
print(y, type(y))

