import numpy as np

a = np.array([
    [50,60,40,89,90],
    [89,78,56,75,99]
])


marks = a[a>40]

print(marks)

new_mark = a[(a>40) & (a<90)]
print(new_mark)

new_mark = a[(a<50) | (a>90)]
print(new_mark)

updated_marks = a[~(a<60)]

print(updated_marks)