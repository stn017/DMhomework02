#!/usr/bin/env python
# coding: utf-8

# # Data Sources
# import data
# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
wine_reviews = pd.read_csv("./data/winemag-data-130k-v2.csv", index_col=0)
wine_reviews


# # Transform into a form suitable for mining association rules
# For 129,971 data items, set minsup = 1200
# In[2]:


minsup = 1200

# Nominal type：# For nominal type, use a specific integer to represent the frequent value of each column. For numeric type, use a specific integer to represent a range of value.# country
# In[3]:


country_filter_reviews = wine_reviews.groupby('country').filter(lambda x: len(x) >= minsup)
country_reviews = country_filter_reviews.groupby('country').country.count().sort_values()
country_reviews


# In[4]:


country_reviews.plot.bar()

# US = 1 France = 2 Italy = 3 Spain = 4 Portugal = 5 Chile = 6 Argentina = 7 Austria = 8 Australia = 9 Germany = 10 New Zealand = 11 South Africa =12 Others = 0
# In[5]:


country_max = 12


# In[6]:


def judge_country(country):
    if country == 'US':
        return 1
    elif country == 'France':
        return 2
    elif country == 'Italy':
        return 3
    elif country == 'Spain':
        return 4
    elif country == 'Portugal':
        return 5
    elif country == 'Chile':
        return 6
    elif country == 'Argentina':
        return 7
    elif country == 'Austria':
        return 8
    elif country == 'Australia':
        return 9
    elif country == 'Germany':
        return 10
    elif country == 'New Zealand':
        return 11
    elif country == 'South Africa':
        return 12
    else:
        return 0

wine_reviews['country_trans'] = wine_reviews['country'].apply(judge_country)

# designation
# In[7]:


designation_filter_reviews = wine_reviews.groupby('designation').filter(lambda x: len(x) >= minsup)
designation_reviews = designation_filter_reviews.groupby('designation').designation.count().sort_values()
designation_reviews


# In[8]:


designation_reviews.plot.bar()

# Reserve = 1 Estate = 2 Reserva = 3 Others = 0
# In[9]:


designation_max = 3


# In[10]:


def judge_designation(designation):
    if designation == 'Reserve':
        return 1
    elif designation == 'Estate':
        return 2
    elif designation == 'Reserva':
        return 3
    else:
        return 0

wine_reviews['designation_trans'] = wine_reviews['designation'].apply(judge_designation)

# province
# In[11]:


province_filter_reviews = wine_reviews.groupby('province').filter(lambda x: len(x) >= minsup)
province_reviews = province_filter_reviews.groupby('province').province.count().sort_values()
province_reviews


# In[12]:


province_reviews.plot.bar()

# California = 1 Washington = 2 Bordeaux = 3 Tuscany = 4 Oregon = 5 Burgundy = 6 Northern Spain = 7 Piedmont = 8 Mendoza Province = 9 Veneto = 10 New York = 11 Alsace = 12 Northeastern Italy = 13 Loire Valley = 14 Sicily & Sardinia = 15 Champagne = 16 Southwest France = 17 South Australia = 18 Southern Italy = 19 Provence = 20 Douro = 21 Central Italy = 22 Others = 0
# In[13]:


province_max = 22


# In[14]:


def judge_province(province):
    if province == 'California':
        return 1
    elif province == 'Washington':
        return 2
    elif province == 'Bordeaux':
        return 3
    elif province == 'Tuscany':
        return 4
    elif province == 'Oregon':
        return 5
    elif province == 'Burgundy':
        return 6
    elif province == 'Northern Spain':
        return 7
    elif province == 'Piedmont':
        return 8
    elif province == 'Mendoza Province':
        return 9
    elif province == 'Veneto':
        return 10
    elif province == 'New York':
        return 11
    elif province == 'Alsace':
        return 12
    elif province == 'Northeastern Italy':
        return 13
    elif province == 'Loire Valley':
        return 14
    elif province == 'Sicily & Sardinia':
        return 15
    elif province == 'Champagne':
        return 16
    elif province == 'Southwest France':
        return 17
    elif province == 'South Australia':
        return 18
    elif province == 'Southern Italy':
        return 19
    elif province == 'Provence':
        return 20
    elif province == 'Douro':
        return 21
    elif province == 'Central Italy':
        return 22
    else:
        return 0

wine_reviews['province_trans'] = wine_reviews['province'].apply(judge_province)

# region_1
# In[15]:


region_1_filter_reviews = wine_reviews.groupby('region_1').filter(lambda x: len(x) >= minsup)
region_1_reviews = region_1_filter_reviews.groupby('region_1').region_1.count().sort_values()
region_1_reviews


# In[16]:


region_1_reviews.plot.bar()

# Napa Valley = 1 Columbia Valley (WA) = 2 Russian River Valley = 3 California = 4 Paso Robles = 5 Mendoza = 6 Willamette Valley = 7 Alsace = 8 Champagne = 9 Barolo = 10 Finger Lakes = 11 Sonoma Coast = 12 Brunello di Montalcino = 13 Rioja = 14 Sonoma County = 15 Others = 0
# In[17]:


region_1_max = 15


# In[18]:


def judge_region_1(region_1):
    if region_1 == 'Napa Valley':
        return 1
    elif region_1 == 'Columbia Valley (WA)':
        return 2
    elif region_1 == 'Russian River Valley':
        return 3
    elif region_1 == 'California':
        return 4
    elif region_1 == 'Paso Robles':
        return 5
    elif region_1 == 'Mendoza':
        return 6
    elif region_1 == 'Willamette Valley':
        return 7
    elif region_1 == 'Alsace':
        return 8
    elif region_1 == 'Champagne':
        return 9
    elif region_1 == 'Barolo':
        return 10
    elif region_1 == 'Finger Lakes':
        return 11
    elif region_1 == 'Sonoma Coast':
        return 12
    elif region_1 == 'Brunello di Montalcino':
        return 13
    elif region_1 == 'Rioja':
        return 14
    elif region_1 == 'Sonoma County':
        return 15    
    else:
        return 0

wine_reviews['region_1_trans'] = wine_reviews['region_1'].apply(judge_region_1)

# region_2
# In[19]:


region_2_filter_reviews = wine_reviews.groupby('region_2').filter(lambda x: len(x) >= minsup)
region_2_reviews = region_2_filter_reviews.groupby('region_2').region_2.count().sort_values()
region_2_reviews


# In[20]:


region_2_reviews.plot.bar()

# Central Coast = 1 Sonoma = 2 Columbia Valley = 3 Napa = 4 Willamette Valley = 5 California Other = 6 Finger Lakes = 7 Sierra Foothills = 8 Others = 0
# In[21]:


region_2_max = 8


# In[22]:


def judge_region_2(region_2):
    if region_2 == 'Central Coast':
        return 1
    elif region_2 == 'Sonoma':
        return 2
    elif region_2 == 'Columbia Valley':
        return 3
    elif region_2 == 'Napa':
        return 4
    elif region_2 == 'Willamette Valley':
        return 5
    elif region_2 == 'California Other':
        return 6
    elif region_2 == 'Finger Lakes':
        return 7
    elif region_2 == 'Sierra Foothills':
        return 8
    else:
        return 0

wine_reviews['region_2_trans'] = wine_reviews['region_2'].apply(judge_region_2)

# taster_name
# In[23]:


taster_name_filter_reviews = wine_reviews.groupby('taster_name').filter(lambda x: len(x) >= minsup)
taster_name_reviews = taster_name_filter_reviews.groupby('taster_name').taster_name.count().sort_values()
taster_name_reviews


# In[24]:


taster_name_reviews.plot.bar()

# Roger Voss = 1 Michael Schachner = 2 Kerin O’Keefe = 3 Virginie Boone = 4 Paul Gregutt = 5 Matt Kettmann = 6 Joe Czerwinski = 7 Sean P. Sullivan = 8 Anna Lee C. Iijima = 9 Jim Gordon = 10 Anne Krebiehl MW = 11 Lauren Buzzeo = 12 Others = 0
# In[25]:


taster_name_max = 12


# In[26]:


def judge_taster_name(taster_name):
    if taster_name == 'Roger Voss':
        return 1
    elif taster_name == 'Michael Schachner':
        return 2
    elif taster_name == 'Kerin O’Keefe':
        return 3
    elif taster_name == 'Virginie Boone':
        return 4
    elif taster_name == 'Paul Gregutt':
        return 5
    elif taster_name == 'Matt Kettmann':
        return 6
    elif taster_name == 'Joe Czerwinski':
        return 7
    elif taster_name == 'Sean P. Sullivan':
        return 8
    elif taster_name == 'Anna Lee C. Iijima':
        return 9
    elif taster_name == 'Jim Gordon':
        return 10
    elif taster_name == 'Anne Krebiehl MW':
        return 11
    elif taster_name == 'Lauren Buzzeo':
        return 12
    else:
        return 0

wine_reviews['taster_name_trans'] = wine_reviews['taster_name'].apply(judge_taster_name)

# taster_twitter_handle
# In[27]:


taster_twitter_handle_filter_reviews = wine_reviews.groupby('taster_twitter_handle').filter(lambda x: len(x) >= minsup)
taster_twitter_handle_reviews = taster_twitter_handle_filter_reviews.groupby('taster_twitter_handle').taster_twitter_handle.count().sort_values()
taster_twitter_handle_reviews


# In[28]:


taster_twitter_handle_reviews.plot.bar()

# @vossroger = 1 @wineschach = 2 @kerinokeefe = 3 @vboone = 4 @paulgwine = 5 @mattkettmann = 6 @JoeCz = 7 @wawinereport = 8 @gordone_cellars = 9 @AnneInVino = 10 @laurbuzz = 11 Others = 0
# In[29]:


taster_twitter_handle_max = 11


# In[30]:


def judge_taster_twitter_handle(taster_twitter_handle):
    if taster_twitter_handle == '@vossroger':
        return 1
    elif taster_twitter_handle == '@wineschach':
        return 2
    elif taster_twitter_handle == '@kerinokeefe':
        return 3
    elif taster_twitter_handle == '@vboone':
        return 4
    elif taster_twitter_handle == '@paulgwine':
        return 5
    elif taster_twitter_handle == '@mattkettmann':
        return 6
    elif taster_twitter_handle == '@JoeCz':
        return 7
    elif taster_twitter_handle == '@wawinereport':
        return 8
    elif taster_twitter_handle == '@gordone_cellars':
        return 9
    elif taster_twitter_handle == '@AnneInVino':
        return 10
    elif taster_twitter_handle == '@laurbuzz':
        return 11
    else:
        return 0

wine_reviews['taster_twitter_handle_trans'] = wine_reviews['taster_twitter_handle'].apply(judge_taster_twitter_handle)

# variety
# In[31]:


variety_filter_reviews = wine_reviews.groupby('variety').filter(lambda x: len(x) >= minsup)
variety_reviews = variety_filter_reviews.groupby('variety').variety.count().sort_values()
variety_reviews


# In[32]:


variety_reviews.plot.bar()

# Pinot Noir = 1 Chardonnay = 2 Cabernet Sauvignon = 3 Red Blend = 4 Bordeaux-style Red Blend = 5 Riesling = 6 Sauvignon Blanc = 7 Syrah = 8 Rosé = 9 Merlot = 10 Nebbiolo = 11 Zinfandel = 12 Sangiovese = 13 Malbec = 14 Portuguese Red = 15 White Blend = 16 Sparkling Blend = 17 Tempranillo = 18 Rhône-style Red Blend = 19 Pinot Gris = 20 Champagne Blend = 21 Cabernet Franc = 22 Grüner Veltliner = 23 Others = 0
# In[33]:


variety_max = 23


# In[34]:


def judge_variety(variety):
    if variety == 'Pinot Noir':
        return 1
    elif variety == 'Chardonnay':
        return 2
    elif variety == 'Cabernet Sauvignon':
        return 3
    elif variety == 'Red Blend':
        return 4
    elif variety == 'Bordeaux-style Red Blend':
        return 5
    elif variety == 'Riesling':
        return 6
    elif variety == 'Sauvignon Blanc':
        return 7
    elif variety == 'Syrah':
        return 8
    elif variety == 'Rosé':
        return 9
    elif variety == 'Merlot':
        return 10
    elif variety == 'Nebbiolo':
        return 11
    elif variety == 'Zinfandel':
        return 12
    elif variety == 'Sangiovese':
        return 13
    elif variety == 'Malbec':
        return 14
    elif variety == 'Portuguese Red':
        return 15
    elif variety == 'White Blend':
        return 16
    elif variety == 'Sparkling Blend':
        return 17
    elif variety == 'Tempranillo':
        return 18
    elif variety == 'Rhône-style Red Blend':
        return 19
    elif variety == 'Pinot Gris':
        return 20
    elif variety == 'Champagne Blend':
        return 21
    elif variety == 'Cabernet Franc':
        return 22
    elif variety == 'Grüner Veltliner':
        return 23
    else:
        return 0

wine_reviews['variety_trans'] = wine_reviews['variety'].apply(judge_variety)

# description
# In[35]:


wine_reviews.groupby('description').winery.count().sort_values()

# 3 < minsup, description not need to consider# title
# In[36]:


wine_reviews.groupby('title').winery.count().sort_values()

# 11 < minsup, title not need to consider# winery
# In[37]:


wine_reviews.groupby('winery').winery.count().sort_values()

# 220 < minsup, winery not need to consider# Numeric type:# Use quartiles to divide the entire range into four intervals, represented by 1 to 4# points
# In[38]:


points_25 = np.percentile(wine_reviews.points, (25))
points_25


# In[39]:


points_50 = np.percentile(wine_reviews.points, (50))
points_50


# In[40]:


points_75 = np.percentile(wine_reviews.points, (75))
points_75


# In[41]:


points_max = 4


# In[42]:


def judge_points(points):
    if points >= points_75:
        return 1
    elif points >= points_50:
        return 2
    elif points >= points_25:
        return 3
    else:
        return 4

wine_reviews['points_trans'] = wine_reviews['points'].apply(judge_points)

# price
# In[43]:


price_25 = np.percentile(wine_reviews.loc[wine_reviews.price >= 0 ].price, (25))
price_25


# In[44]:


price_50 = np.percentile(wine_reviews.loc[wine_reviews.price >= 0 ].price, (50))
price_50


# In[45]:


price_75 = np.percentile(wine_reviews.loc[wine_reviews.price >= 0 ].price, (75))
price_75


# In[46]:


price_max = 4


# In[47]:


def judge_price(price):
    if price >= price_75:
        return 1
    elif price >= price_50:
        return 2
    elif price >= price_25:
        return 3
    else:
        return 4

wine_reviews['price_trans'] = wine_reviews['price'].apply(judge_price)


# # Transform result

# In[48]:


wine_reviews_trans = wine_reviews.loc[: , ['country_trans','designation_trans','province_trans','region_1_trans','region_2_trans','taster_name_trans','taster_twitter_handle_trans','variety_trans','points_trans','price_trans']]
wine_reviews_trans


# # Find out frequent patterns
# Use the Apriori Algorithm# Obviously, there is a direct geographic relationship between country, province, region_1, and region_2, and taster_twitter_handle is just another form of taster_name, so it does not make sense to analyze the relationship between them. Choose country and taster_name as representatives.# {country,designation}
# In[49]:


aprout = [([0] * designation_max) for i in range(country_max)]
for num1 in range(1,country_max+1):
    for num2 in range(1,designation_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['country_trans'] == num1) & (wine_reviews_trans['designation_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[50]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# frequent patterns is {US,Reserve} {US,Estate}#{US,Reserve}
# In[51]:


supp_US_and_Reserve = 1485/129971
conf_US_to_Reserve = 1485/54504
conf_Reserve_to_US = 1485/2009
lift_US_and_Reserve = (1485/129971)/((54504/129971)*(2009/129971))
allconf_US_and_Reserve = 1485/54504
supp_US_and_Reserve,conf_US_to_Reserve,conf_Reserve_to_US,lift_US_and_Reserve,allconf_US_and_Reserve

# The value of supp_US_and_Reserve means that the frequency of this item set is very low
# The value of conf_US_to_Reserve means that it is basically impossible to speculate Reserve from the presence of US
# The value of conf_Reserve_to_US means that it is possible to speculate US from the presence of Reserve 
# The value of lift_US_and_Reserve means that the interdependence of US and Reserve is positive
# The value of allconf_US_and_Reserve means that the all confidence is low#{US,Estate}
# In[52]:


supp_US_and_Estate = 1210/129971
conf_US_to_Estate = 1210/54504
conf_Estate_to_US = 1210/1322
lift_US_and_Estate = (1210/129971)/((54504/129971)*(1322/129971))
allconf_US_and_Estate = 1210/54504
supp_US_and_Estate,conf_US_to_Estate,conf_Estate_to_US,lift_US_and_Estate,allconf_US_and_Estate

# The value of supp_US_and_Estate means that the frequency of this item set is very low
# The value of conf_US_to_Estate means that it is basically impossible to speculate Estate from the presence of US
# The value of conf_Estate_to_US means that it is possible to speculate US from the presence of Estate
# The value of lift_US_and_Estate means that the interdependence of US and Estate is positive
# The value of allconf_US_and_Estate means that the all confidence is low# {country,taster_name}
# In[53]:


aprout = [([0] * taster_name_max) for i in range(country_max)]
for num1 in range(1,country_max+1):
    for num2 in range(1,taster_name_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['country_trans'] == num1) & (wine_reviews_trans['taster_name_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[54]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# frequent patterns is {US,Virginie Boone} {US,Paul Gregutt} {US,Matt Kettmann} {US,Sean P. Sullivan} {US,Anna Lee C. Iijima} {US,Jim Gordon} {France,Roger Voss} {Italy,Kerin O’Keefe} {Spain,Michael Schachner} {Portugal,Roger Voss} {Chile,Michael Schachner} {Argentina,Michael Schachner} {Australia,Joe Czerwinski} {Germany,Anna Lee C. Iijima} {New Zealand,Joe Czerwinski}# {country,variety}
# In[55]:


aprout = [([0] * variety_max) for i in range(country_max)]
for num1 in range(1,country_max+1):
    for num2 in range(1,variety_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['country_trans'] == num1) & (wine_reviews_trans['variety_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[56]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# frequent patterns is {US,Pinot Noir} {US,Chardonnay} {US,Cabernet Sauvignon} {US,Red Blend} {US,Bordeaux-style Red Blend} {US,Riesling} {US,Sauvignon Blanc} {US,Syrah} {US,Merlot} {US,Zinfandel} {France,Pinot Noir} {France,Chardonnay} {France,Bordeaux-style Red Blend} {France,Rosé} {France,Champagne Blend} {Italy,Red Blend} {Italy,Nebbiolo} {Italy,Sangiovese} {Spain,Tempranillo} {Portugal,Portuguese Red} {Argentina,Malbec} {Austria,Grüner Veltliner} {Germany,Riesling}# {country,points}
# In[57]:


aprout = [([0] * points_max) for i in range(country_max)]
for num1 in range(1,country_max+1):
    for num2 in range(1,points_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['country_trans'] == num1) & (wine_reviews_trans['points_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[58]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# frequent patterns is {US,100-75} {US,75-50} {US,50-25} {US,25-0} {France,100-75} {France,75-50} {France,50-25} {France,25-0} {Italy,100-75} {Italy,75-50} {Italy,50-25} {Italy,25-0} {Spain,75-50} {Spain,50-25} {Spain,25-0} {Portugal,100-75} {Portugal,75-50} {Portugal,50-25} {Chile,50-25} {Chile,25-0} {Argentina,25-0} {Austria,100-75} {Austria,75-50}# {country,price}
# In[59]:


aprout = [([0] * price_max) for i in range(country_max)]
for num1 in range(1,country_max+1):
    for num2 in range(1,price_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['country_trans'] == num1) & (wine_reviews_trans['price_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[60]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# frequent patterns is {US,100-75} {US,75-50} {US,50-25} {US,25-0} {France,100-75} {France,75-50} {France,50-25} {France,25-0} {Italy,100-75} {Italy,75-50} {Italy,50-25} {Italy,25-0} {Spain,75-50} {Spain,50-25} {Spain,25-0} {Portugal,25-0} {Chile,25-0} {Argentina,25-0}# {designation,taster_name}
# In[61]:


aprout = [([0] * taster_name_max) for i in range(designation_max)]
for num1 in range(1,designation_max+1):
    for num2 in range(1,taster_name_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['designation_trans'] == num1) & (wine_reviews_trans['taster_name_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout

# no frequent patterns# {designation,variety}
# In[62]:


aprout = [([0] * variety_max) for i in range(designation_max)]
for num1 in range(1,designation_max+1):
    for num2 in range(1,variety_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['designation_trans'] == num1) & (wine_reviews_trans['variety_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout

# no frequent patterns# {designation,points}
# In[63]:


aprout = [([0] * points_max) for i in range(designation_max)]
for num1 in range(1,designation_max+1):
    for num2 in range(1,points_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['designation_trans'] == num1) & (wine_reviews_trans['points_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout

# no frequent patterns# {designation,price}
# In[64]:


aprout = [([0] * price_max) for i in range(designation_max)]
for num1 in range(1,designation_max+1):
    for num2 in range(1,price_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['designation_trans'] == num1) & (wine_reviews_trans['price_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout

# no frequent patterns# {taster_name,variety}
# In[65]:


aprout = [([0] * variety_max) for i in range(taster_name_max)]
for num1 in range(1,taster_name_max+1):
    for num2 in range(1,variety_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['taster_name_trans'] == num1) & (wine_reviews_trans['variety_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[66]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# {taster_name,points}
# In[67]:


aprout = [([0] * points_max) for i in range(taster_name_max)]
for num1 in range(1,taster_name_max+1):
    for num2 in range(1,points_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['taster_name_trans'] == num1) & (wine_reviews_trans['points_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[68]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# {taster_name,price}
# In[69]:


aprout = [([0] * price_max) for i in range(taster_name_max)]
for num1 in range(1,taster_name_max+1):
    for num2 in range(1,price_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['taster_name_trans'] == num1) & (wine_reviews_trans['price_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[70]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# {variety,points}
# In[71]:


aprout = [([0] * points_max) for i in range(variety_max)]
for num1 in range(1,variety_max+1):
    for num2 in range(1,points_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['variety_trans'] == num1) & (wine_reviews_trans['points_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[72]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# {variety,price}
# In[73]:


aprout = [([0] * price_max) for i in range(variety_max)]
for num1 in range(1,variety_max+1):
    for num2 in range(1,price_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['variety_trans'] == num1) & (wine_reviews_trans['price_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[74]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()

# {points,price}
# In[75]:


aprout = [([0] * price_max) for i in range(points_max)]
for num1 in range(1,points_max+1):
    for num2 in range(1,price_max+1):
        apr = wine_reviews_trans[(wine_reviews_trans['points_trans'] == num1) & (wine_reviews_trans['price_trans'] == num2)] 
        if len(apr.index) >= minsup:
            aprout[num1 - 1][num2 - 1] = len(apr.index)
aprout


# In[76]:


aprout_df = pd.DataFrame(aprout)
aprout_df.plot.line()


# # Result analysis
# US has the largest number and the most comprehensive variety in all aspects.
# US is affected by a lot of taster, other countries mostly affected by a specific taster.
# In addition to US, other countries each has its own preference of the type of grapes used to make the wine.
# Different taster have different scoring strategies.
# points and price are positively related.