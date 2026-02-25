"""
flattening is used to convert a multi dimensinal array into a 1d array

ravel()-->views
flatten()--->copy

"""
import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

print(arr.ravel())
print(arr.flatten())
