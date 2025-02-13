print("\nzad1")
A = [1/x for x in range(1, 11)]
print(A)
B = [2**i for i in range (0,10)]
print(B)
C = [x for x in B if x%4 == 0]
print(C)

print("\nzad2 - incompleted ")
import sys
from random import randint
lista1 = []
lista2 = []
lista3 = []
lista4 = []
for i in range(4):
    for j in range(1):
            lista1.append((randint(0,10)))
            lista2.append((randint(0,10)))
            lista3.append((randint(0,10)))
            lista4.append((randint(0,10)))
lista = [(i,j) for i in [1,2,3] for j in [4,5,6]]
print(lista)

print("\nzad4 and zad5\n")

from random import randint

def my_function(a1,b1,a2,b2):
    if(a1 > 0):
        print("y1 is increasing")
    elif (a1 < 0):
        print("y1 is decreasing")
    elif (a1 == 0):
        print("y1 is constant")
    if (a1 == a2):
        print("y1 is parallel to y2")
    elif (a1 * a2 == -1):
        print("y1 is perpendicular to y2")
    else:
        print("y1 is neither parallel nor perpendicular to y2")
a1 = randint(-10,10)
b1 = randint(-10,10)
a2 = randint(-10,10)
b2 = randint(-10,10)
print("y1 = " + str(a1) + " *x1 + " +str(b1))
print("y2 = " + str(a2) + " *x2 + " +str(b2))
print(my_function(a1, b1, a2, b2))

print("\nzad6")
import math as m
def radius (a = 2, b = 5, x = 2, y = 8):
    return m.sqrt( (x-a)**2 + (y-b)**2)

print(radius())

print("\nzad7")
import math as m
def hypotenuse(a = 3, b = 4):
    return m.sqrt( a**2 + b**2)

print(hypotenuse())

print("\nzad8")
import math as m
def sequence(a = 1, r = 1, ile = 10):
    return ( ( a+ (a+ (ile-1)*r) ) * ile )/2
print(sequence())

print("\nzad9")
import math
def sequence2 (* numbers):
    if len(numbers) == 0:
        return 0
    else:
        product = 1
        for i in numbers:
            product *= i
        return product
print(sequence2())
print(sequence2(1,2,3,4,5))

