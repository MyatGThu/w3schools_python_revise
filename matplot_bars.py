# Matplot Bars

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3,4,5,6])

plt.bar(x,y)
plt.show()


plt.barh(x,y)
plt.show()
