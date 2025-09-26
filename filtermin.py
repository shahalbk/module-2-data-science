import numpy as np

a = np.array([120,56,89,45,38,99,140,110])

f= a[a<100]
print(f)

print('minimum is ',np.min(f))