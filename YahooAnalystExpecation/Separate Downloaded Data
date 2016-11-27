import os
import datetime as datetime

print os.getcwd()
os.chdir('/Users/sunjiaxuan/Documents/Py')
import csv
with open('AllQuotes.csv', 'rb') as f:
    reader = csv.reader(f)
    AllQu = list(reader)

with open('outfile.csv', 'rb') as f:
    reader = csv.reader(f)
    rel = list(reader)

rawall = []
for i in list(range(0,len(AllQu)-1)):
    quo = AllQu[i]
    quonext = AllQu[i+1]
    for j in list(range(0,len(rel))):
        #print(quo)
        
        if quo == rel[j]:
            pos1 = j
            #print(rel[j]==quo)
            for m in list(range(0,300)):
                #print(m)
                try: #If we have already passed the limit of the rel
                    if quonext == rel[j+m]:
                        #print(2)
                        pos2 = j+m
                        break
                except:
                    pos2 = len(rel)
            break
    #print(len(rel))
    rawall.append(rel[pos1:pos2])

rec_with_value = []
for i in list(range(0,len(rawall))):
    if len(rawall[i]) > 2:
        rec_with_value.append(rawall[i][0:3])

for i in list(range(0,len(rec_with_value))):
    if ('N/A' not in ''.join(rec_with_value[i][1]))&('N/A' not in ''.join(rec_with_value[i][2])):
        try:
            rec_with_value[i][1] = float(''.join(rec_with_value[i][1])[-3:])
            rec_with_value[i][2] = float(''.join(rec_with_value[i][2])[-3:])
        except:
            continue
    else:
        rec_with_value[i][1] = ''.join(rec_with_value[i][1])[-3:]
        rec_with_value[i][2] = ''.join(rec_with_value[i][2])[-3:]
        
name = "/Users/sunjiaxuan/Documents/Py/YahooAnalysts/" + "YahooAnalystsRecScore_" + str(datetime.datetime.now())[0:10] + ".csv"

with open(name, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in list(range(0,len(rec_with_value))):
        wr.writerow(rec_with_value[i])
        
Tar_with_value = []
for i in list(range(0,len(rawall))):
    if len(rawall[i]) > 12:
        Tar_with_value.append([rawall[i][index] for index in [0,4,5,6,7,8]])

for i in list(range(0,len(Tar_with_value))):
    if ('N/A' not in ''.join(Tar_with_value[i][0]))&('N/A' not in ''.join(Tar_with_value[i][1])):
        try:
            Tar_with_value[i][1] = float(filter(str.isdigit, str(Tar_with_value[i][1])))/100
            Tar_with_value[i][2] = float(filter(str.isdigit, str(Tar_with_value[i][2])))/100
            Tar_with_value[i][3] = float(filter(str.isdigit, str(Tar_with_value[i][3])))/100
            Tar_with_value[i][4] = float(filter(str.isdigit, str(Tar_with_value[i][4])))/100
            Tar_with_value[i][5] = float(filter(str.isdigit, str(Tar_with_value[i][5])))
        except:
            continue
    else:
            Tar_with_value[i][1] = ''.join(Tar_with_value[i][1])[-3:]
            Tar_with_value[i][2] = ''.join(Tar_with_value[i][2])[-3:]
            Tar_with_value[i][3] = ''.join(Tar_with_value[i][3])[-3:]
            Tar_with_value[i][4] = ''.join(Tar_with_value[i][4])[-3:]
            Tar_with_value[i][5] = ''.join(Tar_with_value[i][5])[-3:]

name = "/Users/sunjiaxuan/Documents/Py/YahooAnalysts/" + "YahooAnalystTargetP_" + str(datetime.datetime.now())[0:10] + ".csv"

with open(name, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in list(range(0,len(Tar_with_value))):
        wr.writerow(Tar_with_value[i])
