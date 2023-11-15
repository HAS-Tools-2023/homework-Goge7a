# %%
#Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week_8.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = 'C:\HAS501\homework-Goge7a_H\data\streamflow_week_8.txt'

# %%
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)
# %%
## Plot 1: Histogram 
oct_flow = data[(data['month']==10) & (data['year'] >= 2010)]
mybins = np.linspace(0, (np.mean(oct_flow["flow"])), num=15)
plt.hist((oct_flow["flow"]), bins=mybins)
plt.title('Streamflow')
plt.ylabel('Count')
plt.xlabel("mean flow")
# %%
## Plot 2: Scatter

oct_flow2 = data[(data['month'] == 10) & (data['year'] >= 2010)].groupby('datetime')['flow'].mean()

oct_flow2.plot(x='datetime', y='flow')
plt.xlabel('datetime')
plt.ylabel('mean flow')
plt.title('hydrograph')
# %%
