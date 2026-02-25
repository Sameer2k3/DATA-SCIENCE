'''
np.concantenate((array1,array2,axis=0))

axis = 0 mean vertical stacking in 2d 3d etc
axis= 1 means horizontal stacking in 2d 3d etc
'''

import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
new_arr=np.concatenate((arr1,arr2))

print(new_arr)
