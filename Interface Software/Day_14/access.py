import pandas as pd
#How to access the csv file?(Comma Separated values)
# 1- find the csv File
# 2- keep that csv file inside your working directory
# 3- access the by pandas read_csv function
# 4- then do your filtering in that data
# 5- Make sure your directory should where the scv file
    # ex-1

df = pd.read_csv("locations.csv")
print(df)
print(df.head())    
print(df.head(10))
print(df.tail())
print(df.info())

#Forward slicing and Backward slicing
df1 = df[1:3]
print(df1)
df2 = df[-1:]
print(df2)

