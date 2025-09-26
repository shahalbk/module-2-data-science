import numpy as np

a = np.array([
    34,56,78,90,45,66,89,91,50
])

f = a[a>60]
print(f)
print(np.size(f))
print(f.size)

print('aveerage is ',np.mean(f))
