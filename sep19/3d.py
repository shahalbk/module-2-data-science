#accessing 5 nad 9 from 3d
import numpy as np
l = [
    [[1,2,3],[4,5,6]], #0
    [[8,9,10],[6,5,4]] #1
]

a =np.array(l)

print(a[0,1,1])
print(a[1,0,1])