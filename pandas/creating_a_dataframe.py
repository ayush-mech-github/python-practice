import numpy as np
import pandas as pd

# a series with random elements
ser = pd.Series(np.random.rand(25))
print(ser)
print(type(ser))

# a dataframe with random elements
df = pd.DataFrame(np.random.rand(10, 20))
print(df)
print(type(df))
print(df.index)
print(df.columns)

# transpose of dataframe
print(df.T)
