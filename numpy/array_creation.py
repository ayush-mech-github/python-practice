# creating array using list
import numpy as np
myArr = np.array([2, 3, 4, 5])
print(myArr)

# checking dimensions of array
print(myArr.ndim)

# checking number of bytes consumed
print(myArr.nbytes)

# checking shape,size and datatype of array
print(myArr.shape)
print(myArr.size)
print(myArr.dtype)

# changing element at an index
myArr[0] = 28
print(myArr)

# array with all elements zero
zeros = np.zeros((2, 4))
print(zeros)

# arange function
rng = np.arange(10)
print(rng)

# linspace function
lspace = np.linspace(1, 10)
print(lspace)
