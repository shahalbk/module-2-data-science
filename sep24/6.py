import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([
    10,20,30   #i thing here ,we extend the same row again using broadcasting.
])

c = a+b

print(c)