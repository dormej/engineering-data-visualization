a = 1j * 2J
print(a)
b = 1j * complex(0,2)
print(b)
print(int(a.real))
print(b.imag)
print(abs(a.real))

slowo = 'Pomoc' + 'A'
print(slowo)
print(slowo*3)

string = 'Pomoc' 'A' 'c'
print(string)
print('str' 'ing')
print(string.strip() + 'ing')
print(slowo[5])
print(slowo[2:5])
print(slowo[0:2])
print(slowo[::-1])
print('x' + slowo[-4:])
s = '1234'
print(len(string))

q=[2,3,4,5]
o=['a',q,'b']
print(len(q))
print(o[1][3])
o[1].append('dodaje')
print(o)
print(q)
o.append('dod')
print(o)

a, b = 0, 1
while b < 10:
    print (b)
    a, b = b, a+b
a = ['kot', 'okno', 'wypróżnić']
for x in a:
    print (x, len(x))
for x in a[:]:  # wykrój całą listę (zrób jej kopię)
    if len(x) > 6:
        a.insert(0, x)
print(a)


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'równe', x, '*', n/x)
            break
        else:
            print (n, 'jest liczbą pierwszą')

def f(a, l = []):
    l.append(a)
    return l
print (f(1,))
print (f(2))
print (f(3,['bde']))

def moja_funkcja():
    """ Dokumentacja.

    Druga linia.
    """
    pass
print(moja_funkcja.__doc__)
