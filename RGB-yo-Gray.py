import matplotlib.pyplot as plt 
import numpy as np

I= np.array([[155, 155, 155], [155, 0, 155], [155, 155, 155], [155, 0, 0]])

plt.imshow(I, vmin=0, vmax=255)
plt.show()