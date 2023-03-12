import matplotlib.pyplot as plt
import numpy as np

y = np.array([20,15,40,23])

#showing lables 
mylabels = ["Cannon", "Gun", "Tank", "Soilders"]


#explode
boom = [0.05,0.2,0.05,0.05]

#adding shadows
plt.pie(y, labels = mylabels, explode=boom, shadow=True)

#adding legends
plt.legend()
plt.show()

