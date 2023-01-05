import matplotllib.pyplot as plt
import numpy as np

xpoints = np.arrary([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints)
#prints out a line graph
plt.show()


# Without line [dot points] 'o' is notation for 

plt.plot(xpoints, ypoints, 'o')
plt.show()


# Multiple Points 

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints)
plt.show()

# Default Xpoints

ypoints = np.array([3,8,1,10,5,7])
plt.plot(ypoints)
plt.show()


