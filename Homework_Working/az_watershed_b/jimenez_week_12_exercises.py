# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
#import dataretrieval.nwis as nwis

# %%
# Exercise 1: 
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 
def streamflow(site, start, end):
    url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
          "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates=['datetime'], index_col=['datetime'])
    return data

# Example usage
site = '09506000'
start = '1989-01-01'
end = '2020-10-16'

result = streamflow(site, start, end)
print(result.head())
#%%
# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 
data_gauge1 = streamflow('09506000', start, end)
data_gauge2 = streamflow('09504000', start, end)
data_gauge3 = streamflow('09504950', start, end)

# Print the first few rows of each dataset for verification
print("Data for Gauge 09506000:")
print(data_gauge1.head())

print("\nData for Gauge 09504000:")
print(data_gauge2.head())

print("\nData for Gauge 09504950:")
print(data_gauge3.head())
#%%
#3. Make a timeseries plot showing the data from all 3 gauges. 
plt.figure(figsize=(12, 6))

plt.plot(data_gauge1.index, data_gauge1['flow'], label='Gauge 09506000')
plt.plot(data_gauge2.index, data_gauge2['flow'], label='Gauge 09504000')
plt.plot(data_gauge3.index, data_gauge3['flow'], label='Gauge 09504950')

# Customize the plot
plt.xlabel('Date')
plt.ylabel('Flow')
plt.title('Streamflow Time Series for Three Gauges')
plt.legend()

plt.show()

# %%
