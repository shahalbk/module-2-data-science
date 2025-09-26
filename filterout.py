import numpy as np

a = np.array([12,45,60,75,30,95,100,20])

f = a[(a<40) | (a>90)]
print(f,'and count is ',np.size(f))