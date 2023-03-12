#always import matplotlib to use it. pip install matplotlib on terminal if not recognized in a text editor

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# making markers on each point of a graph to specifiy

ypoints = np.array([3,8,1,19])

# use marker = ''
plt.plot(ypoints, marker='*')
plt.show()

# format strings (fmt)

plt.plot(ypoints, 'o:r')
plt.show()

#marker size, marker color (mec) and marker facecolor (mfc)
# you can also use hex code for the colours
plt.plot(ypoints, marker='o', ms='20', mec = 'r', mfc='r')
plt.show()