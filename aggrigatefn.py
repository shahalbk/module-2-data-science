import numpy as np

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print("sum of elements:",np.sum(a))

print("mean(average):",np.mean(a))


print('maximum value :',np.max(a))

print('minimum value:',np.min(a))

print("index of minimum value :",np.argmin(a))

print("index of maximum value:",np.argmax(a))

print("columnwise sum:",np.sum(a,axis=0))

print("rowwise sum:",np.sum(a,axis=1))

print('product of all elements:',np.prod(a))

print('size(count or how much elements in the array) of the array:',np.size(a))#or print(array.size)

rand_arr = np.random.randint(1,101,size=15)
print(rand_arr)