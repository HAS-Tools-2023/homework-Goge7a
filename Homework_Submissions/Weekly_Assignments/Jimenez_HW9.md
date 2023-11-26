### Grade
4/9 -- I'm not sure what to do with this exactly. It looks like you have copied part of your python scrip into your markdown file. The assignment was to submit your script as a python script so that I can try to run it and to provide a markdown file with some reflections on questions I provided. I don't see any of the answers to the reflection questions here.  I didn't try to run your code since its not a python script but looking it over it looks like your relative paths would be broken from this directory. What I see included here like its the start of your forecast but its not meeting the requirements listed for your graded script (i.e. printing out your forecast values and providing plots). I am glad you were able to create a function though that looks great!

###

Code for function of timeseries
# %%

# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter

# %%
# Set the file name & path and read data
filename = '../data/streamflow_week_9.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week_9.txt'

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], 
        parse_dates=['datetime'])

# %%

# %%
# Read in the datetime for the dataframe
datai = data.copy()
datai = datai.set_index('datetime')

def monthly_median(dataframe, month, year=2023):
    monthly_vals = dataframe[(dataframe.index.month ==month)  &(dataframe.index.year == year)]
    median_val=np.median(monthly_vals['flow'])
    print('calculating median for month:', month, 'year', year)
    return(median_val)

# %%
# Value for the median of a given month and year
monthly_median(datai, 10, 2023)