# -*- coding: utf-8 -*-


#question 1
def annual_cf(pv,r,k,T):
    x=float(pv*r/k/(1-1/(1+r/k)**(T*k)))
    return x
print 'annual cash flow is:',annual_cf(31000.00,0.0625,1,14)

#question 2
pv=61000.00
x=1200.00        #payment per time
k=12             #k period per year
r=float(x*k/pv)  #the formula as t equal to infinite
print 'the rate should be:',r

#question 3
k=4     #return per quarter
T=6
r=3**(1./(T*k))-1
print 'return per quarter is:',r  

#question 4
def present_value(x,k,r,T):
    pv=x*k/r*(1-(1/(1+r/k)**(k*T)))
    return pv
print 'present value of winnings is:', present_value(540000.00/1.05,1,(1.1/1.05-1),16)

#question 5
import math
def time(fv,x,r,k):
    T=(math.log((fv*r/k/x+(1+r/k)),(1+r/k))-1)/k
    return T
print 'we have to make',time(25964.00,380.00,0.08,12)*12,'times payment'       #12 payments per year

#question 6
x=annual_cf(230000.00,0.076,12,30)      #He miss x-800 per payment
pv=present_value((x-800),12,0.076,30)
fv=pv*(1+0.076/12)**360
print 'ballon payment would be:',fv

#question 7
r=0.5 
low=0.0  
up=1.0  
while abs(0.8*2800000-present_value(17000.00,12,r,30))>0.001:          
    n=0.8*2800000-present_value(17000.00,12,r,30)
    if (n>0):  
        up=r  
        r=low+(r-low)/2  
    else:  
        low=r  
        r=up-(up-r)/2  
print 'APR on this loan is:',r 
print 'EAR on this loan is:',(1+r/12)**12-1
  

#question 8
pv_1=present_value(1700.00,12,0.1,16)     #present value of a 16year annuity with 10% interest rate
pv_2=present_value(1700.00,12,0.1,6)      #present value of a 6year annuity with 10% interest rate
pv_3=present_value(1700.00,12,0.13,6)      #present value of a 6year annuity with 13% interest rate
pv=pv_3+pv_1-pv_2
print 'present value of annuity is',pv

#question 9
x=annual_cf(43000.00,0.0825,12,5)
print 'monthly payment is:',x

#question 10
pv=5000.00*0.97
fv=5500.00
r=fv/pv-1
print 'actual rate is:',r


