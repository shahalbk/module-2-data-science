import numpy as np

a = np.array([12,45,67,89,34,22,90,100])

val = a[(a>40) & (a<=90)]

print(val)
print(np.mean(val))