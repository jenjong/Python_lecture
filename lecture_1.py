# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:48:21 2018
@author: Jeon
"""
import os
from pandas import Series, DataFrame
# Series and DataFrame are classes defined in pandas
# we can use Series instead of pandas.Series
import pandas as pd
import numpy as np
# check the working directory
os.getcwd()
# set my working directory
current_dir = 'C:/Users/Jeon/Documents/GitHub/Python_lecture'
home = os.path.expanduser("~")
current_dir = home + '\\Documents\\GitHub\\Python_lecture'
os.chdir(current_dir)
os.getcwd()
# read a csv file:  'header = None'
rdata = pd.read_csv("iris.data", header=None)
# select columns
rdata[[1]]
rdata[[0,2,4]]
type(rdata[[1]])
# read a csv file: 
cdata = pd.read_csv('CO2.csv', header ='infer')
# 다음을 확인하시오: cdata[[0]], cdata[[1]],...
cdata.columns
rdata.columns
cdata_colnames = list(cdata.columns)
c1 = cdata[cdata_colnames[0]]
c2 = cdata[[cdata_colnames[0]]]
type(c1)
type(c2)
type(cdata)

# show the column names; columns is variable included in rdata 
list(rdata.columns)
# set the new column names in rdata
rdata.columns = ['sepal_length', 'Sepal_width', 'petal_length', 
'petal_width', 'class']
# check the column names again
rdata['sepal_length']
# change the second column names as 'sepal_width'
rdata.columns[1] = 'sepal_width' # does not work
# see the following code. Not easy!
rdata.rename(columns = {'Sepal_width':'sepal_width'}, inplace = True)
# 
rdata.rename(columns = {'Sepal_width':'sepal_width',
                        'petal_length':'Petal_length'}, inplace = True)

# show head of dataframe
rdata.head(n=2)

# slicing the row
rdata.iloc[:5]

# delete the selected row
# the fifth row and the first col
rdata.drop(5,0)
#
# 4~5
rdata.drop([4,5],0)
# note that it does not work
# rdata.drop(4:6,0)
idx = [0,4,6,8,10]
rdata.drop(idx,0)

# show the columns
rdata[:2]


colname = list(rdata.columns)
type(colname)
rdata[colname[1]]
rdata[colname[2:]]

# delete columns
rdata.drop("class", 1)


# choose the block matrix in the dataframe
rdata[:2].iloc[0:5]

# choose multiple elements by lambda function
# in R colname[1,3]
[colname[i] for i in [1,3]]
# choose multiple columns in the dataframe by location
rdata[ [colname[i] for i in [0,2] ] ]
# + head()
rdata[ [colname[i] for i in [0,2] ] ].head()
# Note that the meaning of header = 0 in read_csv

# select several rows
# the first and the second rows
rdata[ [colname[i] for i in [0,2] ] ].iloc[0:2]
# the first to the fifth rows
rdata[ [colname[i] for i in [0,2] ] ].iloc[:5]



# object list
# create list
L1 = [10,20,30]
# print the list 
print(L1)
# call an element in the list
print( L1[2] )
# check the type of L1
type(L1)
# check the type of an element in L1
type(L1[0])

# creat another list
L2 = [10, 20.0, 30]
type(L2[0])
type(L2[1])

# creat another list
L3 = [1,[10,20,30],3]
L3[1]

# create another list
L4 = [1,[10,20,30],3]
L5 = ['a', 'b', [1,2,3], [5,6]]

# 
len(L4)


# append and extend
b = [1,2,3]
b.append(1)
b
b.extend(b)
b
# note that the first element in b is added in b again
b.append(b)
len(b)


# which
['a','a','b'].index('a')

# paste
"hi" + str(3)
# concatenating
['hi','there'] + ['3','4']

# paste
list( map(lambda x,y: x + y , ['hi','there'], ['3','4']))


# tuple
a = (1,2,3)
a
a[1] = 3
a = 1,2,3
a


# make dictionary
data = {'state': ['A','A', 'B','B','B'],
        'year': [2000, 2001, 2002, 2003, 2002],
        'pop': [1.5, 1.5, 1.4, 1.3, 1.1]
        }
# check the class of 'data' object
type(data)
# print the values corresponding to the key 'state'
data['state']
# make v1 by data['state']
v1 = data['state']
# check the class of 'v1'
type(v1)
# 
frame = DataFrame(data)
frame.state
frame.year

frame['year']

# series
x = pd.Series([1,3,5])
type(x)
x[[0,2]]
pd.date_range('20130101', '20130331')
dates = pd.date_range('20130101', periods = 6)
df = DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
list('ABDF')

a = [1,3,5,4,2]
a.sort(reverse = True)
a
a = ['Life', 'is', 'too', 'short'] 
' '.join(a)
