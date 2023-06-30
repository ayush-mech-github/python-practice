# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:03:28 2021

@author: AAYUSH pc
"""


#ANKIT TRIPATHI 1803240021
import numpy as np
  # create numpy 2d-array
m = np.array([[1, 2, 3],
              [2, 3, 4],
              [4, 5, 6]])
print("Printing the Original square array:\n",m)
  # finding eigenvalues and eigenvectors
w, v = np.linalg.eig(m)
  # printing eigen values
print("Printing the Eigen values of the given square array:\n",w)
  # printing eigen vectors
print("Printing Right eigenvectors of the given square array:\n",v)