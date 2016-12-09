from bs4 import BeautifulSoup
import requests
import re
import csv
import os

##########Define Spider Class
class DataSpider():
    def __init__(self,url,EquityName,FileName = "output.csv"):
        self.url=url
        self.Header={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7"
        }
        self.EquityName = EquityName
        self.FileName = FileName
    
    def openFile(self):
        self.resultFile = open(self.FileName,'wb')
        self.wr = csv.writer(self.resultFile, dialect='excel')
        
    def closeFile(self):
        self.resultFile.close()
    
    def sendRequest(self):
        url = self.url
        try:
            r = requests.get(url)
            #print(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return
        bf = BeautifulSoup(r.text,"lxml")
        ####For first part
        try:
            tarth = bf.findAll('th', text = re.compile('Recommendation Summary*'))
            tarthre = (tarth[0].find_parent("tr").find_parent("table").find_next_sibling("table"))
            #print(tarthre.text.strip())
        except:
            return
        tartrs = tarthre.find_all("tr")
        for tartr in tartrs:
            wr.writerow("".join(tartr.text.encode('ascii', 'ignore')))
        ####For second part
        tarth = bf.findAll('th', text = re.compile('Price Target Summary'))
        tarthre = (tarth[0].find_parent("tr").find_parent("table").find_next_sibling("table"))
        tartrs = tarthre.find_all("tr")
        for tartr in tartrs:
            wr.writerow(tartr.text.encode('ascii', 'ignore').decode('ascii'))
        ####For Third part
        tarth = bf.findAll('th', text = re.compile('Upgrades & Downgrades History'))
        tarthre = (tarth[0].find_parent("tr").find_parent("table").find_next_sibling("table"))
        tartrs = tarthre.find_all("tr")
        for tartr in tartrs:
            tds = tartr.find_all("td")
            tdsout = ''
            for td in tds:
                if td.text:
                #tdsout = tdsout + td.text 
                    wr.writerow(td.text.encode('ascii', 'ignore').decode('ascii'))
        ####For Last part
        tarth = bf.findAll('th', text = re.compile('Recommendation Trends'))
        tarthre = (tarth[0].find_parent("tr").find_parent("table").find_next_sibling("table"))
        #print(tarthre.text)
        #Find the columns of the table
        ths = tarthre.find_all("th",{'scope',"col"})
        #for th in ths:
            #print(th.text)
        tartrs = tarthre.find_all("tr")
        for tartr in tartrs:
            tds = tartr.find_all("td")
            tdsout = ''
            for td in tds:
                if td.text:
                #tdsout = tdsout + td.text 
                    wr.writerow(td.text.encode('ascii', 'ignore').decode('ascii'))
        self.status = "Success"
    
    def showStatus(self):
       print(self.status)   


###########Download Data
os.chdir('/Users/sunjiaxuan/Documents/Py/YahooAnalysts')

with open('AllQuotes.csv', 'rb') as f:
    reader = csv.reader(f)
    QS = list(reader)

resultFile = open("output.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')

for i in range(0,len(QS)): #
    print(i)
    url = "https://sg.finance.yahoo.com/q/ao?s=" + ''.join(QS[i])
    try:
        temp = DataSpider(url,''.join(QS[i]))
        temp.sendRequest()
    except:
        print("Fail")
        continue
        
resultFile.close()

with open("output.csv") as infile, open("outfile.csv", "w") as outfile:
    for line in infile:
        outfile.write(line.replace(",", ""))
        
import AnalyseYahooResult
import YahooGetPrice
import YahooStrategyMain
import GetProfit
