import numpy as np

# axis in array
x=[[1,2,3],
[4,5,6],
[7,8,9]]
arr=np.array(x)
print(x)

# sum of elements along row(0) and coloumn(1)
print(arr.sum(axis=0))
print(arr.sum(axis=1))

# transpose of array
print(arr.T)

# iterate all elements of array
arr.flat
for item in arr.flat:
    print(item)