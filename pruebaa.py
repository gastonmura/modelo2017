from pylab import *
import matplotlib.pyplot as plt

# make a square figure and axes
plt.figure(1, figsize=(10, 3))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15,30,45, 10]

explode=(0, 0.05, 0, 0)
plt.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True,startangle=100)
plt.title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
plt.gca().set_aspect('1')



plt.figure(2, figsize=(10, 3))
ax2 = plt.axes([0.1, 0.1, 0.8, 0.8])

labels2 = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs2 = [15,30,45, 10]

explode2=(0, 0.05, 0, 0)
plt.pie(fracs2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True,startangle=100)
plt.title('Orueba de 2 charts', bbox={'facecolor':'0.8', 'pad':5})
plt.gca().set_aspect('1')


plt.show()
