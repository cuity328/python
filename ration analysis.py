# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:28:02 2018

@author: cuity328
"""
##first question
sales=534000
cost=295000
depreexpense=41000
interestexpense=34000
taxrate=0.35
netcome=(sales-cost-depreexpense-interestexpense)*(1-taxrate)
print"Netincome:%.2f" %netcome

##second question
sales=684000
cost=255000
depreexpense=52000
interestexpense=33000
taxrate=0.35
cashdiv=72000
rearnings=(sales-cost-depreexpense-interestexpense)*(1-taxrate)-cashdiv
print "retained earnings:%.2f" %rearnings
 
##third question
Beginningnetfixedassets=4200000
Endingnetfixedassets=6500000
Depreciation=955000
Netcapitalspending=Endingnetfixedassets-Beginningnetfixedassets+Depreciation
print "Net capital spending:%.2f" %Netcapitalspending

##4th question
beginasset=1240
beginliability=820
endasset=1660    
endliability=1180
changeNWC=(endasset-endliability)-(beginasset-beginliability)
print "change in NWC:%.2f" %changeNWC

##5th question
begindebt=2600000
newdebt=3900000
Netnewborrowing=newdebt-begindebt
interestexpense=270000
cftc=interestexpense-Netnewborrowing 
print "Cash flow to creditors:%.2f" %cftc

##6th question
beginaccount1=930000
beginaccount2=6600000
endaccount1=955000
endaccount2=8650000
divpaid=530000
cfts=divpaid-(endaccount1+endaccount2-beginaccount1-beginaccount2)
print"Cash flow to stockholders:%.2f" %cfts

#7th question
begindebt=2700000
newdebt=4250000
Netnewborrowing=newdebt-begindebt
interestexpense=180000
cftc=interestexpense-Netnewborrowing 
beginaccount1=730000
beginaccount2=6050000
endaccount1=955000
endaccount2=8650000
divpaid=650000
cfts=divpaid-(endaccount1+endaccount2-beginaccount1-beginaccount2)
ChangeNWC=-165000
Netcapitalspending=860000
ocf=cfts+ cftc+ Netcapitalspending+ ChangeNWC
print"Operating cash flow:%.2f" %ocf

#8th question
cash=390000
PandC=690000
apayable=340000
areceivable=139000
fixedasset=4700000
inventory=205000
notepayable=170000
arearnings=1335000
debt=1830000
CS=cash+PandC+areceivable+fixedasset+inventory-apayable-notepayable-arearnings-debt
print"Common stock:%.2f" %CS
