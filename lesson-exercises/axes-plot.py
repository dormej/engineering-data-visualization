import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fig, ax1 = plt.subplots()
x = np.arange(0,10,step=0.1)
y1 = np.log(x)
ax1.plot(x,y1, color = 'green', label = "y=ln(x)")
ax1.legend(loc=2)
ax1.set_xlabel("oś x")
ax1.set_ylabel("oś y dla ln", color = "green")
ax1.tick_params('y', colors = 'green')

ax2 = ax1.twinx()
ax2.set_ylabel("oś y dla exp", color = 'blue')
ax2.tick_params("y", colors = 'blue')
y2 = np.exp(x)
ax2.plot(x,y2, color ='blue',label ='y=exp(x)', linestyle='--')
ax2.legend(loc = 4)


plt.title("Zestawienie funkcji wykl.")
plt.show()
