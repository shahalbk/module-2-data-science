import numpy as np

a = np.identity(3)
print(a)
b = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a*b)
print(a@b)

