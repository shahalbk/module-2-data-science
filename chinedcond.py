import numpy as np

a = np.random.randint(1,100,15)
print(a)
f = a[(a<20) | (a>80)]
print(f)
print('mean is ',np.mean(f),"sum is ",np.sum(f))