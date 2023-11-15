## Exercises for thursday's class
#%%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter
#%%
# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. 
# You should do this two ways: (1) by modifying the read.table function arguments directly. 
# (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
daymet_df = pd.read_csv('daymet.csv', names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                            parse_dates=['datetime'])


#%%
# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 
daymet_df = pd.read_csv('daymet.csv', index_col= 'date',
                        parse_dates=['date'])

#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 
print(daymet_df.info())

#2.3  Make a scatter plot of day length (dayl) vs maximum temperature.
ax=daymet_df.plot.scatter(x='dayl (s)', y='tmax (deg c)', 
colormap ='jet', marker = 'x')
ax.set_title("day vs temperature")

#%%
#2.4 Make a plot with lines for the monthly average of `tmax` for all months after Jan 2015.  
#Add shading to the plot extending to the monthly minimum and maximum of `tmax` for the same period.

# I tried to use the tips you gave and I couldn't get it

# This is the copied code from  the solutions. Ask about what ('M') means.
mean_val = daymet_df.resample('M').mean()['tmax (deg c)']
min_val = daymet_df.resample('M').min()['tmax (deg c)']
max_val = daymet_df.resample('M').max()['tmax (deg c)']

mean_val_plot = mean_val[mean_val.index.year>=2015]
min_val_plot = min_val[min_val.index.year>=2015]
max_val_plot = max_val[max_val.index.year>=2015]

ax=plt.axes()
plt.plot(mean_val_plot, 'o-', color='blue', label='Mean')
plt.fill_between(max_val_plot.index, min_val_plot.values, max_val_plot.values, color='grey',  alpha=0.2, label='Max-Min')
ax.set_xlabel("Date")
ax.set_ylabel("Monthly Maximum daily temperature")
ax.legend()

#Hint - Use the pandas resample function for datetime objects and the plt.fill type for the shading. 


# %%
