import sys
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([1,2,3,4,5,6])
ypoints = np.array([7,1,2,34,6,7])

plt.plot(xpoints,ypoints, 'o')

plt.savefig("plot-noline.png")
