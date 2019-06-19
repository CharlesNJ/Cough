import os, csv

f=open("C:/Users/Charles/Desktop/AI Cough Detection/cough/audio_cough only/cough/filenmes.csv",'r+')
w=csv.writer(f)
for path, dirs, files in os.walk("C:/Users/Charles/Desktop/AI Cough Detection/cough/audio_cough only/cough"):
    for filename in files:
        w.writerow([filename])