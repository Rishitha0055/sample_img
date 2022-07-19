import os
import csv
import pandas as pd
path='/home/tgt/Desktop/segregatation/wrongtag1.csv'
df=pd.read_csv(path)
#print(df)
list1 = [df]

result = list()
centercode=[]
for df in list1:
    result += df.values.flatten().tolist()
    #print(result)
    for j in map(str,result):
        a,b=j[0:6],j[6:12]
        #print(int(a))
        centercode.append(a)
        print(centercode)
