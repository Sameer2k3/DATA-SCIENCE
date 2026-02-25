'''
np.delete(array,index,axis)
'''

import numpy as np

arr=np.array([1,2,3,4,5,6])
deleted=np.delete(arr,2) # removes the element at the index 2
print(deleted)