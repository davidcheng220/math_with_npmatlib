import numpy as np
import matplotlib.pyplot as plt

position = 100

scale = 5

size = 1000000

values = np.random.normal(position, scale, size)

plt.hist(values, 100)

plt.show()