# coding: utf-8
get_ipython().magic(u'run handleNycBikeshare.py')
df2 = data
df2.index = df2['Start date']
dfOneSlice2 = df2.loc[(df['Start Station'] ==521]
dfOneSlice2.head()

;
)
dfOneSlice2 = df2.loc[(df['Start Station'] ==521)]
dfOneSlice2.head()
dfOneSlice2 = df2.loc[(df2['Start Station'] ==521)]
dfOneSlice2.head()
# Containers to extract series:
rideCounts = []; rideTimes = [];
date = start_date;
t= datetime.timedelta(minutes = 15)
while date != end_date:
            date = date + t;
            rideTimes.append(start_date)
            rideCounts.append(len(dfOneSlice_week12.loc[(dfOneSlice_week1['Start date'] >=start_date)& (dfOneSlice_week1['Start date'] < date)].index))
            start_date = date;
    
rideCounts = []; rideTimes = [];
date = start_date;
t= datetime.timedelta(minutes = 15)
while date != end_date:
            date = date + t;
            rideTimes.append(start_date)
            rideCounts.append(len(dfOneSlice_week12.loc[(dfOneSlice_week12['Start date'] >=start_date)& (dfOneSlice_week12['Start date'] < date)].index))
            start_date = date;
             
series2 = pd.DataFrame({'times': rideTimes, 'count': rideCounts})
series2.index = series2['times']
series2= series2.drop('times',1)
rideCounts = []; rideTimes = [];
date = start_date;
t= datetime.timedelta(minutes = 15)
while date != end_date:
            date = date + t;
            rideTimes.append(start_date)
            rideCounts.append(len(dfOneSlice_week12.loc[(dfOneSlice_week12['Start date'] >=start_date)& (dfOneSlice_week12['Start date'] < date)].index))
            start_date = date;
             
series2 = pd.DataFrame({'times': rideTimes, 'count': rideCounts})
series2.index = series2['times']
series2= series2.drop('times',1)
arma_mod = sm.tsa.ARMA(series2, (20,0))
rideCounts
start_date = datetime.datetime(2012,6,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,6,8,0,0,0,0);
dfOneSlice_week12 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['Start date'] < end_date))]
## NOTE: Could add condition in dcOneSlice_week1 that
#       (['Start date'] >= start_date) & (['End date'] < end_date | ['Start date'] < end_date))
start_date = datetime.datetime(2012,6,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,6,8,0,0,0,0);
dfOneSlice_week12 = dfOneSlice2.loc[(dfOneSlice2['Start date'] >= start_date) & ((dfOneSlice2['Start date'] < end_date))]
## NOTE: Could add condition in dcOneSlice_week1 that
#       (['Start date'] >= start_date) & (['End date'] < end_date | ['Start date'] < end_date))
# Containers to extract series:
rideCounts = []; rideTimes = [];
date = start_date;
t= datetime.timedelta(minutes = 15)
while date != end_date:
            date = date + t;
            rideTimes.append(start_date)
            rideCounts.append(len(dfOneSlice_week12.loc[(dfOneSlice_week12['Start date'] >=start_date)& (dfOneSlice_week12['Start date'] < date)].index))
            start_date = date;
             
series2 = pd.DataFrame({'times': rideTimes, 'count': rideCounts})
series2.index = series2['times']
series2= series2.drop('times',1)
# Trial to make sure ARMA runs on the series.
arma_mod = sm.tsa.ARMA(series2, (20,0))
arma_res = arma_mod.fit()
series2
rideCoutns
rideCounts
start_date = datetime.datetime(2012,6,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,6,8,0,0,0,0);
dfOneSlice_week12 = dfOneSlice2.loc[(dfOneSlice2['Start date'] >= start_date) & ((dfOneSlice2['Start date'] < end_date))]
## NOTE: Could add condition in dcOneSlice_week1 that
#       (['Start date'] >= start_date) & (['End date'] < end_date | ['Start date'] < end_date))
dfOneSlice_week12
start_date = datetime.datetime(2014,6,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2014,6,8,0,0,0,0);
dfOneSlice_week12 = dfOneSlice2.loc[(dfOneSlice2['Start date'] >= start_date) & ((dfOneSlice2['Start date'] < end_date))]
## NOTE: Could add condition in dcOneSlice_week1 that
#       (['Start date'] >= start_date) & (['End date'] < end_date | ['Start date'] < end_date))
# Containers to extract series:
rideCounts = []; rideTimes = [];
date = start_date;
t= datetime.timedelta(minutes = 15)
while date != end_date:
            date = date + t;
            rideTimes.append(start_date)
            rideCounts.append(len(dfOneSlice_week12.loc[(dfOneSlice_week12['Start date'] >=start_date)& (dfOneSlice_week12['Start date'] < date)].index))
            start_date = date;
    
series2 = pd.DataFrame({'times': rideTimes, 'count': rideCounts})
series2.index = series2['times']
series2= series2.drop('times',1)
# Trial to make sure ARMA runs on the series.
arma_mod = sm.tsa.ARMA(series2, (20,0))
arma_res = arma_mod.fit()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-01 00:00:00', '2014-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
predict = arma_res.predict('2012-06-01 00:00:00', '2012-06-07 23:59:59')
len(predict)
cov = np.cov(predict, series['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
cov = np.cov(predict, series2['count'])
predict = arma_res.predict('2014-06-01 00:00:00', '2014-06-07 23:59:59')
cov = np.cov(predict, series2['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres = np.sum((predict - series2['count'])**2)
sstot = np.sum((series2['count'] - np.mean(series2['count']))**2)
r2 = 1-(ssres/sstot)
r2
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 20:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()fig = arma_res.plot_predict('2014-06-07 20:00:00', '2014-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 20:00:00', '2014-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 00:00:00', '2014-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 00:00:00', '2014-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 00:00:00', '2014-06-09 00:00:00', ax=ax, dynamic = True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-08 00:00:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-07 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-08 00:00:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-07 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 23:59:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-06 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 00:00:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-06 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 23:59:50', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
plt.close()fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-06 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 23:00:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-06 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-07 23:00:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-06 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-08 00:00:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
