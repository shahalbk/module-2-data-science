import numpy as np

l = [
    [1,2,3,8,0],
    [4,5,6,9,7]
]

a = np.array(l)

print(a[1,1:4])
print(a[0:2,1:4])