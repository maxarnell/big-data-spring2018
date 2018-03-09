import json
import time
import threading
import tweepy
import jsonpickle
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import os
path='C:/Users/maxar_000/Desktop/github/big-data-spring2018/week-04'
os.chdir(path)
from twitter_keys import api_key, api_secret


def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api

api = auth(api_key, api_secret)

def parse_tweet(tweet):
  p = pd.Series()
  if tweet.coordinates != None:
    p['lat'] = tweet.coordinates['coordinates'][0]
    p['lon'] = tweet.coordinates['coordinates'][1]
  else:
    p['lat'] = None
    p['lon'] = None
  p['location'] = tweet.user.location
  p['id'] = tweet.id_str
  p['content'] = tweet.text
  p['user'] = tweet.user.screen_name
  p['user_id'] = tweet.user.id_str
  p['time'] = str(tweet.created_at)
  return p

def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True:
            with open(out_file, 'w') as f:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets


# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000

#downloading 80000 tweets took over 3 hours, make sure not to run this accidentally
tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

#Run this line after running the code
tweets.to_json('C:/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/data/tweets.json')

# Check how many tweets were Downloaded
len(tweets)
tweets.shape
tweets.head()


def parse_tweet(tweet):
  p = pd.Series()
  if tweet.coordinates != None:
    p['lat'] = tweet.coordinates['coordinates'][0]
    p['lon'] = tweet.coordinates['coordinates'][1]
  else:
    p['lat'] = None
    p['lon'] = None
  p['location'] = tweet.user.location
  p['id'] = tweet.id_str
  p['content'] = tweet.text
  p['user'] = tweet.user.screen_name
  p['user_id'] = tweet.user.id_str
  p['time'] = str(tweet.created_at)
  return p

tweets.head()

tweets['location'].unique()


#Data Reload
dfmain = pd.read_json('/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/data/tweets.json')

#duplicate removal
dfmain[dfmain.duplicated(subset = 'content', keep = False)]
dfmain.drop_duplicates(subset = 'content', keep = False, inplace = True)

#cleaners
bos_list = dfmain[dfmain['location'].str.contains('Boston', case = False)]['location']
dfmain['location'].replace(bos_list, 'Boston', inplace = True)


camb_list = dfmain[dfmain['location'].str.contains('Cambridge', case = False)]['location']
dfmain['location'].replace(camb_list, 'Cambridge', inplace = True)

som_list = dfmain[dfmain['location'].str.contains('Somerville', case = False)]['location']
dfmain['location'].replace(som_list, 'Somerville', inplace = True)

#MA clean with help from Megan
ma_list = dfmain[dfmain['location'].str.endswith('MA')]['location']
dfmain['location'].replace(ma_list, 'Other Mass.', inplace = True)

states = pd.read_csv('/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/data/states.csv')
us_list_end = states['Abbreviation']
us_end = us_list_end.values.tolist()
us_end_t = tuple(us_end)
us_list = dfmain[dfmain['location'].str.endswith(us_end_t)]['location']
dfmain['location'].replace(us_list, 'USA', inplace = True)

us_st_end = states['State']
st_name = us_st_end.values.tolist()
st_t = tuple(st_name)
st_list = dfmain[dfmain['location'].str.endswith(st_t)]['location']
dfmain['location'].replace(st_list, 'USA', inplace = True)

usa_list = dfmain[dfmain['location'].str.contains('usa|USA|Usa', case = False)]['location']
dfmain['location'].replace(usa_list, 'USA', inplace = True)

# city_list = ['Boston', 'Cambridge', 'Somerville', 'United States', 'Other Mass.']
# city_list_t = tuple(city_list)
# type(city_list_t)
#other block
other_list = dfmain[~dfmain['location'].str.contains('Boston|Cambridge|USA|Somerville|Other Mass.')]['location']
dfmain['location'].replace(other_list, 'Other', inplace = True)
#
# loc_tweets = tweets[tweets['location'] != '']
# count_tweets = loc_tweets.groupby('location')['id'].count()
# df_count_tweets = count_tweets.to_frame()
# df_count_tweets
# df_count_tweets.columns
# df_count_tweets.columns = ['count']
# other_list = df_count_tweets['count'] < 10
# other_keys = other_list.keys
# other_keys
# dfmain['location'].replace(other, 'Other', inplace = True, regex = True)
#

# df_loc = dfmain[dfmain['location'] != '']
# count_tweets = df_loc.groupby('location')['id'].count()
# df_count_tweets = count_tweets.to_frame()
# df_count_tweets.dtypes
# other_list = df_count_tweets[df_count_tweets['id'].between(0,10)]
# other_list
# dfmain['location'].replace(other_list2, 'Other', inplace = True)
# other = "Other"
# other_list2 = dfmain['location'].where((df_count_tweets['count'] > 10), other)
# dfmain['location']
#run after cleaning
df_loc = dfmain[dfmain['location'] != '']
count_tweets = df_loc.groupby('location')['id'].count()
df_count_tweets = count_tweets.to_frame()
df_count_tweets
df_count_tweets.columns
df_count_tweets.columns = ['count']
df_count_tweets.sort_values(by = 'count')
df_clean = df_count_tweets
df_clean


#plots
list(df_clean.index)
plt.pie(df_clean['count'], labels = df_clean.index, shadow = True)
plt.axis('equal')
plt.title('Distribution of Tweets by Reported Location')
plt.show()


dfmain.head()
lon_uni = dfmain['lon'].unique()
lat_uni = dfmain['lat'].unique()

plt.scatter(lat_uni, lon_uni)
plt.title('Geolocation of Tweets')
plt.show()




#search term for snow


# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/term.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000

snow = 'snow'

#downloading 80000 tweets took over 3 hours, make sure not to run this accidentally
climate_tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name,
  search_term = snow
  )

#Run this line after running the code
climate_tweets.to_json('C:/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/data/term.json')

dfterm = pd.read_json('C:/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/data/term.json')

dfterm[dfterm.duplicated(subset = 'content', keep = False)]
dfterm.drop_duplicates(subset = 'content', keep = False, inplace = True)

#Snow cleaners
bos_list2 = dfterm[dfterm['location'].str.contains('Boston', case = False)]['location']
dfterm['location'].replace(bos_list2, 'Boston', inplace = True)

camb_list2 = dfterm[dfterm['location'].str.contains('Cambridge', case = False)]['location']
dfterm['location'].replace(camb_list2, 'Cambridge', inplace = True)

som_list2 = dfterm[dfterm['location'].str.contains('Somerville', case = False)]['location']
dfterm['location'].replace(som_list2, 'Somerville', inplace = True)

#MA clean with help from Megan
ma_list2 = dfterm[dfterm['location'].str.endswith('MA')]['location']
dfterm['location'].replace(ma_list2, 'Other Mass.', inplace = True)

states = pd.read_csv('/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/data/states.csv')
us_list_end = states['Abbreviation']
us_end = us_list_end.values.tolist()
us_end_t = tuple(us_end)
us_list2 = dfterm[dfterm['location'].str.endswith(us_end_t)]['location']
dfterm['location'].replace(us_list2, 'USA', inplace = True)

us_st_end = states['State']
st_name = us_st_end.values.tolist()
st_t = tuple(st_name)
st_list2 = dfterm[dfterm['location'].str.endswith(st_t)]['location']
dfterm['location'].replace(st_list2, 'USA', inplace = True)

usa_list2 = dfterm[dfterm['location'].str.contains('usa|USA|Usa', case = False)]['location']
dfterm['location'].replace(usa_list2, 'USA', inplace = True)

# city_list = ['Boston', 'Cambridge', 'Somerville', 'United States', 'Other Mass.']
# city_list_t = tuple(city_list)
# type(city_list_t)
#other block
other_list2 = dfterm[~dfterm['location'].str.contains('Boston|Cambridge|USA|Somerville|Other Mass.')]['location']
dfterm['location'].replace(other_list2, 'Other', inplace = True)
#

#run after cleaning
df_loc2 = dfterm[dfterm['location'] != '']
count_tweets2 = df_loc2.groupby('location')['id'].count()
df_count_tweets2 = count_tweets2.to_frame()
df_count_tweets2
df_count_tweets2.columns
df_count_tweets2.columns = ['count']
df_count_tweets2.sort_values(by = 'count')
df_clean2 = df_count_tweets2
df_clean2


#plots
list(df_clean2.index)
plt.pie(df_clean2['count'], labels = df_clean2.index, shadow = True)
plt.axis('equal')
plt.title('Distribution of "Snow" Tweets by Reported Location')
plt.show()


dfterm.head()
lon_uni2 = dfterm['lon'].unique()
lat_uni2 = dfterm['lat'].unique()

plt.scatter(lat_uni2, lon_uni2)
plt.title('Geolocation of "Snow" Tweets')
plt.show()


#Export to csv
dfmain.to_csv('C:/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/submission/twitter_data.csv', sep=',', encoding = 'utf-8')
dfterm.to_csv('C:/Users/maxar_000/Desktop/github/big-data-spring2018/week-04/submission/snow_twitter_data.csv', sep=',', encoding = 'utf-8')
