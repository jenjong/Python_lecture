# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:19:09 2020

@author: Jeon
# iterator
"""
import os 
# while 구문의 기본
i = 0
while i<3:
    print("Hi, Code number " + str(i)+ '!') 
    i=i+1

# break를 통한 while의 제어
i = 0
while True:
    if i>=3:
        break
    print("Hi, Code number " + str(i)+ '!') 
    i=i+1

# for 구문의 기본: range(1,11,1)은 1:10 in R
# ex-1
v = 0
for i in range(1,11,1):
    v = v + i
v    
    
# ex-2
# for 문은 반복자(iterator)를 제공하는 컨테이너라면 모두 순회할 수 있다.
v = ["You", "are", "a", "smart student", "of", "UOS."]
for i in v:
    print(i)
    
v = ("I", "am", "a", "talkative", "guy!")    
type(v)   
for i in v:
    print(i)
# Dictionary 도 가능한가?
    
    
# iter() 함수는 전달된 데이터의 반복자를 꺼내 반환한다. 
# next() 함수는 반복자를 입력받아 그 반복자가 다음에 출력해야 할 요소를 반환한다.
# iter() 함수로 반복자를 구하고 그 반복자를 next() 함수에 전달하여 요소를 차례대로 꺼낼 수 있다.

it = iter([1, 2, 3])  # [1, 2, 3]의 반복자 구하기
next(it)   
next(it)
next(it)   
next(it)

it.__next__() 


# iterator 예
import csv
train_file_path = 'C:/Users/Jeon/Documents/data/train.csv'
!head {train_file_path}
f = open(train_file_path, 'r', encoding='utf-8')
rdr = csv.reader(f)
i = 0
for line in rdr:
    print(i)
    i += 1
    print(line)
f.close()    
# 여기서 rdr 이라는 것도 반복자를 가지고 있음을 예상
f = open(train_file_path, 'r', encoding='utf-8')
rdr = csv.reader(f)
it = iter(rdr)  # [1, 2, 3]의 반복자 구하기
it
next(it)   
next(it)   
next(it)   

# for 문의 구조에 대해서 생각해보자.
# 1. 순회하려는 컨테이너로 부터 반복자 객체를 얻는다.
# 2. 반복자 객체는 next() 에 넣어 값을 얻고 그것을 변수에 저장한다.
# 3. 그 변수값을 이용하여 for 아래 구문을 실행한다. 
# 4. 반복자의 오류가 발생할 때까지 계속 반복한다.



# 참조:: 생성기 (iterator 기능을 하는 함수)
def one_to_infinite():
    n=1
    while True:
        yield n
        n += 1
# 함수지만 실행되지 않는다.
one_to_infinite() 
# 변수로 저장하고
natural_numbers = one_to_infinite() 
# 다음과 같이 next를 이용해서 실행한다.
next(natural_numbers)
