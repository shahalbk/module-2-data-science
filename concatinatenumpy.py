import numpy as np

a = np.array([
    [1,2,3],
    [7,8,9]])
b = np.array([[4,5,6],[1,2,3]])

j = np.concatenate((a,b),axis=1)#default is 0(row)
print(j)