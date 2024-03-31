import pandas as pd

# Creating two sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Appending DataFrames using append method
result = df1.append(df2, ignore_index=True)

print(result)