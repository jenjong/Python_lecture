# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:50:11 2019

@author: Jeon
"""

s1 = set([1,2,3,1,4])
a = {}
type(a)
a = set(a)
type(a)

result = 0
def add(num):
    global result
    result += num
    return(result)

add(3)
add(4)
# Class


class Cal:
    # Intialize the value used in the instance
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
    
cal1 = Cal()    
cal2 = Cal()
cal1.add(3)
cal1.add(4)
cal1
id(cal2)


class MoreCal(Cal):
    pass

mcal1 = MoreCal ()
mcal1.add(3)

class MoreCal(Cal):
    def add2(self, num):
        self.result += (num + 100)
        return self.result

    
        
mcal1 = MoreCal ()
mcal1.add(3)
mcal1.add2(3)

mcal2 = MoreCal ()
mcal2.add(3)
mcal2.add(3)

# Module