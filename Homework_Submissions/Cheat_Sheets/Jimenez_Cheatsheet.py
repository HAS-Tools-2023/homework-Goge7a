# %%
# Because why not...
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter
#%%
#### Numpy: 
#  - The general purpose of the numpy library : 
#       numpy has a database that can perform functions such as finding the mean or average of data
#  - What numpy array's are and what kinds of things they can (and can't contain)
#       numpy arrrays are data type object. They can contain lists and they can't contain 
#  - Various approaches for how to slice a numpy array (e.g. grabbing out a row, column, range of values)
#       Using [:,3] for example would grab the third column for each row. In the bracket is row, column
#  - How to create a numpy array from scratch (please show at least 2 options)
#       np.array([1,2,3]) -just lists the array 1,2,3
#       np.linspace([0,10,num=5]) - np.linspace is usual especially for graphing in this case there would be an axis from 0-10 with 5 intervals in between those numbers.
#  - List 5-6 helpful numpy functions and what they do
#       np.linspace() - explained above 
#       np.mean() - calculates the mean of an array
#       np.median() -calculates the median of an array
#       np.zeros() - used to create a matrix full of zeroes
#       np.arange() - creates an instance of ndarray with evenly spaced values and returns the reference to it
#       np.std() - calculates the standard deviation of values in an array 

# %%
#### Pandas
#  - The general purpose of the Pandas library
#       it makes working with data sets much easier
#  - What makes a pandas data frame is different from a numpy array
#       numpy arrays can be multidimensional and dataframes are only 2D
#  - An explanation of what the 'index' of a dataframe and why its different from other columns
#       the index refers to the dataframe rows which are usually integers or strings whereas the other columns are typically strings
#  - How to setup a pandas dataframe by reading a file
#        pd.DataFrame 
#  - How to see the index of a pandas dataframe
#       set dataframe to be index_list (or something else) and use a print statement like print(index_list)
#  - How to slice a pandas dataframe: 
#    - using loc and iloc to get rows 
#       loc = selects rows and columns with specific labels, iloc = selects rows and columns specific integers positions
#    - grabbing out columns by name or number
#       using loc for two columns i.e. 'datetime' and 'streamflow' would provide the column name and values
#  - 5-6 helpful pandas functions or methods that you can use to inspect your dataframe (list each and explain what it does)
#       head()function - calculates the first value(s) of the dataframe
#       tail()function - calculates the last value(s) of the dataframe
#       dtypes()function - tells you the data type of each column
#       loc()function - used to access rows or columns of a dataframe
#       iloc()function - used to retrieve rows of a dataframe 