# -*- coding: utf-8 -*-
#Stephon Kumar
#stephon.kumar13@myhunter.cuny.edu
#Python3 Final 


import sys 
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import seaborn as sns
import csv 

#read csv file
project = pd.read_csv('nycrest.csv', index_col=0)

#columns to be used 
project = project[['DBA','BORO','ZIPCODE','CUISINE DESCRIPTION','CRITICAL FLAG','SCORE','GRADE']]

project = project.dropna()

project = project[project.GRADE != 'Z']
project = project[project.GRADE != 'P']
project = project[project.GRADE != 'Not Yet Graded']
project = project[project.BORO != 'Missing']
project = project[project.BORO != 'STATEN ISLAND']
project = project.reset_index()

project.head()

#bar graph of count and grade per boro
sns.countplot(y = 'GRADE', data=project, hue='BORO', palette='Greens_d')
plt.style.use("fivethirtyeight")

#piechart for all boros
criticalgraph = project[["CRITICAL FLAG", "GRADE"]]
critnona = criticalgraph.dropna()
critnona["GRADE"].value_counts().plot(kind="pie", title = "All Boros")
