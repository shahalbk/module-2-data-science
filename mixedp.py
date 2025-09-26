import numpy as np

a = np.array([
    [1,2,2],
    [3,4,4],
    [5,6,6]
])

print(a.flatten())

b=np.unique(a)
print(b)

b = b.reshape(2,-1000000000000000000)#just give ,-1,-2,-3.....???whYYYYYYYYYYY
print(b)


print(np.transpose(b))
