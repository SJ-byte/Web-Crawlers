import os
import datetime as datetime
import glob
import pandas as pd
import csv
import numpy as np

#print os.getcwd()
os.chdir('/Users/sunjiaxuan/Documents/Py/YahooAnalysts')
AllFiles = glob.glob("/Users/sunjiaxuan/Documents/Py/YahooAnalysts/*.csv")


#####Get All the dates we have for now
AllDates = []
###Here we readin all the files that we have downloaded in the history

PriceFilesNames = []
AllPriceResult = []

AnalystFilesNames = []
AllAnalystsResult =[]

for files in AllFiles:
    if 'Price' in files:
        PriceFilesNames.append(files)
        temp = pd.read_csv(files,header = None)
        temp.columns = ['index','Price']
        AllPriceResult.append(temp)
        AllDates.append(files[-14:-4])
    elif 'AnalystsRecScore' in files:
        AnalystFilesNames.append(files)
        temp = pd.read_csv(files,header = None)
        temp.columns = ['index','BuyThisWeek','BuyPreWeek']   
        #Delete all , and [] in temp.ix[:,0]
        for i in list(range(0,len(temp.ix[:,0]))):
            temp.ix[i,0] = ''.join(x for x in temp.ix[i,0] if x.isalpha())
        temp = temp.ix[:,0:2]
        AllAnalystsResult.append(temp)
        
############Combine the views we have now to a dataframe
AllViews = pd.DataFrame()
for i in list(range(0,len(AllAnalystsResult))):
    if i == 0:
        AllViews = AllAnalystsResult[i]
    else:
        AllViews = pd.merge(AllViews,AllAnalystsResult[i] ,on = 'index', how='outer')

#Rename Analysts' view columns
NewName = ['index']
for date in AllDates:
    NewName.append(date)
AllViews.columns = NewName

############Combine the prices we have now to a dataframe for later look up purpose
AllPrices = pd.DataFrame()
for i in list(range(0,len(AllPriceResult))):
    if i == 0:
        AllPrices = AllPriceResult[i]
    else:
        AllPrices = pd.merge(AllPrices,AllPriceResult[i] ,on = 'index', how='outer')

#Rename Prices columns
NewName = ['index']
for date in AllDates:
    NewName.append(date)
AllPrices.columns = NewName

#Store Today's Stock Selection
for i in list(range(1,AllViews.shape[1])):
    for j in list(range(0,len(AllViews.ix[:,-i].values))):
        try: 
            AllViews.ix[j,-i] = float(AllViews.ix[j,-i]) 
        except: 
            AllViews.ix[j,-i] = np.nan

ChangeRating = pd.DataFrame(AllViews.ix[:,-1].values - AllViews.ix[:,1].values,index = AllViews['index'].values)
ChangeRating = ChangeRating.sort_values([0],ascending=True)
#ChangeRating = ChangeRating.dropna()
AllViews = pd.DataFrame(AllViews.ix[:,1:].values,index = AllViews['index'].values)
ChangeRating.columns = ['change']

#Re = ChangeRating
Re = AllViews.join(ChangeRating)
ToBuy = Re.ix[Re.ix[:,-1]<0,:]
ToSell = Re.ix[Re.ix[:,-1]>0,:]

nameBuy = "/Users/sunjiaxuan/Documents/Py/YahooAnalysts/" + "ToBuy" + str(datetime.datetime.now())[0:10] + ".csv"
nameSell = "/Users/sunjiaxuan/Documents/Py/YahooAnalysts/" + "ToSell" + str(datetime.datetime.now())[0:10] + ".csv"

ToBuy.to_csv(nameBuy)
ToSell.to_csv(nameSell)
