import numpy as np 

temp = np.array([46, 23, 87, 46, 220])
average = np.mean(temp)

print(average)

# creating array with default values
zeroes=np.zeros(3)
print(zeroes)

# 1 as default values
ones=np.ones((2,3)) #array of 2d
print(ones)

# array with any specific number
specific=np.full((2,3),9) #array of 9 as default value
print(specific)