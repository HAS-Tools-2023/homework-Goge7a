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