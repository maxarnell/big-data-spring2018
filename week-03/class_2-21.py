#class notes 2-21-18
import pandas as pd
import numpy as np
#standard references
import matplotlib
%matplotlib inline

new_list = []
df = pd.DataFrame()
print(df)

df['name'] = ['Bilbo', 'Frodo', 'Samwise']

#linking new data with a list
df.assign(height = [0.5, 0.4, 0.6])

#bring csv into file, seperator def as comma
df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')

#if you wanted to change working directory
import os
# os.chdir

#examine first 5 rows
df.head()

#dimensions of data frame
df.shape

#number of columns in row 1
df.shape[1]

#names of columns
df.columns

#what are the possible values of cat_name
df['cat_name'].unique()

#hour is in weeks, so out of 167
df['hour'] == 158
#this is a Mask. This is a boolean test of whether each row has hour == 158

#to create subset of data based on mask, we pass a mask to the data frame
one_fifty_eight = df[df['hour'] == 158]


one_fifty_eight.shape

#more specific mask, only more than 50 pings in the area

(df['hour'] == 158) & (df['count'] > 50)

#pandas convention and &   or |  not !


#this is a query, it does not overwrite
df[(df['hour'] == 158) & (df['count'] > 50)].shape

bastille = df[df['date'] == '2017-07-14']
bastille.head()

#greater than average cells MASK
bastille['count'] > bastille['count'].mean()

#greater than avg data DataFrame
lovers_of_bastille = bastille[bastille['count'] > bastille['count'].mean()]

#summary statistics
lovers_of_bastille['count'].describe()

#groupby method to collapse rows by shared column values
#collapse full df by date, sum count values on each day
df.groupby('date')['count'].sum()

#plot of grouped data, summed by day
df.groupby('date')['count'].sum().plot()

df['count'].max()
df['count'].min()
#.mean .std .count

#hours are weird, done by week
df['hour'].unique()

jul_sec = df[df['date'] == '2017-07-02']

jul_sec.groupby('hour')['count'].sum().plot()

#convert date string to machine readable timestamp
df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

#create new column 'weekday' using machine readable 'date_new'
#lambda means all that follows acts like a function, applied to every value in 'date_new'
#default .weekday() function is monday-sunday, our data is sunday-saturday. Add one.
df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)
#replacing 7 with 0
df['weekday'].replace(7, 0, inplace = True)

#iterating over hours in week by 24s
for i in range(0, 168, 24):
    df.drop(df[df['weekday'] == (i/24) &
    (
    (df['hour']) , i 
    )
    ])
