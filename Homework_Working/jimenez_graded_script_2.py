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
forecast_date_input = input("Enter the forecast date (YYYY-MM-DD): ")
forecast_date = datetime.datetime.strptime(forecast_date_input, "%Y-%m-%d").date()
#%%
# Access USGS 
# Originally ChatGPT used an 'f' in front of the https portion. I changed it back to the way we did it in class using plus signs, since 'f' did not make sense to me. 
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
# The docstring did not quite make sense to me so I used ChatGPT to help me write it.
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
    
    # I was trying to use a numpy function to help me with line and could not figure it out so ChatGPT used this for the lines of code to get it to work. 
    print(f"Predicted Streamflow for Next Week: {predicted_next_week} cfs")
    print(f"Predicted Streamflow for Following Week: {predicted_following_week} cfs")
#%%
# Time to Graph.
    plt.title('USGS Streamflow Data and Forecast')
    plt.xlabel('Date')
    plt.ylabel('Flow (cfs)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Specify the week for the forecast. 
# I wanted to graph to look nice. I was not sure how to structure this at first since I wanted to use < , > but doing it this way really helped me get the graph that I wanted to get. 
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