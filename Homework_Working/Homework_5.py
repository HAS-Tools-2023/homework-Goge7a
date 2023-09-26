# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('../data/', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7
#flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==7))


criteria = (flow_data[:, 0] >= 2015) & (flow_data[:, 0] <= 2019)
flow_5yr = flow_data[criteria, :]
flow_mean = np.mean(flow_5yr[:,3])
print(flow_5yr.shape)
print(flow_mean)


# Calculate the average flow for these same criteria 
#%%
flow_5yr[:,3]*86400
#%%
flow_monthly = np.zeros((60,3))
flow_monthly[:,0]= np.repeat(np.arange(2015,2020),12)

flow_monthly[:,1]= np.tile(np.arange(1,13),5)

for i in range(60):
    ytemp = flow_monthly[i,0]
    mtemp =flow_monthly[i,1]
    print(ytemp,mtemp)
    ilist=(flow_5yr[:,0]==ytemp) & (flow_5yr[:,1]==mtemp)
    flow_monthly[i,2] = np.nanmean(flow_5yr[ilist,3])
    print(ytemp, mtemp, flow_monthly[i,2])
    
print(flow_monthly[0:5,:])    




# %%
