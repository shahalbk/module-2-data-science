import numpy as np

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([
    [4,5,6]
])

c = a@b

print(c)

print(np.shape(a))
print(np.shape(b))

print(np.matmul(a,b))