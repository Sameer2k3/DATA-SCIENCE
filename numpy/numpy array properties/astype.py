# used to convert the datatype of the elements of the array 

import numpy as np 

arr=np.array([1.3,6,6.9])
arr_new=arr.astype(int)

print(arr)
print(arr.dtype)

print(arr_new)
print(arr_new.dtype)