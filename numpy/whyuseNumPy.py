# numpy provides efficient storage.
# it also provides better ways of handling data for processing.
# fast and easy to learn.
# uses relatively less memory to store data.

import numpy as np
import sys
py_arr=[2,3,4,5]
np_arr=np.array(py_arr)
x=sys.getsizeof(1)*len(py_arr)
print(x)
y=np_arr.itemsize*np_arr.size
print(y)