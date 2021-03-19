import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee=[]
    sleep=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row['coffee in ml']))
            sleep.append(float(row['sleep']))
    return{"x":coffee in ml,"y":sleep}

def findCorelation(dataSource):
    corelation= np.corrcoef(dataSource["x"],datasource["y"])
    print('Corelation between coffee and sleep is '+ corelation[0,1])

def setup():
    data_path='CoffeevsSleep.csv'
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)

setup()

#with open("CoffeevsSleep.csv") as csv_file:
 #   df= csv.DictReader(csv_file)
  #  fig= px.scatter(df,x='Coffee in ml',y="sleep")
   # fig.show()