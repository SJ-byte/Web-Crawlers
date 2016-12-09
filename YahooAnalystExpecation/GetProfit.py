import os
import datetime as datetime
import glob
import pandas as pd
import csv
import numpy as np
import operator

#print os.getcwd()
os.chdir('/Users/sunjiaxuan/Documents/Py/YahooAnalysts')
AllFiles = glob.glob("/Users/sunjiaxuan/Documents/Py/YahooAnalysts/*.csv")


#####Get All the dates we have for now
AllDates = []
###Here we readin all the files that we have downloaded in the history

PriceFilesNames = []
AllPriceResult = []
PriceDate = []

BuyFileNames = []
BuyFileResult =[]
BuyDate = []

for files in AllFiles:
    if 'TodayPrice' in files:
        PriceFilesNames.append(files)
        temp = pd.read_csv(files,header = None)
        temp.columns = ['index','Price']
        AllPriceResult.append(temp)
        PriceDate.append(files[-14:-4])
    elif 'ToBuy' in files:
        BuyFileNames.append(files)
        temp = pd.read_csv(files,header = None)
        resulttemp = []
        for i in list(range(1,len(temp.ix[1:,0]))):
            resulttemp.append(''.join(x for x in temp.ix[i,0] if x.isalpha()))
        BuyFileResult.append(resulttemp)
        BuyDate.append(files[-14:-4])
        
BuyStocks = BuyFileResult
BuyPrice = []
OneWeekPrice = []
allBuyStockPos = []

for i in list(range(0,len(BuyStocks))):
    ToBuy = BuyStocks[i]
    Date = BuyDate[i]
    PricePos = PriceDate.index(Date)
    tempPrice = []
    for stock in ToBuy:
        tempPrice.append(float(AllPriceResult[PricePos].ix[:,1][AllPriceResult[PricePos].ix[:,0] == stock].tolist()[0]))
    BuyPrice.append(tempPrice)
    NextDate = "{:%Y-%m-%d}".format(datetime.datetime.strptime(Date, '%Y-%m-%d') + datetime.timedelta(days=7))
    flag = 1
    try:
        PricePos = PriceDate.index(NextDate)
    except:
        print("No Data Downloaded")
        flag = 0
    if flag == 0:
        continue
    tempPrice = []
    allBuyStockPos.append(i)
    for stock in ToBuy:
        tempPrice.append(float(AllPriceResult[PricePos].ix[:,1][AllPriceResult[PricePos].ix[:,0] == stock].tolist()[0]))
    OneWeekPrice.append(tempPrice)

NewBuy = map(BuyStocks.__getitem__, allBuyStockPos)
NewBuyPrice = map(BuyPrice.__getitem__, allBuyStockPos)
NewDate = map(BuyDate.__getitem__,allBuyStockPos)
result = []
resultmean = []

for i in list(range(0,len(NewBuy))):
    result.append(list((np.array(OneWeekPrice[i]) - np.array(NewBuyPrice[i])) /np.array(NewBuyPrice[i])))
    resultmean.append(np.nanmean(result[i]))

ProfitFromLong = pd.Series(resultmean,index = NewDate)
nameStore = "/Users/sunjiaxuan/Documents/Py/YahooAnalysts/" + "ProfitFromLong.csv"

ProfitFromLong.to_csv(nameStore)

#######################Get the profit from short euiqties
PriceFilesNames = []
AllPriceResult = []
PriceDate = []

FileNames = []
FileResult =[]
Date = []

for files in AllFiles:
    if 'TodayPrice' in files:
        PriceFilesNames.append(files)
        temp = pd.read_csv(files,header = None)
        temp.columns = ['index','Price']
        AllPriceResult.append(temp)
        PriceDate.append(files[-14:-4])
    elif 'ToSell' in files:
        FileNames.append(files)
        temp = pd.read_csv(files,header = None)
        resulttemp = []
        for i in list(range(1,len(temp.ix[1:,0]))):
            resulttemp.append(''.join(x for x in temp.ix[i,0] if x.isalpha()))
        FileResult.append(resulttemp)
        Date.append(files[-14:-4])
        
Stocks = FileResult
Price = []
OneWeekPrice = []
allStockPos = []
SellDate = Date

for i in list(range(0,len(Stocks))):
    ToSell = Stocks[i]
    Date = SellDate[i]
    PricePos = PriceDate.index(Date)
    tempPrice = []
    for stock in ToSell:
        try:
            tempPrice.append(float(AllPriceResult[PricePos].ix[:,1][AllPriceResult[PricePos].ix[:,0] == stock].tolist()[0]))
        except:
            print("No Price for"+stock)
            tempPrice.append(np.nan)    
    Price.append(tempPrice)
    NextDate = "{:%Y-%m-%d}".format(datetime.datetime.strptime(Date, '%Y-%m-%d') + datetime.timedelta(days=7))
    flag = 1
    try:
        PricePos = PriceDate.index(NextDate)
    except:
        print("No Data Downloaded")
        flag = 0
    if flag == 0:
        continue
    tempPrice = []
    allStockPos.append(i)
    for stock in ToSell:
        try:
            tempPrice.append(float(AllPriceResult[PricePos].ix[:,1][AllPriceResult[PricePos].ix[:,0] == stock].tolist()[0]))
        except:
            print("No Price for"+stock)
            tempPrice.append(np.nan)
    OneWeekPrice.append(tempPrice)

NewSell = map(Stocks.__getitem__, allStockPos)
NewSellPrice = map(Price.__getitem__, allStockPos)
NewDate = map(SellDate.__getitem__,allStockPos)
result = []
resultmean = []

for i in list(range(0,len(NewSell))):
    result.append(list((-np.array(OneWeekPrice[i]) + np.array(NewSellPrice[i])) /np.array(NewSellPrice[i])))
    resultmean.append(np.nanmean(result[i]))

ProfitFromShort = pd.Series(resultmean,index = NewDate)
nameStore = "/Users/sunjiaxuan/Documents/Py/YahooAnalysts/" + "ProfitFromShort.csv"

ProfitFromShort.to_csv(nameStore)
