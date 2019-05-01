# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:44:53 2019

@author: Jeon
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from scipy.linalg import toeplitz
p = 10
n = 20000
rho = 0.5
a = toeplitz(np.array(range(p), dtype = float) )
Sigma_mat = pow(rho, a)
mu_vec = np.zeros(p)
x = np.random.multivariate_normal(mu_vec, Sigma_mat, n)
y = np.random.choice(np.array([0,1], dtype = float), n , True)

model = keras.Sequential(
        [layers.Dense(20, activation = 'relu', kernel_initializer ='orthogonal', input_shape=(p,)),
        layers.Dense(20, activation = 'relu'),
        layers.Dense(1)])
# See 
optimizer = tf.keras.optimizers.RMSprop(0.001)
# optimizer: RMSprop, SGD, Adam
# optimizer = tf.keras.optimizers.SGD(0.001)
model.compile(loss = 'binary_crossentropy',
             optimizer = optimizer,
             metrics = ['mae', 'mse', 'accuracy'])
model.summary()
model.predict(x)
model.fit(x,y, epochs = 20, batch_size = 300)
score = model.evaluate(x,y)


