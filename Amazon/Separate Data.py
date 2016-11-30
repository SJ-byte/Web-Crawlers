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
    print(files)
    if 'AmazonYSL' in files:
        AllResult.append(pd.read_csv(files,header = None))

mapping = AllResult[0].ix[1:,1]

Combined_R = pd.DataFrame()

for i in list(range(0,len(AllResult))):
    print(i)
    if i == 0:
        Combined_R = AllResult[0].iloc[1:]
        Combined_R.columns = ['Price','Name']
        Combined_R = pd.DataFrame(Combined_R['Price'].values,index = Combined_R['Name'].values) #list(range(0,len(mapping)))
    else:
        temp = AllResult[i]
        temp = temp.iloc[1:] #No Header
        temp.columns = ['Price','Name','Notes']
        temp = temp.ix[:,0:2]
        temp = pd.DataFrame(temp['Price'].values,index = temp['Name'].values)
        temp.columns = ['price' + str(i)]
        #tempDF = pd.DataFrame(AllResult[i].ix[:,0].values,index = [AllResult[i].ix[:,1]])
        #print(tempDF.iloc[0:3])
        #Combined_R = Combined_R.join(temp, on = ['Name'], how='outer')
        Combined_R = Combined_R.join(temp)
        Combined_R = Combined_R.drop_duplicates()
        print(Combined_R.shape)


Combined_R['change'] = Combined_R.ix[:,-1] - Combined_R.ix[:,1]
New_Low = Combined_R.ix[Combined_R['change']<0,:]
New_Low = New_Low.sort_values(['change'])
New_Low = New_Low.drop_duplicates()
name = "/Users/sunjiaxuan/Documents/Py/AmazonPrice/" + "PriceChange" + str(datetime.datetime.now())[0:10] + ".csv"
New_Low.to_csv(name)
