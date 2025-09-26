import numpy as np

a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

f = a[(a>30) & (a<80)]
print(f)
print('sum is ',np.sum(f))