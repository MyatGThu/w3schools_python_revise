import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,320])

plt.plot(x,y)

#customize lables

font1 = {'family': 'Poppins', 'color': 'red'}

# title for ploted graph and x / y lables.
plt.title("Sports Watch Data", loc='left', fontdict=font1)
plt.xlabel("Average Paulse")
plt.ylabel("Calorie Burnage")

plt.show()