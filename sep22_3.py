import numpy as np

a = np.arange(1,21).reshape(4,5)

b = a[2:,:3]
print(b)