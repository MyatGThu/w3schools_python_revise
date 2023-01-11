import sys
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.image as mpimg

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,5,7,9])

plt.plot(xpoints,ypoints)
plt.savefig("multi-plots.png")

image_path = "multi-plots.png"
image = mpimg.imread(image_path)
plt.imshow(image)