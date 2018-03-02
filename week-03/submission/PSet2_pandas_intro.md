
```python
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# This line lets us plot on our ipython notebook
%matplotlib inline

# Read in the data

df = pd.read_csv('week-03/data/skyhook_2017-07.csv', sep=',')

# Create a new date column formatted as datetimes.
df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Determine which weekday a given date lands on, and adjust it to account for the fact that '0' in our hours field corresponds to Sunday, but .weekday() returns 0 for Monday.
df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)
df['weekday'].replace(7, 0, inplace = True)

# Remove hour variables outside of the 24-hour window corresponding to the day of the week a given date lands on.
for i in range(0, 168, 24):
  j = range(0,168,1)[i - 5]
  if (j > i):
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    ( (df['hour'] < j) & (df['hour'] > i + 18) ) |
    ( (df['hour'] > i + 18 ) & (df['hour'] < j) )
    )
    ].index, inplace = True)
  else:
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    (df['hour'] < j) | (df['hour'] > i + 18 )
    )
    ].index, inplace = True)
```

## Problem 1: Create a Bar Chart of Total Pings by Date

Your first task is to create a bar chart (not a line chart!) of the total count of GPS pings, collapsed by date. You'll have to use `.groupby` to collapse your table on the grouping variable and choose how to aggregate the `count` column. Your code should specify a color for the bar chart and your plot should have a title. Check out the [Pandas Visualization documentation](https://pandas.pydata.org/pandas-docs/stable/visualization.html) for some guidance regarding what parameters you can customize and what they do.

### Solution

```python
df.head()

df_sort = df['count'].groupby(by = df['date_new']).sum()
#checking that sums of grouped and raw are the same
df['count'].sum()
df_sort.sum()
#plot the graph with arguements
df_sort.plot(kind = 'bar', color = 'green', title = 'GPS Pings by Date')


```

## Problem 2: Modify the Hours Column

Your second task is to further clean the data. While we've successfully cleaned our data in one way (ridding it of values that are outside the 24-hour window that correspond to a given day of the week) it will be helpful to restructure our `hour` column in such a way that hours are listed in a more familiar 24-hour range. To do this, you'll want to more or less copy the structure of the code we used to remove data from hours outside of a given day's 24-hour window. You'll then want to use the [DataFrame's `replace` method](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html). Note that you can use lists in both `to_replace` and `value`.

After running your code, you should have either a new column in your DataFrame or new values in the 'hour' column. These should range from 0-23. You can test this out in a couple ways; the simplest is probably to `df['hour'].unique()`; if you're interested in seeing sums of total pings by hour, you can run `df.groupby('hour')['count'].sum()`.

### Solution

```python



#create a df copy to mangle
df_copy = df
df = df_copy

for i in range(0, 168, 24):
  j = range(0,168,1)[i - 5]
  if (j > i):
    df['hour'].replace(range(j, j + 5, 1), range(-5, 0, 1), inplace=True)
    df['hour'].replace(range(i, i + 19, 1), range(0, 19, 1), inplace=True)
  else:
    df['hour'].replace(range(j, j + 24, 1), range(-5, 19, 1), inplace=True)

'''
df['hour'].unique()

for i in range(0, 168, 24):
    #i-5 as index
    #ranges are exclusive on the right side, not inclusive
    j = range(0,168,1)[i-5]
    print(i,j)
    if (j > i):
        df['hour'].replace(range(i, i + 19, 1), range(5, 24, 1), inplace = True)
        df['hour'].replace(range(i,i+5,1),range(163,168,1), inplace=True)    
    else:
        df['hour'].replace(range(j, i+19, 1),range(0, 24, 1), inplace = True)
df['hour'].replace(range(163,168,1),range(0,5,1), inplace = True)
        # a range from x to y will be a list of values running from x to y-1
df.head()
list_check = df['hour'].unique()
list_check = sorted(set(list_check))
print(list_check)


print(i,j)
'''



```

## Problem 3: Create a Timestamp Column

Now that you have both a date and a time (stored in a more familiar 24-hour range), you can combine them to make a single timestamp. Because the columns in a `pandas` DataFrames are vectorized, this is a relatively simple matter of addition, with a single catch: you'll need to use `pd.to_timedelta` to convert your hours columns to a duration.

### Solution

```python
df.head()



df['timestamp'] = (df['date_new'] + (pd.to_timedelta(df['hour'],unit = 'h')))
df.head()
df['timestamp'].dtypes



```

## Problem 4: Create Two Line Charts of Activity by Hour

Create two more graphs. The first should be a **line plot** of **total activity** by your new `timestamp` field---in other words a line graph that displays the total number of GPS pings in each hour over the course of the week. The second should be a **bar chart** of **summed counts** by hours of the day---in other words, a bar chart displaying the sum of GPS pings occurring across locations for each of the day's 24 hours.

### Solution

```python
df_line = df.groupby(by=['timestamp']).sum()
df_line['count'].plot(color = 'purple', title = 'Pings by Time')

df_bar2 = df.groupby(by = df['hour']).sum()
df_bar2['count'].plot(kind = 'bar', color = 'blue', title = 'Total Pings by Hour of Day')



```

## Problem 5: Create a Scatter Plot of Shaded by Activity

Pick three times (or time ranges) and use the latitude and longitude to produce scatterplots of each. In each of these scatterplots, the size of the dot should correspond to the number of GPS pings. Find the [Scatterplot documentation here](http://pandas.pydata.org/pandas-docs/version/0.19.1/visualization.html#scatter-plot). You may also want to look into how to specify a pandas Timestamp (e.g., pd.Timestamp) so that you can write a mask that will filter your DataFrame appropriately. Start with the [Timestamp documentation](https://pandas.pydata.org/pandas-docs/stable/timeseries.html#timestamps-vs-time-spans)!

```python
df.head()
df_scat1 = df[df['timestamp'] == '2017-07-01 09:00:00']
df.dtypes
df_scat1.plot.scatter(x = 'lat', y = 'lon', color = 'blue', s = df_scat1['count']*0.4, title = 'Scatter Plot of Lat/Long and Ping Activity')


df_scat2 = df[df['timestamp'] == '2017-07-04 18:00:00']
df_scat2.plot.scatter(x = 'lat', y = 'lon', s = df_scat2['count']*0.4, color = 'red', title = 'Distribution of Pings at 6pm on the 4th of July')

df_scat3 = df[df['timestamp'] == '2017-07-20 09:00:00']
df_scat3.plot.scatter(x = 'lat', y = 'lon', s = df_scat3['count']*0.4, color = 'green', title = 'Distribution of Pings at 9am on the 20th of July')


```

## Problem 6: Analyze Your (Very) Preliminary Findings

For three of the visualizations you produced above, write a one or two paragraph analysis that identifies:

1. A phenomenon that the data make visible (for example, how location services are utilized over the course of a day and why this might by).
2. A shortcoming in the completeness of the data that becomes obvious when it is visualized.
3. How this data could help us identify vulnerabilities related to climate change in the greater Boston area.


In the plot of GPS Pings at 9am on the 20th of July, the visualization reveals a geographical distribution that would not have been obvious by scrolling through the data table. In particular, the road network appears very strongly, especially on graphs during commute hours. It is unclear exactly where the clusters correspond to on a map, and generally the edges of the data set pose a significant limitation for analysis. This data set appears to have been clipped by a polygon clipping shape rather than by a municipality border, resulting in unnatural straight edges along the right side of the graph. The graph of 6pm on July 4th shows a tremendous cluster along the edge of the Charles River, possibly of people watching fireworks.

In terms of our ability to assess climate vulnerabilities, this data provides a good starting point but is still relatively sparse. However, this does provide hotspots of human activity, which we see are often clustered along the coasts. These regions may be vulnerable to flooding in a storm surge, especially at night when weather is less salient to residents (because it's dark out). However, elevation is not available from this data set, and neither is movement. It is also clear that this data is not perfectly aligned with human activity, as there are large portions of Boston that appear as nearly empty.  
