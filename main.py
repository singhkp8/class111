import csv
import pandas as p
import random
import plotly.figure_factory as pff
import statistics

df = p.read_csv('medium_data.csv')
data = df["id"].tolist()



def RamdonSetOfMeans(counter):
    list1 = []

    for i in range(0,counter):
        ramdonIndex = random.randint(0,len(data) - 1 )
        value = data[ramdonIndex]
        list1.append(value)
    mean = statistics.mean(list1)
    return mean

meanList = []
for i in range(0,1000):
    SetOfMeans = RamdonSetOfMeans(100)
    meanList.append(SetOfMeans)

population_mean = statistics.mean(meanList)
print(population_mean)

std = statistics.stdev(meanList)
print(std)

