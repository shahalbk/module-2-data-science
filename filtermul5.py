import numpy as np

a = np.random.randint(1,101,25).reshape(5,5)
print(a)
f = a[a%5==0]
print(f)