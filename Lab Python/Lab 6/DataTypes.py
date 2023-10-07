import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr1 = np.array([1, 2, 3, 4], dtype='S')
print(arr1)

arr2 = np.array([1.1, 2.1, 3.1])
newarr = arr2.astype('i')
print(newarr)