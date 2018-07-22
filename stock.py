# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 00:58:16 2018

@author: cuity328
"""

#question 1
dividend=1.32
g=0.06  
r=0.1
current_price=dividend*(1+g)/(r-g)
print 'Q1(a): current price is: %.2f' %current_price
typ=dividend*(1+g)**11/(r-g)
print 'Q1(b): the price in 10 years will be: %.2f'%typ

#question 2
dividend=4.55
g=0.03
cv=40
r=dividend/cv+g
print 'Q2: required return is: %.2f%%' %(r*100)

#question 3
dividend=4.9
g=0.043
r=0.079
cv=dividend/(r-g)
print 'Q3: current price id :%.2f' %cv

#question 4
cv=90
r=0.1
g=0.05
dividend=cv*(r-g)
print 'Q4: current dividend per share is : %.2f' %dividend

#question 5
divident=25
r=0.1
cv=dividend*(1-1/(1+r)**7)/r
print 'Q5: current price is : %.2f'%cv

#question 6
dividend=1.40
g=0.06
r1=0.089
r2=0.119
r3=0.153
cv1=dividend/(r1-g)
cv2=dividend/(r2-g)
cv3=dividend/(r3-g)
print 'Q6(a): stock price for Red Inc is: %.2f'%cv1
print 'Q6(b): stock price for Yellow Corp is: %.2f'%cv2
print 'Q6(c): stock price for Blue company is: %.2f'%cv3

#question 7
dividend=11
r=0.12
g=0.04
cv=dividend/(r-g)/(1+r)**15
print 'Q7: current share price is:%.2f'%cv

#question 8
dividend1=13
dividend2=11    
dividend3=9
dividend=5
r=0.17
g=0.08
cv=dividend1/(1+r)+dividend2/(1+r)**2+dividend3/(1+r)**3+dividend/(r-g)/(1+r)**3
print 'Q8: current share price is： %.2f'%cv

#question 9
dividend=1.6
g1=0.18
g2=0.04
r=0.07
cv=dividend*(1+g1)*(1-((1+g1)/(1+r))**3)/(r-g1)+dividend*(1+g1)**3*(1+g2)/(r-g2)/(1+r)**3
print 'Q9: current sare price is: %.2f'%cv

#question 10
dividend=18
g=-0.12
r=0.19
cv=dividend*(1+g)/(r-g)
print 'Q10: pay: %.2f for each share' %cv

#question 11
cv=75
r=0.11
g=0.05
dividend=cv*(r-g)
print 'Q11: most recent divident paid is: %.2f'%(dividend/(1+g))

#question 12
g=0
dividend=14
r=0.07
cv=dividend/(r-g)/(1+r)**5
print 'Q12: cost: %.2f per share'%cv

#question 13
dividend=1.3
g1=0.35
g2=0.05
r-0.14
cv=dividend*(1+g1)*(1-((1+g1)/(1+r))**9)/(r-g1)+dividend*(1+g1)**9*(1+g2)/(r-g2)/(1+r)**9
print 'Q13: price of stock today is: %.2f'%cv