import numpy as np

a = np.array(
    [45,78,23,90,67,88,34,59]
)

mark = a[a>50]
print(mark)
print(np.sum(mark))