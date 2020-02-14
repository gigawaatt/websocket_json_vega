import asyncio
import json
import datetime
import csv
import sys


data_02 = []

itog1 = []
itog2 = []

itog11 = []
itog22 = []

with open('response.json') as f:
    templates = json.load(f)
    data_01 = templates['data_list']


for z in data_01:
    data_02.append(z['data'])
    

i = 0

while i < len(data_02):
    if data_02[i][0:2] != "01":
        del data_02[i]    
    else:
        itog1.append(data_02[i][12:14] + data_02[i][10:12] + data_02[i][8:10] + data_02[i][6:8])
        itog2.append(int(data_02[i][22:24] + data_02[i][20:22] + data_02[i][18:20] + data_02[i][16:18], 16))    
        i += 1  

i = 0

itog2.append(0)

while i < len(itog1):
    itog1[i] = int(itog1[i] , 16)
    itog1[i] = datetime.datetime.fromtimestamp(itog1[i])
    itog1[i] = str(itog1[i].strftime('%Y-%m-%d %H:%M:%S'))
    itog2[i] = abs(itog2[i+1]-itog2[i]) 
    i += 1

del itog2[len(itog2)-1]

i = 0
z = 0

while i < len(itog1):
    if itog2[i] != 0:
        itog11.append(itog1[i])
        itog22.append(itog2[i])
        i += 1
    else:
        i += 1

itog11.reverse()
itog22.reverse()
itog = dict(zip(itog11 , itog22))
itog = itog.items()



def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)


path = "output.csv"

csv_writer(itog, path)

#print(itog)