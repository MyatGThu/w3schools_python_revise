import matplotlib
import sys
matplotlib.use("Agg")

import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np


print(matplotlib.__version__) #checking version of installed matplotlib


xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints, ypoints)
plt.show() #prints out restuls of the graph points.

plt.savefig("plot.png")


plt.plot(xpoints,ypoints,'o')
plt.savefig("plot1.png") # Plotting without a line.