import numpy as np

a = np.array([
    [50,60,40,89,90],
    [89,78,56,75,99]
])


marks = a[a>40]

print(marks)