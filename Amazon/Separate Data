import os
import datetime as datetime
import glob
import pandas as pd
import csv

print os.getcwd()
os.chdir('/Users/sunjiaxuan/Documents/Py/AmazonPrice')
AllFiles = glob.glob("/Users/sunjiaxuan/Documents/Py/AmazonPrice/*.csv")

AllResult = []
for files in AllFiles:
    AllResult.append(pd.read_csv(files,header = None))

toitems = AllResult[0].shape[0]
Combined_R = AllResult[0]
Combined_R.columns = ['Price','Name']
Combined_R = Combined_R[['Name','Price']]
for i in list(range(1,len(AllResult))):
    temp = AllResult[i]
    temp = temp.iloc[1:] #No Header
    temp.columns = ['Price','Name','Notes']
    temp = temp.ix[:,0:2]
    #tempDF = pd.DataFrame(AllResult[i].ix[:,0].values,index = [AllResult[i].ix[:,1]])
    #print(tempDF.iloc[0:3])
    #Combined_R = Combined_R.join(temp, on = ['Name'], how='outer')
    Combined_R = pd.merge(Combined_R,temp ,on = 'Name', how='outer')
    print(Combined_R.shape)


Combined_R['change'] = Combined_R.ix[:,-1] - Combined_R.ix[:,1]
New_Low = Combined_R.ix[Combined_R['change']<0,:]
New_Low = New_Low.drop_duplicates()
name = "/Users/sunjiaxuan/Documents/Py/AmazonPrice/" + "PriceChange" + str(datetime.datetime.now())[0:10] + ".csv"
New_Low.to_csv(name)
