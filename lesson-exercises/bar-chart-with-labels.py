import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# WYKRES SŁUPKOWY HORYZONTALNY - ETYKIETY OBOK SŁUPKÓW

plt.subplot(1,2,1)

height = [-17,-74,-2,-35,-45]
x = np.arange(-100,0,20)
y = ['1','4','6','8','8']
y_pos = np.arange(len(height))
label = ['1','4','6','8','8']

bar_plot = plt.barh(y_pos, height, color=['sandybrown','darkred','cyan','black','yellow'])
plt.xlim(-100,0)
plt.yticks(y_pos, y)

for i, v in enumerate(height):
    plt.text(v+(-15), i, str(v),va="center")

plt.title('Tytuł1')

plt.subplot(1,2,2)

height = [12,82,17,74,84]
x = np.arange(-100,0,20)
y = ['8','1','1','8','3']
y_pos = np.arange(len(height))
label = ['1','4','6','8','8']

plt.barh(y_pos, height, color=['red','darkturquoise','darkgreen','springgreen','olivedrab'])
plt.xlim(0,100)
plt.yticks(y_pos, y)

for i, v in enumerate(height):
    plt.text(v+(5), i, str(v), va="center")

plt.title('Tytuł2')

plt.show()

# x = np.linspace(0, np.pi * 2, 100)
# y = np.sin(x)
#
# plt.plot(x, y)
# plt.grid(True)
# plt.xlim(0, np.pi * 2)
# plt.xlabel("x")
# plt.ylabel("f(x) = sin(x)")
# plt.title("Dwa wykresy")
# plt.savefig("fig1.jpg", dpi = 72)
# plt.show()
