# DataQuest
# Data Visualization Basics
# Guided Project: Finding Heavy Traffic Indicators on Interstate 94

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pt 1
# the dataset

### MARKDOWN CELL ###
# Exploring I-94 traffic patterns: when one can expect slowdowns.
# This project will explore conditions and variables and how they impact traffic on westbound Interstate 94. I will look at several variables, such as weather, time of the day and week, etc., to find correlations with heavy traffic on the interstate.
## Useful Links
# https://en.wikipedia.org/wiki/Interstate_94
# https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume

# Dataset Information
# The dataset contains hourly westbound I-94 traffic volume near, what I assume is, mile marker 301, roughtly between Minneapolis and St. Paul, MN. The dataset includes hourly weather features and holidays for impacts on traffic volume.

# Data Dictionary
# holiday Categorical US National holidays plus regional holiday, Minnesota State Fair
# temp Numeric Average temp in kelvin
# rain_1h Numeric Amount in mm of rain that occurred in the hour
# snow_1h Numeric Amount in mm of snow that occurred in the hour
# clouds_all Numeric Percentage of cloud cover
# weather_main Categorical Short textual description of the current weather
# weather_description Categorical Longer textual description of the current weather
# date_time DateTime Hour of the data collected in local CST time
# traffic_volume Numeric Hourly I-94 ATR 301 reported westbound traffic volume

traffic_volume = pd.read_csv('Metro_Interstate_Traffic_Volume.csv')

# Examining the first and last five rows
print(traffic_volume.head())
print(traffic_volume.tail())
print('\n')
# Examining basic info for traffic_volume
print(traffic_volume.info())

# Pt 2
# Analyzing Traffic Volume

# Jupyter inline magic below, not needed here
# %matplotlib inline

# plotting traffic_volume column using pandas hist
traffic_volume['traffic_volume'].plot.hist()
plt.title('Traffic Volume Column')
plt.show()

# series.describe() to see basic stats of traffic_volume
print('\n')
print(traffic_volume['traffic_volume'].describe())
#
#- a few observations about the stats describe() and the histo:
#	- The traffic volume seems to reach peak, between ~6,500-7,200, with low frequency. 
#	- The highest volume frequencies are low traffic volumes, 0 to ~750 or ~1,250, and high-mid volumes, ~5,000. 
#		- The low-volume occurrences likely correspond to odd hours and the mid-high volumes likely correspond to rush hours.
#	- The average colume is ~3,200 vehicles.
#	- ~25% of time, traffic is ~1,200 vehicles or less
#	- ~25% of time, traffic is ~4x that, ~5,000 vehicles

# Pt 3
# Traffic Volume: Day vs. Night

# transforming date_time column using pd.to_datetime() function
traffic_volume['date_time'] = pd.to_datetime(traffic_volume['date_time'])

# use series.dt.hour property to get hour of every instance of date_time column
# isolate daytime data, isolate nighttime data

# day 0700 to less than 1900 hours
day_traffic = traffic_volume.copy()[(traffic_volume['date_time'].dt.hour >= 7) & (traffic_volume['date_time'].dt.hour < 19)]

# night 1900 to less than 0700
night_traffic = traffic_volume.copy()[(traffic_volume['date_time'].dt.hour >= 19) | (traffic_volume['date_time'].dt.hour < 7)]

print('\n')
print(day_traffic.tail())
print(night_traffic.head())

# Pt 4
# Traffic Volume: Day and Night
# Comparing traffic volume for the two approximate times of day.

# Plotting histograms for each sub dataset in 
plt.figure()
plt.subplot(2, 1, 1)
plt.hist(night_traffic['traffic_volume'])
plt.title('Night Traffic')
plt.ylabel('Frequency')
plt.xlabel('Traffic Volume')
plt.ylim(0,8000)
plt.xlim(0,8000)
plt.subplot(2, 1, 2)
plt.hist(day_traffic['traffic_volume'])
plt.title('Day Traffic')
plt.ylabel('Frequency')
plt.xlabel('Traffic Volume')
plt.ylim(0,8000)
plt.xlim(0,8000)
plt.show()

# series.describe() for both sub datasets
print('\n')
print('Night Traffic')
print(night_traffic['traffic_volume'].describe())
print('\n')
print('Day Traffic')
print(day_traffic['traffic_volume'].describe())

#- some observations
#	- shape of the histograms
#		- day traffic
#			- The histogram shows a relatively normal distribution with a slight left skew for the daytime traffic, 7 a.m. to 6:59 p.m. or 18:59 hours.
#			- Mid to high traffic volumes are much more prevalent during the daytime. On average, 4,762 vehicles pass by the station during the daytime hours. Rarely is there low traffic, but the traffic volume does peak to higher levels with some degree of frequency.
#		- night traffic
#			- The night traffic, 7 p.m. or 19:00 hours to 6:59 a.m., is right skewed. Most of the values fall in the frequency range to the right, nearer the y-axis origin.
#			- Traffic volume during the night tends to be sparse. The average traffic volume is 1,785 vehicles passing the station in any given nighttime hour. Though there are times of high traffic volume, low traffic volume is so much more prevalent during the night hours. 
#				- Should night traffic data still be used?
#					- Given the low frequency of high traffic volume during the nighttime hours, it may be beneficial to use this data to see what factors cause it this traffic volume to increase. And it may be easier to seek out those indicators for comparison to daytime hours.
# Pt 5
# Time Indicators

# Looking at traffic volume by month
# creating a new column 'month' using dt.month method on date_time column
day_traffic['month'] = day_traffic['date_time'].dt.month

# aggregate by month using groupby method and calc mean
day_by_month = day_traffic.groupby('month').mean()
print('\n')
print('Day Traffic')
print(day_by_month['traffic_volume'])

night_traffic['month'] = night_traffic['date_time'].dt.month
night_by_month = night_traffic.groupby('month').mean()
print('\n')
print('Night Traffic')
print(night_by_month['traffic_volume'])

# repeat for all traffic
traffic_volume_copy = traffic_volume.copy()
traffic_volume_copy['month'] = traffic_volume_copy['date_time'].dt.month
traffic_volume_by_month = traffic_volume_copy.groupby('month').mean()
print('\n')
print('All Traffic')
print(traffic_volume_by_month['traffic_volume'])

# plot via line
plt.figure()
plt.subplot(3, 1, 1)
night_by_month['traffic_volume'].plot.line()
plt.ylabel('Traffic Volume')
plt.title('Night traffic by month')
plt.subplot(3, 1, 2)
day_by_month['traffic_volume'].plot.line()
plt.ylabel('Traffic Volume')
plt.title('Day traffic by month')
plt.subplot(3, 1, 3)
traffic_volume_by_month['traffic_volume'].plot.line()
plt.ylabel('Traffic Volume')
plt.title('All traffic by month')
plt.show()

# Pt 6
# Time Indicators II, Day of the Week

# create new column 'dayofweek' to consist of the weekday, 0 is monday, 6 is sunday
day_traffic['dayofweek'] = day_traffic['date_time'].dt.dayofweek

# aggregate into a new df, grouped by day of week and avg calc'ed
day_traffic_dayofweek = day_traffic.groupby('dayofweek').mean()
print('\n')
print('Day Traffic Volume by Day of Week')
print(day_traffic_dayofweek['traffic_volume'])

# repeat above for night traffic
night_traffic['dayofweek'] = night_traffic['date_time'].dt.dayofweek
night_traffic_dayofweek = night_traffic.groupby('dayofweek').mean()
print('\n')
print('Night Traffic Volume by Day of Week')
print(night_traffic_dayofweek['traffic_volume'])

# repeat above for all traffic
traffic_volume_copy['dayofweek'] = traffic_volume_copy['date_time'].dt.dayofweek
traffic_dayofweek = traffic_volume_copy.groupby('dayofweek').mean()

# plot via line
plt.figure()
plt.subplot(3, 1, 1)
night_traffic_dayofweek['traffic_volume'].plot.line()
plt.ylabel('Traffic Volume')
plt.title('Night traffic by day of week')
plt.subplot(3, 1, 2)
day_traffic_dayofweek['traffic_volume'].plot.line()
plt.ylabel('Traffic Volume')
plt.title('Day traffic by day of week')
plt.subplot(3, 1, 3)
day_traffic_dayofweek['traffic_volume'].plot.line()
plt.ylabel('Traffic Volume')
plt.title('All traffic by day of week')
plt.show()

# Pt 7
# Time Indicators III

# creating hour of the day column
day_traffic['hour'] = day_traffic['date_time'].dt.hour
night_traffic['hour'] = night_traffic['date_time'].dt.hour
traffic_volume_copy['hour'] = traffic_volume_copy['date_time'].dt.hour

# limit by week and weekend days
day_traffic_weekdays = day_traffic.copy()[day_traffic['dayofweek'] <= 4] # 4 == Friday
night_traffic_weekdays = night_traffic.copy()[night_traffic['dayofweek'] <= 4]
traffic_weekdays = traffic_volume_copy.copy()[traffic_volume_copy['dayofweek'] <= 4]

day_traffic_weekends = day_traffic.copy()[day_traffic['dayofweek'] >= 5] # 5 == Saturday
night_traffic_weekends = night_traffic.copy()[night_traffic['dayofweek'] >= 5]
traffic_weekends = traffic_volume_copy.copy()[traffic_volume_copy['dayofweek'] >= 5]

# grouped by hour and calc'ed avg: weekdays and weekends
day_traffic_hours_weekdays = day_traffic_weekdays.groupby('hour').mean()
night_traffic_hours_weekdays = night_traffic_weekdays.groupby('hour').mean()
traffic_hours_weekdays = traffic_weekdays.groupby('hour').mean()

day_traffic_hours_weekends = day_traffic_weekdays.groupby('hour').mean()
night_traffic_hours_weekends = night_traffic_weekends.groupby('hour').mean()
traffic_hours_weekends = traffic_weekdays.groupby('hour').mean()

print('\n')
print('Day Traffic Volume by Hour, Weekdays')
print(day_traffic_hours_weekdays['traffic_volume'])
print('Day Traffic Volume by Hour, Weekends')
print(day_traffic_hours_weekends['traffic_volume'])
print('\n')
print('Night Traffic Volume by Hour, Weekdays')
print(night_traffic_hours_weekdays['traffic_volume'])
print('Night Traffic Volume by Hour, Weekends')
print(night_traffic_hours_weekends['traffic_volume'])
print('\n')
print('Traffic Volume by Hour, Weekdays')
print(traffic_hours_weekdays['traffic_volume'])
print('Traffic Volume by Hour, Weekends')
print(traffic_hours_weekends['traffic_volume'])

plt.figure(figsize=(10,12), layout='tight')
plt.subplot(3,2,1)
day_traffic_hours_weekdays['traffic_volume'].plot.line()
plt.xlim(6,20)
plt.ylim(0,6500)
plt.title('Day Traffic Volume by Hour: Weekdays')
plt.subplot(3,2,2)
day_traffic_hours_weekends['traffic_volume'].plot.line()
plt.xlim(6,20)
plt.ylim(0,6500)
plt.title('Day Traffic Volume by Hour: Weekends')
plt.subplot(3,2,3)
night_traffic_hours_weekdays['traffic_volume'].plot.line()
plt.xlim(0,24)
plt.ylim(0,6500)
plt.title('Night Traffic Volume by Hour: Weekdays')
plt.subplot(3,2,4)
night_traffic_hours_weekends['traffic_volume'].plot.line()
plt.xlim(0,24)
plt.ylim(0,6500)
plt.title('Night Traffic Volume by Hour: Weekends')
plt.subplot(3,2,5)
traffic_hours_weekdays['traffic_volume'].plot.line()
plt.xlim(0,24)
plt.ylim(0,6500)
plt.title('All Traffic Volume by Hour: Weekdays')
plt.subplot(3,2,6)
traffic_hours_weekends['traffic_volume'].plot.line()
plt.xlim(0,24)
plt.ylim(0,6500)
plt.title('All Traffic Volume by Hour: Weekends')
plt.show()

## Markdown about observations

# Pt 8
# Weather Indicators

# Find corr between traffic_volume and weather columns
print('\n')
print('Correlation: All Traffic')
print(traffic_volume.corr()['traffic_volume'][['temp', 'rain_1h', 'snow_1h', 'clouds_all']])
print('\n')
print('Correlation: Day Traffic')
print(day_traffic.corr()['traffic_volume'][['temp', 'rain_1h', 'snow_1h', 'clouds_all']])
print('\n')
print('Correlation: Night Traffic')
print(night_traffic.corr()['traffic_volume'][['temp', 'rain_1h', 'snow_1h', 'clouds_all']])
## corrolary values
# temp          0.130299
# rain_1h       0.004714
# snow_1h       0.000733
# clouds_all    0.067054

# plot scatter with column that has the strongest correlation
traffic_volume.plot.scatter(y='temp', x='traffic_volume')
plt.ylim(230,320) # errant 0K entries throw off the distribution
plt.show()

# Weather offers no strong indicators

# Pt 9
# Weather Types

# looking over weather_main and weather_description
print('\n')
print('A look at weather_main column')
print(traffic_volume['weather_main'].value_counts())
print('\n')
print(traffic_volume['weather_main'].describe())
print('\n')
print(traffic_volume['weather_main'].info())
print('\n')

print('\n')
print('A look at weather_description column')
print(traffic_volume['weather_description'].value_counts())
print('\n')
print(traffic_volume['weather_description'].describe())
print('\n')
print(traffic_volume['weather_description'].info())
print('\n')

# grouping these together and aggregating via mean
by_weather_main = day_traffic.groupby('weather_main').mean()
by_weather_description = day_traffic.groupby('weather_description').mean()

# plot horizontal bar for column traffic_volume of weather_main
by_weather_main['traffic_volume'].plot.barh()
plt.title('Traffic Volume by Weather Main')
plt.show()

# plot horizontal bar for column traffic_volume of weather_description
by_weather_description['traffic_volume'].plot.barh(figsize=(10,20))
plt.title('Traffic Volume by Weather Description')
plt.show()