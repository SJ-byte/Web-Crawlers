import os
import datetime as datetime
import glob
import pandas as pd
import csv
import numpy as np
import operator

#print os.getcwd()
os.chdir('/Users/sunjiaxuan/Documents/Py/ASharesAnalystsView')
AllFiles = glob.glob("/Users/sunjiaxuan/Documents/Py/ASharesAnalystsView/*.csv")
UpFiles = []
UpExistDate = []
FirstFiles = []
FirstExistDate = []

for files in AllFiles:
    if "RatingUp" in files:
        RatingUpDataAll = files
    elif "RatingFirst" in files:
        RatinFistpDataAll = files
    elif "UpStock" in files:
        UpFiles.append(files)
        UpExistDate.append(files[-14:-4])
    elif "FirstStock" in files:
        FirstFiles.append(files)
        FirstExistDate.append(files[-14:-4])
    
RUp = pd.read_csv(RatingUpDataAll,header = None)
RUp.columns = ['Stock','Name','Rating','SecurityName','Analyst','Indusry','Date']
UniqueDate = RUp.Date.unique()
#AllExistDate = 

for date in UniqueDate:
    if date not in UpExistDate:
        temp = RUp.ix[RUp.Date==date,:]
        nameStore = "/Users/sunjiaxuan/Documents/Py/ASharesAnalystsView/UpStock"+date+".csv"
        temp.to_csv(nameStore,index=False)
    
RFirst = pd.read_csv(RatinFistpDataAll,header = None)
RFirst.columns = ['Stock','Name','Target','Rating','SecurityName','Analyst','Indusry','Date']
UniqueDate = RFirst.Date.unique()

for date in UniqueDate:
    if date not in FirstExistDate:
        temp = RFirst.ix[RFirst.Date==date,:]
        nameStore = "/Users/sunjiaxuan/Documents/Py/ASharesAnalystsView/FirstStock"+date+".csv"
        temp.to_csv(nameStore,index=False)
