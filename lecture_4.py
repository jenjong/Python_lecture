# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 23:21:57 2018

@author: Jeon
"""
import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


current_dir = 'C:/Users/Jeon/Documents/GitHub/Python_lecture'
os.chdir(current_dir)
TRAIN_DIR = './data/MNIST/trainingSet/'
train_folder_list = array(os.listdir(TRAIN_DIR))

train_input = []
train_label = []
#Factor in R?s??
# intialize the label encoder
label_encoder = LabelEncoder()
# set values in the label encoder
label_encoder.fit(train_folder_list)
# transform the values as integers
integer_encoder = label_encoder.transform(train_folder_list)
# cf:
label_encoder.inverse_transform(np.array(range(0,9)))
onehot_encoder = OneHotEncoder(sparse = False)

#see http://www.birc.co.kr/2018/02/26/