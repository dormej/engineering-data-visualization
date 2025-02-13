"""
print("zad1")
import sys
print("Podaj tekst: ")
s = sys.stdin.readline()
sys.stdout.write(s)
a = input("Podaj napis: ")
suma=a.count(" ")
print(suma)

import sys
print("\nzad2")
print("Insert n1: ")
n1 = int(sys.stdin.readline())
print("Insert n2: ")
n2 = int(sys.stdin.readline())
mn = n1*n2
print(mn)

import sys
import math as m
print("\nzad4")
n3 = int(input("Insert n3: "))
print(int (m.fabs(n3)))

import sys
print("\nzad5")
a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))
if (a>0 and a<=10) and (a>b or b>c) :
    print("OK")
else:
    print("NOT OK")

print("\nzad6")
for i in range (5, 45, 5):
    print(str(i) + " ")

import sys
print("\nzad7")
for i in range (0, 4, 1):
    x = int(input("Insert the number: "))
    px=x**2
    print(px)

import sys
print("\nzad8")
i=0
lista = []
while (i!= 4):
    x = int(input("Insert x: "))
    lista.append(x)
    i+=1
print(lista)

import sys
print("\nzad9")
suma=0
x = int(input("Insert x: "))
while (x > 0):
        suma += x % 10
        x /= 10
print(int (suma))

import sys
print("\nzad10")
h = int(input("Height: "))
for i in range (1, int(h)+1 ):
    for j in range (1, int(i)+1):
        sys.stdout.write('A')
    sys.stdout.write('\n')
"""
print("\nzad11")
import sys
import math
H = int(input("Height: "))
s = math.ceil(H/2)
n=0
for i in range(1, s + 1):
    for j in range(1, (s - i) + 1):
        print(end=" ")
    while n != (2 * i - 1):
        print("o", end="")
        n = n + 1
    n = 0
    print()
k=1
n=1
for i in range(1, s):
    for j in range(1, k + 1):
        print(end=" ")
    k = k + 1
    while n <= (2 * (s - i) - 1):
        print("o", end="")
        n = n + 1
    n = 1
    print()

