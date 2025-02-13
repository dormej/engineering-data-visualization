import math
import matplotlib.pyplot as plt
import numpy as np


fx_name = r'$f(x) = \frac{4-x+x^3}{6+x-4*x^2+x^3}$'
x = np.arange(-10,10,step=0.001)
y = (4-x+x**3)/(6+x-4*x**2+x**3)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x,y, color = 'lightblue', label = "f(x)")


av = np.ones(len(x))
plt.plot(x,av, color = 'red', linestyle = '--', label= "as.poz. y=1")
plt.ylim(-50,50)

ahx1 = [-1,-1]
ahy1 = [-50,50]
plt.plot(ahx1,ahy1,color = 'orange', linestyle='--', label='as. pion. x=-1')

ahx2 = [2,2]
ahy2 = [-50,50]
plt.plot(ahx2,ahy2,color = 'green', linestyle='--', label="as.pion x=2")

ahx3 = [3,3]
ahy3 = [-50,50]
plt.plot(ahx3,ahy3,color = 'black', linestyle='--',label="as.pion x=3")
plt.legend()
plt.title(fx_name)
plt.savefig("zad1.pdf",format = 'pdf')

plt.show()
