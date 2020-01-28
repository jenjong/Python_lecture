# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:03:48 2020

@author: Jeon

advanced read files (대용량 계산을 위한 파일 읽기)
"""
import numpy as np
import tensorflow as tf
# digit expression option
np.set_printoptions(precision=4, suppress=True)

train_file_path = 'C:/Users/Jeon/Documents/data/train.csv'
!head {train_file_path}
# 위에서 파일 구조를 대충 확인할 수 있음

# 여기서 predicted variable 정하기 (하나만 하면 됨)
LABEL_COLUMN = 'survived'
LABELS = [0, 1]

# 찾아보기: tf.data.experimental.make_csv_dataset()
def get_dataset(file_path, **kwargs):
    dataset = tf.data.experimental.make_csv_dataset(
    file_path,
    batch_size=5, # Artificially small to make examples easier to show.
    label_name=LABEL_COLUMN,
    header = True,
    shuffle = False,
    na_value="?",
    num_epochs=1,
    ignore_errors=True, 
    **kwargs)
    return dataset

raw_train_data = get_dataset(train_file_path)

def show_batch(dataset):
  for batch, label in dataset.take(1):
    for key, value in batch.items():
      print("{:20s}: {}".format(key,value.numpy()))

show_batch(raw_train_data)

SELECT_COLUMNS = ['survived', 'age', 'n_siblings_spouses', 'class', 'deck', 'alone']
temp_dataset = get_dataset(train_file_path, select_columns=SELECT_COLUMNS)
show_batch(temp_dataset)


SELECT_COLUMNS = ['survived', 'age', 'n_siblings_spouses', 'parch', 'fare']
DEFAULTS = [0, 0.0, 0.0, 0.0, 0.0]
temp_dataset = get_dataset(train_file_path, 
                           select_columns=SELECT_COLUMNS,
                           column_defaults = DEFAULTS)
# iter: iterator 값을 보자. 
example_batch, labels_batch = next(iter(temp_dataset)) 
# 
example_batch
type(example_batch)
len(example_batch)
example_batch['age'].numpy()
labels_batch.numpy()

show_batch(temp_dataset)
