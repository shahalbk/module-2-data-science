import numpy as np

a = np.random.randint(10,100,12).reshape(3,4)
print(a)
f = a[a>50]
print('value greater than 50',f)
print('max is ',np.max(f))