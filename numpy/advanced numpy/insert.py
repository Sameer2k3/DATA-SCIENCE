# inserting a new element in array
# np.insert(array,index,value,axis)
'''
for 1d axis is none by default
for 2d use  0 for row insetion and 1 for the coloum insertion
'''

import numpy as np

arr=np.array([1,2,3,4,5,6])

new_arr=np.insert(arr,2,500)
print(new_arr)
