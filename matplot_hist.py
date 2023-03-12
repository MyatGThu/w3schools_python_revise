# Histograms using matplot

import matplotlib.pyplot as plt
import numpy as np

# Generating random array with 250 values where values will concentrate around 170 with a deviaition of 10. 

x = np.random.normal(170, 10, 250)

# print(x)

plt.hist(x)
plt.show()