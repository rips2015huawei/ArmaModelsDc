# coding: utf-8


# get_ipython().magic(u'run handleBikeshare.py')
# get_ipython().magic(u'run workingBinningStats.py')

# Assume from handleBikeShare: data ~ df of all rides


df = data
df.index = df['Start date']

# Cluster stations: 0.75km within range of Lincoln Memorial.
dfOneSlice = df.loc[(df['Start Station'] == 'Ohio Dr & West Basin Dr SW / MLK & FDR Memorials') | (df['Start Station'] == 'US Dept of State / Virginia Ave & 21st St NW') |(df['Start Station'] == '21st St & Constitution Ave NW') |(df['Start Station'] == 'Lincoln Memorial') ]
dfOneSlice.head()

# Select time of interest, first week of 2012.
start_date = datetime.datetime(2012,1,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,1,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['End date'] < end_date)| (dfOneSlice['Start date'] < end_date))]

# Bin data on rides started for each 15-minute interval.
rideCounts = []; rideTimes = [];
date = start_date;
t= datetime.timedelta(minutes = 15)
while date != end_date:
            date = date + t;
            rideTimes.append(start_date)
            rideCounts.append(len(dfOneSlice_week1.loc[(dfOneSlice_week1['Start date'] >=start_date)& (dfOneSlice_week1['Start date'] < date)].index))
            start_date = date;
    
# Drop data into series.
series = pd.DataFrame({'times': rideTimes, 'count': rideCounts})
series.index = series['times']
series = series.drop('times',1)

# Trial to make sure ARMA runs on the series.
arma_mod = sm.tsa.ARMA(series, (20,0))
arma_res = arma_mod.fit()

# Prediction over first week. (We do this to check to see how results are on the training data. It should at the very least perform well then.)
prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-01-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-01-01 00:00:00', '2012-01-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()

# Now do some analysis on the in-sample data. Note: had to put 23:59:59 else got too many results from predict.
predict = arma_res.predict('2012-01-01 00:00:00', '2012-01-07 23:59:59')
np.cov(predict, series['count'])

cov=np.cov(predict, series['count'])

r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r

ssres = np.sum((predict - series['count'])**2)
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
r2 = 1-(ssres/sstot)

predict[predict <0]=0

ssres = np.sum((predict - series['count'])**2)
r2 = 1-(ssres/sstot) # Note didn't recalculate sstot since it doesn't dependt on predict.
r2


# Try rounding results.
predict_=np.ceil(predict)
predict_
cov = np.cov(predict_, series['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres = np.sum((predict_ - series['count'])**2)
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
r2 = 1-(ssres/sstot)


# Tried dividing the data by 4 since we clustered 4 stations together, but it didn't really help (nor is it necessarily something one can just do..)
ssres = np.sum((predict_ - series['count']/4)**2)
r2 = 1-(ssres/sstot)
r2

# Checking covariances again..comparing..
cov = np.cov(predict_, series['count'])
sig1=np.std(predict_)
sig2=np.std(series['count'])
cov
cov[0][1]/(sig1*sig2)
cov = np.cov(predict, series['count'])
sig1=np.std(predict)
sig2=np.std(series['count'])
cov[0][1]/(sig1*sig2)

# Checked out ssreg
ssreg = np.sum((predict_ - np.mean(series['count']))**2)
ssreg/sstot

###################################################################
##############
##### RETRIAL: Filter for data with START DATE between our times.
#
start_date = datetime.datetime(2012,1,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,1,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['Start date'] < end_date))]

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


arma_mod = sm.tsa.ARMA(series, (20,0))
arma_res = arma_mod.fit()
# ##>>This results in error>># prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-07 23:59:59')

fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-01-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-01-01 00:00:00', '2012-01-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()



###################################################################
##############
##### RETRIAL: Filter for data in the first 7 days of JUNE 2012.
#
start_date = datetime.datetime(2012,6,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,6,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['Start date'] < end_date))]

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

# Generate ARMA models:
arma_mod = sm.tsa.ARMA(series, (20,0))
arma_res = arma_mod.fit()

# Predict and plot results.
pred = arma_res.predict('2012-06-01 00:00:00', '2012-06-08 00:00:00')
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-01 00:00:00', '2012-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()

# Set negative predicted values to zero.
pred[pred<0]=0
cov = np.cov(pred, series['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
ssres = np.sum((pred - series['count'])**2)
r2 = 1-(ssres/sstot)
r2


fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-01 00:00:00', '2012-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()


##############################
# Try rounding -- rounds up
pround = pred.round()
pround
ssres = np.sum((pround - series['count'])**2)
sstot
1-(ssres/sstot)
plot(pround, series['count'])
plt.plot(pround, series['count'])
plt.show()

######################
# Try shifting the results back by 1
pround = pround -1
ssres = np.sum((pround - series['count'])**2)
1-(ssres/sstot)
pround
pround[pround<0]=0
ssres = np.sum((pround - series['count'])**2)
1-(ssres/sstot)

# Various plot-prediction code
predict = arma_res.predict('2012-06-01 00:00:00', '2012-06-07 23:59:59')
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-01 00:00:00', '2012-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()plt.close()

# Check model parameters
arma_res.params

###########################
# More plot predictions. 
#     NOTE, LESSON: PLOT_PREDICT PARAMETERS:
#           dynamic ~ automatically set to False, uses in-sample data
#                     set to true, uses own prediction on the fly
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()


fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax,  dynamic=True)
plt.show()



fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-08 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample = True, dynamic=True)
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-05 00:00:00':].plot(ax=ax) # start later to zoom in
fig = arma_res.plot_predict('2012-06-07 17:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample = True, dynamic=True)
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-05 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 17:00:00', '2012-06-09 00:00:00', ax=ax, dynamic=True)
plt.show()
