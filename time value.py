# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 09:45:14 2018

@author: cuity328
"""
import math
def future_value(v,t,r):
    vt=float(v*(1+r)**t)
    print vt
    return vt

def present_value(vt,t,r):
    v=float(vt/(1+r)**t)
    print v
    return v

def time(v,vt,r):
    t=float(math.log(vt/v,(1+r)))
    print t
    return t

def rate(v,vt,t):
    r=float((vt/v)**(1./t)-1)
    print r
    return r

#question 1
rate(21308.00,27958.00,6.00)

#question 2
time(35000.00,180000.00,0.05)

#question 3
present_value(650000000.00,17.00,0.095)

#question 4
present_value(4500000.00,73.00,0.08)

#question 5
future_value(55.00,87.00,0.07)

#question 6a
r=rate(120.00,1179000.00,112.00)
#question 6b
future_value(120.00,145.00,r)

#question 7
rate(12385500.00,10305500.00,4)

#question 8a
future_value(2000.00,35.00,0.1)
#question 8b
future_value(2000.00,28.00,0.1)

#question 9
future_value(29000.00,8.00,0.05)

#question 10
print(time(8000.00,95000.00,0.12)+2)
