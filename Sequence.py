'''To check if a given sequence of the array row length is in the Numpy array or not...'''

import numpy as np
array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
# tolist converts array to list and list comparison is pretty easy
print([1, 2, 3, 4, 5] in array.tolist())
print([3, 4, 5, 6, 7] in array.tolist())

'''Now check if a given sequence of the smaller array row length is in the Numpy array or not...
            It should give true for [1, 2] in [1, 2, 3, 4]'''

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# Length and breadth of the given 2D array
l, b = 4, 4
a = [1, 2]
# length of the given substring
l1 = 2
# Evaluating breadth of the new formed 2D array
b1 = (int)((l * b)/l1)
# Given array reshaped into 8 x 2 matrix
arr = array.reshape((b1, l1))         # row x column
print("Reshaped Array :",arr.shape)
print(arr)
print([1, 2] in arr.tolist())     # It will give True
# Similar example of reshaping in the array
a = [1, 2, 3, 4, 5, 6, 7, 8]
l1 = 8
b1 = (int)(l * b/l1)
a1 = array.reshape((b1, l1))
print("Reshaped Array :",a1.shape)
print(a1)
print(a in a1.tolist())      # It will give True