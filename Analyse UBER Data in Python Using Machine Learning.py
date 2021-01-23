# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 18:35:33 2020

@author: Abdullah Younis
"""


import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.style.use('ggplot')
import calendar
data='file:///C:/Users/joker/AppData/Local/Temp/datasets_1026_1855_My%20Uber%20Drives%20-%202016.csv'
data=pd.read_csv('file:///C:/Users/joker/AppData/Local/Temp/datasets_1026_1855_My%20Uber%20Drives%20-%202016.csv')
data.head()
data.tail()
data=data[:-1]
data.isnull().sum()    
sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")
plt.show()
data=data.dropna()
sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")
plt.show()
data['START_DATE*'] = pd.to_datetime(data['START_DATE*'], format="%m/%d/%Y %H:%M")
data['END_DATE*'] = pd.to_datetime(data['END_DATE*'], format="%m/%d/%Y %H:%M")
hour=[]
day=[]
dayofweek=[]
month=[]
weekday=[]
for x in data['START_DATE*']:
        hour.append(x.hour)
        day.append(x.day)
        dayofweek.append(x.dayofweek)
        month.append(x.month)
        weekday.append(calendar.day_name[dayofweek[-1]])
data['HOUR']=hour
data['DAY']=day
data['DAY_OF_WEEK']=dayofweek
data['MONTH']=month
data['WEEKDAY']=weekday
time=[]
data['TRAVELLING_TIME']=data['END_DATE*']-data['START_DATE*']
for i in data['TRAVELLING_TIME']:
        time.append(i.seconds/60)
data['TRAVELLING_TIME']=time
data.head()
data['TRAVELLING_TIME']=data['TRAVELLING_TIME']/60
data['SPEED']=data['MILES*']/data['TRAVELLING_TIME']
data.head()
sns.countplot(x='CATEGORY*',data=data)
data['MILES*'].plot.hist()
data['PURPOSE*'].value_counts().plot(kind='bar',figsize=(10,5),color='blue')
plt.show()
data['HOUR'].value_counts().plot(kind='bar',figsize=(10,5),color='green')
plt.show()
data['WEEKDAY'].value_counts().plot(kind='bar',color='green')
plt.show()
data['DAY'].value_counts().plot(kind='bar',figsize=(15,5),color='green')
plt.show()
data['MONTH'].value_counts().plot(kind='bar',figsize=(10,5),color='green')
plt.show()
data['START*'].value_counts().plot(kind='bar',figsize=(25,5),color='red')
plt.show()
data.groupby('PURPOSE*').mean().plot(kind='bar',figsize=(15,5))
plt.show()
