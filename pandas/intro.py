import numpy as np
import pandas as pd

dict1 = {'name': ['ayush', 'ankit', 'parashar', 'dishant'],
         'city': ['lucknow', 'chitrakoot', 'agra', 'bulandshahar'],
         'marks': [28, 25, 26, 25]
         }

# making a dataframe
df = pd.DataFrame(dict1)
print(df)

# making an excel sheet
df.to_csv('friends.csv')

# making an excel sheet without index
df.to_csv('friends_index_false.csv', index=False)

# to see rows at beginning or end only
print(df.head(2))
print(df.tail(2))

# to statistically analyze the data
print(df.describe())

# to change indices
df.index=['first','second','third','fourth']
print(df)
