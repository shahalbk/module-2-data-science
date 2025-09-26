import numpy as np

a = np.array([
    [23,45,67],
    [89,12,34],
    [56,78,90]
])

f = a[a%2==0]
print(f)
print('max is',max(f),'min is ',min(f))