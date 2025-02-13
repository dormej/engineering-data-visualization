import matplotlib.pyplot as plt

x = ['Java', 'Python','PHP','JavaScript','C#','C++']
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
width = [0.1,0.2,0.2,0.3,0.5,0.5]
plt.bar(x,y, alpha=0.5, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.barh(x,y) #odwraca wykres :)))))
plt.xticks(x_pos,x, rotation = 90)
y_pos = [0,1,2,5,7,10]
plt.bar(y_pos, y, width=width)
fig, ax = plt.subplots(figsize=(6,5),dpi=100, facecolor='g', edgecolor='yellow')
rects1 = ax.bar(x, y, color='b')
plt.title("Popularity of PL\n Wordlwide, OCT 2017")
plt.xlabel("Languages")
plt.ylabel("Popularity")

plt.minorticks_on()
plt.grid(which='major', linestyle='-',linewidth='0.5',color='red')
plt.grid(which='minor', linestyle=':',linewidth='0.5',color='black')

def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1*height, ha='center', va='bottom')
        autolabel(rects1)

x = ['Java', 'Python','PHP','JavaScript','C#','C++']
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.xticks(x_pos,x, rotation = 90)
plt.subplots_adjust(bottom=0.1, top=.8)
plt.title("Popularity of PL\n Wordlwide, OCT 2017")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.bar(x, y)
plt.minorticks_on()
plt.grid(which='major', linestyle='-',linewidth='0.5',color='red')
plt.grid(which='minor', linestyle=':',linewidth='0.5',color='black')
plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# n_groups = 5
# men = [22,30,33,30,26]
# women = [25,32,30,35,29]
#
# fig, ax = plt.subplots()
# x = np.arange(n_groups)
# bar_width = 0.35
#
# wykres1= plt.bar(x,men, bar_width, label = 'Men', color = 'r')
# wykres2= plt.bar(x+bar_width,women, bar_width, label="Woman")
#
# plt.xlabel('Person')
# plt.ylabel('Score')
# plt.title('Scores by person')
# plt.xticks(x + bar_width, ('G1','G2','G3','G4','G5'))
# plt.legend()
#
# plt.tight_layout()
# plt.show()

# from pandas import DataFrame
# import numpy as np
# import matplotlib.pyplot as plt

# a = np.array([ [4,8,5,7,6], [2,3,4,2,6], [ 4,7,4,7,8], [2,6,4,8,6], [2,4,3,3,2]])
# df = DataFrame(a, columns=['a','b','c','d','legenda3'], index = [2,4,6,8,10])
#
# df.plot(kind='bar', label='Man', yerr=(0.6,1,0.2,0.5,1)) # paski błędów
# plt.xticks(rotation=0)
# plt.minorticks_on()
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#
# plt.show()
#
# men = (22,30,35,35,26)
# women = (25,32,30,35,29)
#
# x = np.arange(5)
#
# wykres1 = plt.bar(x,men, color = 'red', width=0.35, yerr=(1,3,5,0.7,2))
# wykres2 = plt.bar(x,women, bottom=men, color = 'green',width=0.35, yerr=(6,3,5,0.7,2))
#
# plt.ylabel("Scores")
# plt.xlabel('Groups')
# plt.title("Scores by groups\n and gender")
# plt.xticks(x, ("G1",'G2','G3','G4','G5') )
# plt.yticks(np.arange(0,81,10))
# plt.legend((wykres1,wykres2),("Men","Women"))
# plt.show()
#
# L = 70
# M = 100
# S = 150
#
# x = ['Student1','Student2','Student3']
#
# wL = plt.barh(x,L, color = 'red')
# wM = plt.barh(x,M, bottom=L, color='green' )
# # wS = plt.barh(x,L)
#
# plt.xticks(np.arange(0,350,50))
# plt.show()
