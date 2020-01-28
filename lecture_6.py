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

# id returns the address of class
id(cal1)
id(cal2)


# practice (l_r norm)
class norm:
    def my_init(self, r):
        self.r = r
    
    def dist(self, x1, x2):
        v = pow( pow(abs(x1),self.r) + pow(abs(x2),self.r), 1/self.r)
        return v
    
a = norm() # what is diffent between jcl() and jcl
a.dist(1,3) #error because self don't have values.
a.my_init(2)  # l_2 norm
a.dist(3,4)

a.my_init(1)  # l_1 norm
a.dist(3,4)

# compare a0 with a

a0 = norm
a0.my_init(2)  # does not work. the function including self is implemented when instance is made.
a = a0() # a is instance but a0 is just class
a.my_init(2) # l_2 norm

# Suppose that the user implement the code as follows.
a = norm()
a.dist(3,4)
# We have to notice the tntitialization is required everytime? 
# Can the class takes the values required as class variable when the instance is created?
# use __init__ !!!

class norm:
    def __init__(self, r):
        self.r = r
    
    def dist(self, x1, x2):
        v = pow( pow(abs(x1),self.r) + pow(abs(x2),self.r), 1/self.r)
        return v

a = norm() # error! 
a = norm(2)
a.dist(3,4)


# Ok! suppose that we create a new class with addition functions to norm.
# Then we entirely remake the class? No. it is not necessary if we use  override(상속)
# override!
class newnorm(norm):
    pass

# newnorm is the same class as norm. Let add additional method to the newnorm

class newnorm(norm):
    def dist2(self, x1,x2):
        v = pow(abs(x1),self.r) + pow(abs(x2),self.r)
        return v
    
       

a = newnorm(2)
a.dist(3,4)    
a.dist2(3,4)    


# ok! if we want to replace the method with the same name how can we do?
class newnorm2(norm):
    def dist(self, x1,x2):
        v = pow(abs(x1),self.r) + pow(abs(x2),self.r)
        return v
a = newnorm2(2)
a.dist(3,4)    
a.dist2(3,4) # error!  Because of absence of method dist2.


        
