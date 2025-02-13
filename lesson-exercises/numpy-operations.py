# x = [1,2,3.5,10,20]
# print(x)
# print(x[-1])
#
# import numpy as np
# y = np.array([1,2,3.5,10,20])
# print(y)
# print(np.mean(y))
# print(np.min(y))
# print(np.max(y))
# t = np.ones(5)
# print(t)
#
# r = np.linspace(0,1,5) # od 0 do 1, 5 elementów
# print(r)
#
# import matplotlib.pyplot as plt
#
# plt.plot(r,y,'ro')
# plt.show()
#
# a = '7'
# b = 3
# print("laczenie stringow", a+str(b))
# print("łączenie intów", int(a)+b)

import numpy as np
print(np.__version__)
print(np.show_config())
# print(np.info(np.add))

a = np.array([1,2,3,4])
print(np.all(a)) # true wszystkie elementy nie są zerami
a = np.array([7,3,5,1]) # false
print(np.all(a))
print(np.any(a)) #Czy któreś jest nie zerem False
print(np.iscomplex(a))

a = np.arange(20)
a[(a>=9) & (a<=15)] *= -1
print(a)

m = np.arange(10,22).reshape(3,4)
print(m)
print(m.shape)

x = np.eye(6) # po przekątnej 1 reszta 0
print(x)

x = np.ones((10,10))
x[1:-1,1:-1] = 0
print(x)

x = np.diag([1,2,3,4,5])
print(x)

x = np.zeros((4, 4))
x[::2, 1::2] = 1
x[1::2, ::2] = 1
print(x)

x = np.ones((3,5,2)) #trzy kawałki 5 elem w kawałki i 2 rzędy
print(x)

x = np.array([1,2])
y = np.array(([7,10]))

print(np.dot(x,y))# 1*7 + 2*10

m = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 1, 0])
print(v)
print(m)
result = np.empty_like(m)
for i in range(4):
    result[i, :] = m[i, :] + v
print(result)

lista = [12.23, 13.32, 100, 36.32 ]
a = np.array(lista)
print(a)

a = np.arange(2,11).reshape(3,3)
print(a)

a = np.zeros(10)
a[6] = 11
print(a[::-1]) #od tyłu
x = np.asfarray([1,2,3])
print(x)

x = np.zeros((8,8), dtype=int)
x[1::2, ::2] = 1 # szachownica
x[::2,1::2] = 1
print(x)

lista = [1,2,3,4,5,6,7,8]
print(np.asfarray(lista))

a = np.array([1,2,3,4])
a = np.append(a,[[0,4,0], [9,1,7]])
print(a)

z = np.empty((3,4))
print(z)
a = np.full((3,3),6)
print(a)
for a in np.nditer(a):
    print(a,end='')  #wypisuje kolejno elementy

a = np.arange(1,100)
n = a[(a%3==0) | (a%5==0)]
print(n)
print(n.sum())
#
# a = np.arange(1e3)
# print(a)

x = np.ones((5,5,5)).astype(int)
r = np.ones((3,2,3)).astype(int)
print(x)
print(r)

x = np.arange(12).reshape(3,4)
print(np.multiply(x,3))

x = np.arange(4)
print(x)
y = np.arange(8).reshape(2,4)
print(y)
for a,b in np.nditer([x,y]):
    print("%d:%d"%(a,b))

x = np.zeros((3,), dtype=('i4,f4,a40'))
new_data = [(1, 2., "Albert Einstein"), (2, 2., "Edmond Halley"), (3, 3., "Gertrude B. Elion")]
x[:] = new_data
print(x)

x = np.arange(1,4)
print(x**3)

x = np.array([1,2,3,4])
z = np.array(['Red','Green','White','Orange'])
y = np.array([12.20, 12, 20, 40.1])
result = np.core.records.fromarrays([x,z,y])
print(result[0])
print(result[1])
print(result[2])

x = np.arange(6).reshape((3,2))
print(x)
print(x.tolist())

x = np.arange(9).reshape(3,3)
print(x[:,0])
print(x[:,1])
print(x[:,2])

x = np.array([[12.3,3.4,1.2],[1.2,4.5,7.8],[1.3,5.5,6.8],[1.3,5.5,6.8]])
print(x.astype(int))

x = np.array([[10,20,30],[40,50,60]])
y = np.array([[100],[200]])
print(np.append(x,y,axis=1))

data = np.array([ [6,3,2], [7,9,60], [70,80,90] ])
print(data.tolist())

arra = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arra)
result = arra[[1,2],:]
print(result)
result2 = arra[:,[1,2]]
print(result2)

print(np.max(result2<3))

a = np.empty((0,3))
b = np.append(a,[[10,20,30],[3,4,5]], axis=0)
print(b)

e = np.array([ [1,6,3], [4,5,3]])
print(np.max(e))

x = np.linspace(1,10,4)
print(x)
x = np.random.randn(3,3)
print(x)

f = np.array(np.mat('1 2 5; 3 4 2'))
print(f)

x = np.array([[1,2,3,4],[3,3,3,3]])
print(x)
print(x.shape)

s = np.zeros((5,), dtype=int)
print(s)

a =np.eye(4, k=1)
print(a)
print(a.T)
print(a.flat[6])
print(a.flatten())

a = np.array([[19, 10, 5], [4, 5, 6], [7, 8, 9]])
d = a.sort(axis=1)
print(a)
print(np.unique(a))
