import numpy as np

a = np.array([
    [1,2],
    [3,4],
    [7,8]
])

b = np.array([
    [5,6,1,2],
    [7,8,3,4]
])

c = a@b
print(np.shape(c))