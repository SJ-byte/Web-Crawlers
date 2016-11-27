from bs4 import BeautifulSoup
import requests
import time
import re
import os
import datetime as datetime
print os.getcwd()
os.chdir('/Users/sunjiaxuan/Documents/Py')
import csv
with open('AllQuotes.csv', 'rb') as f:
    reader = csv.reader(f)
    QS = list(reader)
    
name = "/Users/sunjiaxuan/Documents/Py/YahooAnalysts/" + "TodayPrice" + str(datetime.datetime.now())[0:10] + ".csv"

resultFile = open(name,'wb')
wr = csv.writer(resultFile, dialect='excel')

for i in range(0,len(QS)):
    print(i)
    #wr.writerow(''.join(QS[i]))
    url = "https://sg.finance.yahoo.com/q/hp?s=" + ''.join(QS[i])
    try:
        r = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue
    bf = BeautifulSoup(r.text,"lxml")
    try:
        tartr = bf.findAll('th', text = re.compile('High*'))
        tartrre = (tartr[0].find_parent("tr").find_next_sibling("tr"))
    except:
        continue
    #print(tartrre)
    tartds = tartrre.find_all("td")
    #for tartd in tartds:
    if tartds[1].text:
        #print("".join(tartds[1].text.encode('ascii', 'ignore')))
        templist = [''.join(QS[i]).encode('ascii', 'ignore'),str("".join(tartds[1].text.encode('ascii', 'ignore')))]
        wr.writerow(templist)
    else:
        continue

resultFile.close()
    
