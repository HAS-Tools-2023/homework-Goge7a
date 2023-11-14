#Map script
# %%
import matplotlib.pyplot as plt
import os
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx

# %%
# Reading it using geopandas
file =  os.path.join('gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)
#%%
# Lets checkout what we just got: 
# This is basically just a regular pandas dataframe but it has geometry
type(gages)
gages.head()
gages.columns
gages.shape #seeing how many entries there are
#%%
# Can see the geometry type of each row like this: 
gages.geom_type
# can see the projection here
gages.crs
# And the total spatial extent like this:
gages.total_bounds
# %% 
# Now to plot: 
fig, ax = plt.subplots(figsize=(10, 10))
gages.plot(ax=ax)
plt.show()

# For now lets just plot a subset of them 
# see what the state column contains
gages.STATE.unique()
gages_AZ=gages[gages['STATE']=='AZ']
gages_AZ.shape

#plot our subset
fig, ax = plt.subplots(figsize=(10, 10))
gages_AZ.plot(ax=ax)
plt.show()

# Could plot by some other variable: 
fig, ax = plt.subplots(figsize=(10, 10))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False, 
                legend=True, markersize=45, cmap='OrRd',
                ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
plt.show()
# %%
# Read in geodataframe
file = os.path.join('WBD_15_HU2_GDB.gdb')
#This will list all the layers in that file
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")
#%%
#Check the type and see the list of layers
type(HUC6)
HUC6.head()

#Then we can plot just one layer at atime
fig, ax = plt.subplots(figsize=(10, 10))
HUC6.plot(ax=ax)
ax.set_title("HUC Boundaries")
plt.show()

# %%
# Add some points
# UA:  32.22877495, -110.97688412
# Stream gauge:  34.44833333, -111.7891667
point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333]])
#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

#mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)


# plot these on the first dataset 
#Then we can plot just one layer at atime
fig, ax = plt.subplots(figsize=(10, 10))
HUC6.plot(ax=ax)
point_df.plot(ax=ax, color='red', marker='*')
ax.set_title("HUC Boundaries")
plt.show()

# %%
# Note this is a difernt projection system than the stream gauges
# CRS = Coordinate Reference System
HUC6.crs 
gages_AZ.crs


# Lets plot with more information this time:
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='Set2',
              ax=ax)
point_df.plot(ax=ax, color='r', marker='*')

# The points aren't showing up in AZ because they are in a different project
# We need to project them first
points_project = point_df.to_crs(gages_AZ.crs)
# NOTE: .to_crs() will only work if your original spatial object has a CRS assigned 
# to it AND if that CRS is the correct CRS!

# Now plot again
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='black', marker='*')

# %%
# Now put it all together on one plot
HUC6_project = HUC6.to_crs(gages_AZ.crs)


# Now plot again
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=25, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='black', marker='*')
HUC6_project.boundary.plot(ax=ax, color=None, 
                           edgecolor='black', linewidth=1)
# %%
# Adding a basemap:
# Now put it all together on one plot
HUC6_project = HUC6.to_crs(gages_AZ.crs)


# Now plot again
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=25, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='red', marker='*', label = 'UA and Forecast River' )
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=1,label = 'HUC6')
ax.legend()
ax.set_title('Map of AZ gages in Africa')
ctx.add_basemap(ax)

# %%
#Forecast Script. Week 11. 
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
filename = '../data/streamflow_week_11.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week_11.txt'

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
monthly_median(datai, 11, 2023)