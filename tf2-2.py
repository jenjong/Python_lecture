# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:10:34 2020

@author: Jeon
tensorflow dataset
"""
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.set_printoptions(precision=4)
x = np.random.sample((100,2))
dataset = tf.data.Dataset.from_tensor_slices(x)
dataset
# iterator for each row
for a in dataset: 
  print(a) 

# iterator for each row
features, labels = (np.random.sample((100,2)), np.random.sample((100,1)))
type(features)
type(labels)
dataset = tf.data.Dataset.from_tensor_slices((features,labels))
for a in dataset: 
  print(a) 
# explcit iterator in python
it = iter(dataset)
it  
# for example, 0x189ba08f1d0
next(it)
it
a = next(it)
a[0].numpy()
a[1].numpy()

