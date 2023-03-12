import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) #subplot function allows double graphs to be printed out 
                    #the syntax is to tell that the figure has 1 row, 2 columns and this plot is the first one.
plt.grid(color = "black", linestyle = '--', linewidth = 0.5)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) #the syntax is to tell that the figure is 1 row, 2 colums and the plot is 2nd one.
plt.grid(color = "black", linestyle = '--', linewidth = 0.5)
plt.plot(x,y)

plt.show()