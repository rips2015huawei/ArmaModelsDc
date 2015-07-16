# coding: utf-8
get_ipython().magic(u'cd Desktop/RIPS/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ARMAModels-local/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'run handleBikeshare.py')
get_ipython().magic(u'run handleBikeshare.py')
get_ipython().magic(u'ls ')
get_ipython().magic(u'run workingBinningStats.py')
get_ipython().magic(u'run workingBinningStats.py')
get_ipython().magic(u'run workingBinningStats.py')
get_ipython().magic(u'run workingBinningStats.py')
get_ipython().magic(u'run workingBinningStats.py')
data
df = data
df.index = df['Start date']
start_date = datetime.datetime(2012,1,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,1,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['End date'] < end_date)| dfOneSlice['Start date'] < end_date))]
## NOTE: Could add condition in dcOneSlice_week1 that
#       (['Start date'] >= start_date) & (['End date'] < end_date | ['Start date'] < end_date))
start_date = datetime.datetime(2012,1,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,1,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['End date'] < end_date)| (dfOneSlice['Start date'] < end_date))]
dfOneSlice = df.loc[(df['Start Station'] == 'Ohio Dr & West Basin Dr SW / MLK & FDR Memorials') | (df['Start Station'] == 'US Dept of State / Virginia Ave & 21st St NW') |(df['Start Station'] == '21st St & Constitution Ave NW') |(df['Start Station'] == 'Lincoln Memorial') ]
dfOneSlice.head()
start_date = datetime.datetime(2012,1,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,1,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['End date'] < end_date)| (dfOneSlice['Start date'] < end_date))]
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
prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-01-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-01-01 00:00:00', '2012-01-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()
predict = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
np.cov(predict, series['count'])
predict = arma_res.predict('2012-01-01 00:00:00', '2012-01-07 23:59:59')
np.cov(predict, series['count'])
cov=np.cov(predict, series['count'])
cov(1)
cov(1,1)
cov[1]
cov[1][1]
r=cov[1][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres = np.sum((predict - series['count'])**2)
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
r2 = 1-(ssres/sstot)
r2
avg = np.mean(series['count'])
avg
np.mean(predict)
sstot = np.sum((series['count'] - avg))**2)
sstot = np.sum((series['count'] - avg)**2)
r2 = 1-(ssres/sstot)
r2
ssres = np.sum((predict - series['count'])**2)
predict
predict[predict <0]=0
ssres = np.sum((predict - series['count'])**2)
ssres = np.sum((predict - series['count'])**2)
r2 = 1-(ssres/sstot)
r2
predict['count']= predict['count'].round
predict_ = predict.round()
predict_
predict_ = predict.astype(int)
predict_
predict
predict_=np.ceil(predict)
predict_
cov = np.cov(predict_, series['count'])
r=cov[1][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres = np.sum((predict_ - series['count'])**2)
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
r2 = 1-(ssres/sstot)
r2
predict_
predict_[0]
predict_[1]
predict_[0:]
predict_[0][:]
predict_[0]
ssres = np.sum((predict_ - series['count'])**2)
ssres
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
sstot
predict_
series['count']
predict_=np.floor(predict)
cov = np.cov(predict_, series['count'])
r=cov[1][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres = np.sum((predict_ - series['count'])**2)
r2 = 1-(ssres/sstot)
r2
g =  open('closeSubwayStations.txt', "w")
g.write("%s\n" % edg)
g.close()
g =  open('rideCounts.txt', "w")
g.write("%2\n" %predict_)
predict_.to_csv('predicted.csv')
series.to_csv('data.csv')
sstot = np.sum(((series['count'] - np.mean(series['count']))/4)**2)
r2 = 1-(ssres/sstot)
r2
ssres = np.sum((predict_ - series['count']/4)**2)
r2 = 1-(ssres/sstot)
r2
ssres = np.sum((predict_ - (series['count']/4))**2)
r2 = 1-(ssres/sstot)
r2
cov = np.cov(predict_, series['count'])
np.std(predict_)
sig1=np.std(predict_)
sig2=np.std(series['count'])
cov
cov[0][1]/(sig1*sig2)
cov = np.cov(predict, series['count'])
sig1=np.std(predict)
sig2=np.std(series['count'])
cov[0][1]/(sig1*sig2)
ssreg = np.sum((predict_ - np.mean(series['count']))**2)
ssreg/sstot
start_date = datetime.datetime(2012,1,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,1,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['Start date'] < end_date))]
## NOTE: Could add condition in dcOneSlice_week1 that
#       (['Start date'] >= start_date) & (['End date'] < end_date | ['Start date'] < end_date))
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
prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-08 00:00:00')
prediction = arma_res.predict('2012-01-01 00:00:00', '2012-01-07 23:59:59')
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-01-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-01-01 00:00:00', '2012-01-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()
start_date = datetime.datetime(2012,6,1,0,0,0,0); date=start_date; t = datetime.timedelta(minutes = 15)
end_date = datetime.datetime(2012,6,8,0,0,0,0);
dfOneSlice_week1 = dfOneSlice.loc[(dfOneSlice['Start date'] >= start_date) & ((dfOneSlice['Start date'] < end_date))]
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
pred = arma_res.predict('2012-06-01 00:00:00', '2012-06-08')
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-01 00:00:00', '2012-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
pred = arma_res.predict('2012-06-01 00:00:00', '2012-06-08 00:00:00')
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-01 00:00:00', '2012-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
plt.close()
pred = predict_
predict_[predict_<0]=0
cov = np.cov(predict_, series['count'])
cov
r=cov[1][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres = np.sum((predict_ - series['count'])**2)
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
r2 = 1-(ssres/sstot)
r2
cov
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres
predict_
pred = predict
pred
pred[pred<0]=0
cov = np.cov(pred, series['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
ssres = np.sum((pred - series['count'])**2)
r2 = 1-(ssres/sstot)
r2
ssres
pred
predict = arma_res.predict('2012-06-01 00:00:00', '2012-06-07 23:59:59')
len(predict)
cov = np.cov(predict, series['count'])
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
cov
pred = predict
pred[pred<0]=0
r=cov[0][1]/(np.sqrt(cov[0][0])*np.sqrt(cov[1][1]))
r
cov2 = np.cov(pred,series['count'])
r=cov2[0][1]/(np.sqrt(cov2[0][0])*np.sqrt(cov2[1][1]))
r
ssres = np.sum((pred - series['count'])**2)
r2 = 1-(ssres/sstot)
r2
sstot
sstot = np.sum((series['count'] - np.mean(series['count']))**2)
r2 = 1-(ssres/sstot)
ssres2 = np.sum((predict - series['count'])**2)
r2 = 1-(ssres2/sstot)
r2
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-01 00:00:00', '2012-06-08 00:00:00', ax=ax, plot_insample=True)
plt.show()
pround = pred
pround.roud
pround.round
pround = pround.roud
pround = pround.round
pround
pround = pred.round
pround
pround = pred.round()
pround
ssres = np.sum((pround - series['count'])**2)
sstot
1-(ssres/sstot)
plot(pround, series['count'])
plt.plot(pround, series['count'])
plt.show()
pround = pround -1
ssres = np.sum((pround - series['count'])**2)
1-(ssres/sstot)
pround
pround[pround<0]=0
ssres = np.sum((pround - series['count'])**2)
1-(ssres/sstot)
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
arma_res.param
arma_mod.param
arma_mod.params
arma_res.params
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample=True)
plt.show()
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax, , dynamic=True)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax,  dynamic=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 00:00:00', '2012-06-09 00:00:00', ax=ax,  dynamic=True)
plt.show()
fig = arma_res.plot_predict('2012-06-08 00:00:00', '2012-06-09 00:00:00', ax=ax,  dynamic=True)
fig, ax = plt.subplots(figsize=(12, 8))
fig = arma_res.plot_predict('2012-06-08 00:00:00', '2012-06-09 00:00:00', ax=ax,  dynamic=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
fig = arma_res.plot_predict('2012-06-08 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample = True, dynamic=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
fig = arma_res.plot_predict('2012-06-08 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample = True, dynamic=True)
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-08 00:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample = True, dynamic=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-01 00:00:00':].plot(ax=ax)
ax = series.ix['2012-06-05 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 17:00:00', '2012-06-09 00:00:00', ax=ax, plot_insample = True, dynamic=True)
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax = series.ix['2012-06-05 00:00:00':].plot(ax=ax)
fig = arma_res.plot_predict('2012-06-07 17:00:00', '2012-06-09 00:00:00', ax=ax, dynamic=True)
plt.show()
