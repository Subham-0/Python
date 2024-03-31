                #    """ PANDAS"""
""" It is a python library which is used for tabular format. Where the dates from xlfile or any other file will be retrive and will be stored in a tabular format(data frame). Necessity of this package is arrise because python application when it for data analytics meet to intract with the database so the best part is to connect to the data frame of pandas as both are written in python language(application,pandas) then it is a better compatibility.

- For using pandas we have to install, then the methods are to be used.

We have to imported two libraries pandas and numpy
    - we are using an array of numpy , so that one array will be created
    - we are using function as a series of pandas and passing two parameters
            1 - data(dataset)
            2 - index
"""

#Example1

import pandas as pd 
import numpy as np
data = np.array(["a","b","c","d"])
s= pd.Series(data,index=[100,101,102,103])
print(s)

#Example2
import pandas as pd 
info = {
    "one":pd.Series([1,2,5],index= ['a','b','c']),
    "two":pd.Series([1,2,3],index= ['a','b','c'])
}
print(type(info))
print(info)
df = pd.DataFrame(info)
print(df)

#Example3
data = {
    "calories":[400,350,300],
    "minutes":[40,35,30]
}
print(data)
df= pd.DataFrame(data,index=["Day1","Day2","Day3"])
print(df)


# #Deleting a Column
# del df["minutes"]
# print(df) 

# # or
# df.pop("calories")
# print(df)

#How to get perticular column values by using local function
print(df.loc[["Day1","Day2"]])
