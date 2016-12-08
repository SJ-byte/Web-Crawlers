from bs4 import BeautifulSoup
import requests
import re
import csv
import os
import sys


##########Define Spider Class
class DataSpider():
    def __init__(self,url):
        self.url=url
        self.Header={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7"
        }

    
    def sendRequest(self):
        url = self.url
        try:
            r = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return
        bf = BeautifulSoup(r.text,"lxml")
        try:
            parenttr = bf.findAll('tr', {"class","head"})
        except:
            return
        stocktrs = parenttr[0].find_parent("table").find_all("tr")
        mylist = [0,4,5,6,7,8]
        for stocktr in stocktrs[1:]:
            tdsAll = stocktr.findAll('td')
            #print(len(tdsAll)) the length is 13
            result = []
            for i in list(range(0,len(tdsAll))):
                if i in mylist:
                    result.append(tdsAll[i].text)
            wr.writerow(result)
            #print(tdsAll[i].text)
        self.status = "Success"
    
    def showStatus(self):
       print(self.status)   


###########Download Data
os.chdir('/Users/sunjiaxuan/Documents/Py/ASharesAnaLystsView')

resultFile = open("outputBuySellAdvice.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')

for i in range(0,500): #
    print(i)
    url = "http://vip.stock.finance.sina.com.cn/q/go.php/vIR_SumRating/index.phtml?last=10&p=" + str(i)
    try:
        temp = DataSpider(url)
        temp.sendRequest()
    except:
        print("Fail")
        continue
        
resultFile.close()
        
