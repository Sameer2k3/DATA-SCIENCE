'''
split(array,no of divisions) 

.hsplit()  for the horizontal splitting
.vsplit() for the vertical splitting
vsplit works only on the 2d or more dimensions array not 1d
'''
import numpy as np

arr=np.array([1,2,3,4,5,6])
print(np.hsplit(arr,3))
print(np.vsplit(arr,2))
