# reshaping---> chaning the dimension of an array without modifying the elements , no. of elements remains the same

"""
1.reshape(row,coloum) gives new array if the dimensions match
2.reshaping does not create the copy it gives us the view
3.doing the reshaping will effect the array
"""

import numpy as np

arr=np.array([1,2,3,4,5,6])
arr_reshaped=arr.reshape(2,3) 
print(arr_reshaped)