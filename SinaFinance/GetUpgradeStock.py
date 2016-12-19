# -*- coding: utf-8 -*-
#codecs.BOM_UTF8
#这里的是股票综合评级，对于我们的参考意义不是很大，通过研报我们发现真正有意义的是评级上调和首次评级的股票
from bs4 import BeautifulSoup
import requests
import re
import csv
import os
import sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import chardet
import urllib2
import codecs
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
            html_1 = urllib2.urlopen(url,timeout=120).read()
            encoding_dict = chardet.detect(html_1)
            #print encoding to see if we need to do any necessary change
            web_encoding = encoding_dict['encoding']
            if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
                html = html_1
            else :
                #Change the encode of the website to utf-8 to make it readable
                html = html_1.decode('gbk','ignore').encode('utf-8')
            r = html
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            print('Connection Error')
            return
        #Typecially it should be "xlml" but as now we are using string as input, so we use "html.parser"
        #print(r)
        bf = BeautifulSoup(r,"html.parser")
        #print(bf.prettify())
        trs = bf.findAll('tr')#, {"class","list"})
        #print(len(parenttr))
        for tr in trs[1:]:
            tds = tr.find_all("td")
            mylist = list(range(0,7))
            result = []
            for i in mylist:
                result.append(tds[i].text.encode('utf-8'))
            #print(result)
            wr.writerow(result)
        self.status = "Success"
    
    def showStatus(self):
       print(self.status)   


###########Download Data
os.chdir('/Users/sunjiaxuan/Documents/Py/ASharesAnaLystsView')

resultFile = open("RatingUp.csv",'wb')
resultFile.write('\xEF\xBB\xBF') 
wr = csv.writer(resultFile)

for i in range(0,6): #
    print(i)
    url = "http://vip.stock.finance.sina.com.cn/q/go.php/vIR_RatingUp/index.phtml?p=" + str(i)
    #try:
    temp = DataSpider(url)
    temp.sendRequest()
    #except:
    #print("Fail")
    #continue
        
resultFile.close()
