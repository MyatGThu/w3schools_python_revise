# Matplot Bars

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3,4,5,6])

plt.bar(x,y)
plt.show()


plt.barh(x,y)
plt.show()

# Change width of the bars

plt.bar(x,y, width = 0.1)
plt.show()

plt.barh(x,y, height = 0.1)
plt.show()