import csv 
import pandas as pd
import plotly.express as px
import math as m

with open('class1.csv',newline='') as f:
    reader= csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
totalmarks=0
totalentry=len(filedata)


for entry in filedata:
    totalmarks=totalmarks+float(entry[1])
mean=totalmarks/totalentry
print(mean)

df=pd.read_csv('class1.csv')
graph=px.scatter(df,x='Student Number', y='Marks')
graph.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=totalentry)])
graph.show()

squarelist=[]
for entry in filedata:
    distance=float(entry[1])-mean 
    distance = distance*distance
    squarelist.append(distance)

sum=0
for i in squarelist:
    sum=sum+i
standardDeviation=m.sqrt(sum/totalentry-1)
print(standardDeviation)

