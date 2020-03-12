#%%











import math

A = 9

print( math.sqrt(9))
print( math.sqrt(9))
print(math.log2(A))


import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0,2 * math.pi)
y = np.sin(x)

plt.plot(x,y)

import seaborn as sns

sns.barplot(x=x, y=y)
