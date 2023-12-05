#%%
# Import the Things!!! 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json
import urllib.request as req
#%%
# User input
site_code = '09506000'  # USGS site code for the streamflow location
# LC - Very cool! I love how you used the input function here to ask your user for something. 
forecast_date_input = input("Enter the forecast date (YYYY-MM-DD): ")
forecast_date = datetime.datetime.strptime(forecast_date_input, "%Y-%m-%d").date()
#%%
# Access USGS 
# LC - It looks like you have this setup in a bit of a complicated way where it is reading a json file and then having to parse that to create your dataframe. 
# you can do this much more simply following the exercise we did in class just by reading it into a dataframe directly. See examples from our starter codes and in class exercises on this. 
def get_usgs_data(site_code, start_date, end_date):
    """
    Retrieves USGS streamflow data for a specified time period.

    Parameters:
    - site_code (str): USGS site code for the streamflow location.
    - start_date (str): Start date in the format 'YYYY-MM-DD'.
    - end_date (str): End date in the format 'YYYY-MM-DD'.

    Returns:
    - pd.DataFrame: A DataFrame containing the retrieved streamflow data.
    """
    # USGS API URL
    url = 'https://waterservices.usgs.gov/nwis/dv/?format=json&sites=' + str(site_code) + '&startDT=' + str(start_date) + '&endDT=' + str(end_date) + '&parameterCd=00060'

    # Fetch data from the USGS API
    with req.urlopen(url) as response:
        data = json.load(response)

    # Extract relevant information from the JSON response
    values = data['value']['timeSeries'][0]['values'][0]['value']
    dates = [entry['dateTime'] for entry in values]
    flow_values = [float(entry['value']) for entry in values]

    # Create a DataFrame
    df = pd.DataFrame({'Date': dates, 'Flow(cfs)': flow_values})
    df['Date'] = pd.to_datetime(df['Date'])

    return df
# %%
# Forecast Prediction
# LC it seems like this function needs a different name or needs to be two functions because in addition ot plotting the streamflow it is also calculating the forecast
def plot_streamflow(data, forecast_date):
    """
    Plots the streamflow data and predicts streamflow for the next week and the following week.

    Parameters:
    - data (pd.DataFrame): DataFrame containing streamflow data.
    - forecast_date (str): Forecast date in the format 'YYYY-MM-DD'.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Flow(cfs)'], label='Observed Flow')
    plt.axvline(pd.to_datetime(forecast_date), color='red', linestyle='--', label='Forecast Date')
    
    # Predict streamflow for next week and following week using median of previous years
    previous_years_data = data[data['Date'].dt.year != forecast_date.year]
    median_flow = previous_years_data.groupby(previous_years_data['Date'].dt.dayofyear)['Flow(cfs)'].median()

    # Extract day of the year for the forecast date
    day_of_year = forecast_date.timetuple().tm_yday

    # Predict streamflow for the next week and the following week
    predicted_next_week = median_flow.get(day_of_year, np.nan)
    predicted_following_week = median_flow.get((day_of_year + 7) % 365, np.nan)
    
    print(f"Predicted Streamflow for Next Week: {predicted_next_week} cfs")
    print(f"Predicted Streamflow for Following Week: {predicted_following_week} cfs")
#%%
# Time to Graph.
# LC Not sure what these lines of code are doing as there is nothing thats actually being plotted yet (the function has not been called yet its just been defined)
plt.title('USGS Streamflow Data and Forecast')
plt.xlabel('Date')
plt.ylabel('Flow (cfs)')
plt.legend()
plt.grid(True)
plt.show()

# Specify the week for the forecast. 
# LC - if you already have a variable called forecast_date defined there is no need to create a new variable with a different name here just use the one you already have. 
forecast_start_date = forecast_date
forecast_end_date = forecast_start_date + pd.DateOffset(days=13)  # Next week and following week

# Get historical data
# This takes the date that the user entered and substracts a year from it so the graph is only over the span of a year. 
start_date = (forecast_start_date - pd.DateOffset(years=1)).strftime('%Y-%m-%d')
end_date = (forecast_end_date - pd.DateOffset(days=1)).strftime('%Y-%m-%d')
historical_data = get_usgs_data(site_code, start_date, end_date)

# Plot historical data and predictions
plot_streamflow(historical_data, forecast_date)


# %%
