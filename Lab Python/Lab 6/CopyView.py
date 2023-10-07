import numpy as np

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
x = arr.view()
print(x)