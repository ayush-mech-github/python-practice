import numpy as np

# arange function
rng = np.arange(10)
print(rng)

# linspace function
lspace = np.linspace(1, 10, num=5)
print(lspace)

# empty function (assigns random values)
emp = np.empty((3, 5))
print(emp)

# empty_like function
emp_like = np.empty_like(rng)
print(emp_like)

# creating identity matrix
id = np.identity(5)
print(id)
print(id.shape)

# reshape and ravel function
arr = np.arange(99)
print(arr)
arr1 = arr.reshape(3, 3, 11)
print(arr1)
arr2=arr1.ravel()
print(arr2)
