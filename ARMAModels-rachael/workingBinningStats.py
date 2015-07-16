import numpy as np
import statsmodels.api as sm
from scipy import stats
import pandas as pd
from statsmodels.graphics.api import qqplot
import scipy



# Assume: ran handleBikeShare and have dataframe 'data' of all rides
df = data
df.index = df['Start date']

# Slice the df to the stations we care about
dfOneSlice2 = df2.loc[(df['Start Station'] ==521)]
dfOneSlice2.head()


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
#prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2014-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-01 00:00:00', '2014-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()



predict = arma_res.predict('2012-06-01 00:00:00', '2012-06-07 23:59:59')
len(predict)
cov = np.cov(predict, series['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))

# stats.correlation(predict, series['count'])


# THE FOLLOWING CODE WILL MODIFY ALL ELEMENTS IN THE SERIES, setting the negatives to 0.
p[p<0] = 0


# Note: p is 4*predict. We scaled p by 4 bc the data set is 4 stations superimposed on each other.
# However, that just resulted in all the results being scaled by a factor of 4 (of course)


# Example of scipy's linregress():
#   slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(p, series['count'])

# View residues 
# arma_res.resid
res = arma_res.resid

# Example of numpy's lstsqs
#   model, resid = np.linalg.lstsq(p,series['count'])[:2] 

# R^2 values on predicted results vs actual
ssres = np.sum((predict - series2['count'])**2)
sstot = np.sum((series2['count'] - np.mean(series2['count']))**2)
r2 = 1-(ssres/sstot)


start_date = datetime.datetime(2012,6,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,6,8,0,0,0,0);
dfOneSlice_week1 = data.loc[(data['Start date'] >= start_date) & ((data['Start date'] < end_date))]
## NOTE: Could add condition in dcOneSlice_week1 that
#       (['Start date'] >= start_date) & (['End date'] < end_date | ['Start date'] < end_date))
# Containers to extract series:
rideCounts = []; rideTimes = [];
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

# Trial to make sure ARMA runs on the series.
arma_mod = sm.tsa.ARMA(series, (20,0))
arma_res = arma_mod.fit()
#prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-07 00:00:00':].plot(ax=ax)
fig, ax = plt.subplots(figsize=(12, 8))
ax = series2.ix['2014-06-06 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2014-06-08 00:00:00', '2014-06-08 01:00:00', ax=ax, dynamic = True)
plt.show()
plt.close()



predict = arma_res.predict('2012-06-01 00:00:00', '2012-06-07 23:59:59')
len(predict)
cov = np.cov(predict, series['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))



