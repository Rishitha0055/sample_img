import os
import numpy as np 
import pandas as pd
import cv2
import csv
import shutil
path_csv_data='/home/tgt/Downloads/wrongtag_05-05-2022/wrongtag_evening_05_05_2022.csv'

path_dir='/home/tgt/Downloads/wrongtag_05-05-2022/evening'
#path ='/home/tgt/Downloads/wrongtag_05-05-2022/EVENING_PHOTOS'
length = 0
df=pd.read_csv(path_csv_data)
rollnos = list(df['rollno'])
rollnos = [str(i)  for i in rollnos]
print(type(rollnos[0]))
for subdir, dirs, files in os.walk(path):
    for file in files:
        #print(file)
        new_file = os.path.join(subdir, file)
        f= file.split('/')[-1].split('.')[0].split('_')[0] 
        #print(f)
        if f not in rollnos:
            length = length+1
            
            #print("the.........",f)
           
