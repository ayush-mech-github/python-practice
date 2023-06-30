import numpy as np

# sum of two matrices
arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr2 = np.array([[3, 2, 1],
                [6, 5, 4],
                [9, 8, 7]])

print(arr1 + arr2)

# multiply elements to the corresponding elements
arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr2 = np.array([[3, 2, 1],
                [6, 5, 4],
                [9, 8, 7]])

print(arr1 * arr2)

# elementwise square root
arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(np.sqrt(arr1))

# sum of all elements
arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr1.sum())


# max of all elements
arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr1.max())

# finding an element
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(np.where(arr>5))

