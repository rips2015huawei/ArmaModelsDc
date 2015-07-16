# coding: utf-8

import numpy as np
import statsmodels.api as sm
from scipy import stats
import pandas as pd
from statsmodels.graphics.api import qqplot


df = data
df.index = df['Start date']

dfOneSlice = df.loc[(df['Start Station'] == 'Ohio Dr & West Basin Dr SW / MLK & FDR Memorials') | (df['Start Station'] == 'US Dept of State / Virginia Ave & 21st St NW') |(df['Start Station'] == '21st St & Constitution Ave NW') |(df['Start Station'] == 'Lincoln Memorial') ]
dfOneSlice.head()


start_date = datetime.datetime(2012,1,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,1,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & (dfOneSlice['End date'] < end_date)]
rideCounts = []
rideTimes = []
date = start_date;


t= datetime.timedelta(minutes = 15)
while date != end_date:
    date = date + t;
    rideTimes.append(start_date)
    rideCounts.append(len(dfOneSlice_week1.loc[(dfOneSlice_week1['Start date'] >=start_date)& (dfOneSlice_week1['Start date'] < date)].index))
    start_date = date;
     
series = pd.DataFrame({'times': rideTimes, 'count': rideCounts})
series.index = series['times']

series = series.drop('times',1)

arma_mod = sm.tsa.ARMA(series, (20,0))
arma_res = arma_mod.fit()

prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-01-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-01-01 00:00:00', '2012-01-08 00:00:00', ax=ax, plot_insample=True)


