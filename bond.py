# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:39:15 2018

@author: cuity328
"""

#question 1
t=14
g=0.06                         #coupon rate
r=0.1                          #yield to maturity
par=1000.00
pv=par*g*(1-(1+r)**-t)/r+par*(1+r)**-t
print 'Q1: current bond price is: %.2f' %pv

#question 2
t=14
g=0.09
pv=850.46                      #current bond price
par=1000
low=0
high=1
r=0.5
while abs(pv-par*g*(1-(1+r)**-t)/r+par*(1+r)**-t)>0.001:
    if pv>par*g*(1-(1+r)**-t)/r+par*(1+r)**-t:
        high=r
        r=(low+high)/2
    elif pv<par*g*(1-(1+r)**-t)/r+par*(1+r)**-t:
        low=r
        r=(low+high)/2
    else:
        break
print 'Q2： YTM is: %.2f%%' %(r*100)

#question 3
t=6
pv=970
r=0.099
par=1000
g=(pv-par*(1+r)**-t)/(par*(1-(1+r)**-t)/r)   #coupon rate of bond
print 'Q3: coupon rate must be :%.2f%%' %(g*100)

#question 4
t=17
g=0.094
pv=1.02                      #current bond price is 1.02 times par value and we assume par value is 1
par=1
low=0
high=1
r=0.5
while abs(pv-par*g/2*(1-(1+r/2)**(-2*t))/(r/2)+par*(1+r/2)**(-2*t))>0.001:
    if pv>par*g/2*(1-(1+r/2)**(-2*t))/(r/2)+par*(1+r/2)**(-2*t):
        high=r
        r=(low+high)/2
    elif pv<par*g/2*(1-(1+r/2)**(-2*t))/(r/2)+par*(1+r/2)**(-2*t):
        low=r
        r=(low+high)/2
    else:
        break
print 'Q4： YTM is: %.2f%%' %(r*100)

#question 5
rr=0.055      #real rate
ir=0.02       #inflation rate
nr=(1+rr)*(1+ir)-1     #nominal return rate
print 'Q5： you would see: %.2f%% on a treasury bill' %(nr*100)

#question 6
tr=0.095      #total return rate
ir=0.05       #inflation rate
rr=(1+tr)/(1+ir)-1     #real rate
print 'Q5： your real return is: %.2f%%' %(rr*100)

#question 7
def price_change(rate_change,g):    #g:coupon bond rate
    r=0.07                        #origianl rate
    t=7
    par=1 
    pv=par*g/2*(1-(1+r/2)**(-2*t))/(r/2)+par*(1+r/2)**(-2*t)
    rnew=r+rate_change
    pvnew=par*g/2*(1-(1+rnew/2)**(-2*t))/(rnew/2)+par*(1+rnew/2)**(-2*t)
    pricechange=(pvnew-pv)/pv
    return pricechange
print 'Q7(a): price of bond J will change by %.2f%%'%(price_change(0.02,0.05)*100)
print 'Q7(b): price of bond k will change by %.2f%%'%(price_change(0.02,0.11)*100)
print 'Q7(c): price of bond J will change by %.2f%%'%(price_change(-0.02,0.05)*100)
print 'Q7(d): price of bond k will change by %.2f%%'%(price_change(-0.02,0.11)*100)

#question 8
t=11
g=0.104
pv=1013.04                  
par=1000
low=0                  #then we solve the ytm
high=1
r=0.5
while abs(pv-par*g/2*(1-(1+r/2)**(-2*t))/(r/2)+par*(1+r/2)**(-2*t))>0.001:
    if pv>par*g/2*(1-(1+r/2)**(-2*t))/(r/2)+par*(1+r/2)**(-2*t):
        high=r
        r=(low+high)/2
    elif pv<par*g/2*(1-(1+r/2)**(-2*t))/(r/2)+par*(1+r/2)**(-2*t):
        low=r
        r=(low+high)/2
    else:
        break
gnew=r             #coupon rate should equals to ytm when the bond sell at par
print 'Q8： coupon rate hould be: %.2f%%' %(gnew*100)

#question 9
cp=1180.00           #clean price
g=0.076
ip=cp+g/2*1000*4/6   #full price=clean price+accrued interest
print 'Q9: invoice price is: %.2f'%ip

#question 10
r=0.114
g=0.036            #price increas rate
pv=5*((1+g)/(1+r))**(1./52)*(1-((1+g)/(1+r))**32)/(1-(1+g)**(1./52)/(1+r)**(1./52))
print 'Q10: present value of commitment is: %.2f'%pv


