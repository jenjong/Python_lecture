# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:51:47 2020

@author: Jeon
"""
import tensorflow as tf

# elementary operation
a = tf.add(1,2)
type(a)
a
print(a)
tf.add([1,3], [4,5])
tf.square(3)
tf.reduce_sum([1,2,3])
tf.add(tf.square(5), tf.square(4))


# type 
tf.add(1.0,2.0)
tf.square(3.0)

# define tensor
# 1. constant
tf.constant(3.0)
tf.constant(3)
tf.constant(3, dtype = 'float32')
tf.constant(3, dtype = 'int32')

a1 = tf.constant([1,2,3], dtype ='float32')
a2 = tf.constant([4,7,9], dtype ='float32')
a1 + a2
tf.add(a1, a2)

a3 = tf.constant([1,2,3], shape = (3,1), dtype ='float32')
a4 = tf.constant([4,7,9], shape = (1,3), dtype ='float32')
tf.matmul(a3, a4)

# note tf matmul
a3 = tf.constant([1,2,3],  shape = (1,3), dtype ='float32')
a4 = tf.constant([4,7,9],  shape = (1,3), dtype ='float32')
tf.matmul(a3, a4, transpose_a = True)
tf.matmul(a3, a4, transpose_b = True)


x = tf.matmul(a3, a4, transpose_a = True)
x.shape
x.dtype


# tensor vs numpy
import numpy as np
ndarray = np.ones([3, 3])
print("텐서플로 연산은 자동적으로 넘파이 배열을 텐서로 변환합니다.")
tensor = tf.multiply(ndarray, 42)
print(tensor)
print("그리고 넘파이 연산은 자동적으로 텐서를 넘파이 배열로 변환합니다.")
print(np.add(tensor, 1))
print(".numpy() 메서드는 텐서를 넘파이 배열로 변환합니다.")
print(tensor.numpy())

# ok?
x.numpy()