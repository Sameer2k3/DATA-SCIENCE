# boolean masking picks the elements on the basis of the certain condition provided by us

import numpy as np

arr=np.array([1,2,3,4,5,6])

print(arr[arr>4]) # all elements greater than 4
print(arr[arr>=2])  # all elements above 2