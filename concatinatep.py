import numpy as np

a = np.array([100,20,30])
b = np.array([40,50,60])

c = np.concatenate((a,b),axis=0)
print(c)