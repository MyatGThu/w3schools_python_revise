import matplotlib
import matplotlib.pyplot as plt # pip install matplotlib

print(matplotlib.__version__) #checking version of installed matplotlib

import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints, ypoints)
plt.show() #prints out restuls of the graph points
