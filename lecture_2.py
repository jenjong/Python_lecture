# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:13:04 2018

@author: Jeon
"""
# MATHMATICAL FUNCTIONS
# numpy array
import numpy as np
# create 1D-array
## from list
a = np.array([3,1,2,4,])
print(a)
## from tuple
a = np.array((3,1,2,4,))
type(a)
## check the result: from dict, from set
a = np.array({'v1':3, 'v2':1, 'v3':2,'v4':4,})
a = np.array(set({1,2,4,}))

# data type
a = np.array([3,1,2,4,])
a.dtype
a = np.array([3.,1.,2.,4.,])
a.dtype
a = np.array([3,1,2,4,], dtype = 'float32')
a.dtype
a = np.array([3,1,2,4,], dtype = float)
a.dtype
# change the data type
a = a.astype('float32')
a.dtype


a_r = np.array([3,1,2,4,])
a_l = [3.,1.,2.,4.]
# power
2**(4)
2**(0.5)
pow(2,0.5)

# check the result
a_l**(4)
pow(a_l, 4)

a_r**(4)
pow(a_r, 4)

# dtype



# quotient
5//2
# remains
5%2


# matrix
a = list([3,1,2,4,6,5])
a = np.array(a, dtype = 'f')
type(a)
a.dtype

a.sum()
a.argmin()
a.argmax()
# cumulative sum
np.cumsum(a)
a.cumsum()
# reshape
a
np.reshape(a,(2,3))
b = a.reshape((2,3))

# one row
b = np.reshape(range(0,30), (10,3))
# the third row
b[2]
# the third and fourth row
b[2:4]
# the second column, the result is array
b[:,1]
# the second column, the result is matrix
b[:,1:2]
np.reshape(b[:,1], (10,1))
# matrix
x = np.random.normal(size = 100)
x = x.reshape(20,5)

x = np.array(range(0,100))

x = np.arange(1,101,1, dtype=float)
x = np.linspace(1,2,20)
np.repeat( np.array([0,2,4]) , [2,3,4])
# dimension
x = x.reshape(20,5)


# matrix
x = np.random.normal(size = 100)
x = x.reshape(20,5)
# covariance
x_cov = np.cov(x, rowvar = False)
# correlation
x_corr = np.corrcoef(x, rowvar = False)



x_cov = np.array([1,0.5,0.5,1])
x_cov = x_cov.reshape(2,2)

a, b = np.linalg.eig(x_cov) 
# eigenvalue
a
# eigen matrix
b
# 
np.argsort(-a)
np.dot(b[0,:], b[1,:])
# singular value decomposition
x_cov = np.array([1,0.5,0.5,1])
x_cov = x_cov.reshape(2,2)
U, D, Vt = np.linalg.svd(x_cov)

# indexing
a[a<.5]

np.isnan(np.nan)


# function
# lambda function

list(map(lambda x: x ** 2, range(5)))

from functools import reduce
# x takes the return at previous step and y takes a current input!
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
reduce(lambda x, y: x + y, (0, 1, 2, 3, 4)) 
data = 'abcde'
reduce(lambda x, y: x + y, data) 
reduce(lambda x, y: y + x, data) 
# x = null, y ="a"  -> y+x = 'a'
# x = 'a', y ='b'  -> y+x = 'ba'
# x = 'ba', y ='c'  -> y+x = 'cba' ... 
# 



reduce(lambda x, y: x + y, [0])
