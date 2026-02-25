# array[start,end,step]
# [::-1]  reverse the array
#[:: 2] [picks every 2nd element]

import numpy as np

arr=np.array([1,2,3,4,5,])

print(arr[1:5:2])
print(arr[:4])
print(arr[::-1])
