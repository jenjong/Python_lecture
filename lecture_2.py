# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:13:04 2018

@author: Jeon
"""
# MATHMATICAL FUNCTIONS
import numpy as np
a = np.array([1,2,3,7,9])


2**(2)
pow(2,2.3)
# quotient
5//2
# remains
5%2


# matrix
a = list([3,1,2,4,6,5])
a = np.array(a)
type(a)
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


