# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 06:36:46 2018

@author: cuity328
"""

import urllib2
import zipfile
url='https://www.sec.gov/files/dera/data/financial-statement-data-sets/2017q4.zip'
file=urllib2.urlopen(url)
data=file.read()
with open('findata.zip',"wb") as code:
    code.write(data)

zfile= zipfile.ZipFile('findata.zip')
zfile.extractall()

sub=open('sub.txt','r')
data=sub.read()
findata=data.split('\n')
finaldata=[]
for row in findata:
    f=row.split('\t')
    finaldata.append(f)

n=[]
for r in finaldata:
    if 'AMERICAN AIRLINES GROUP INC.' in r:
        n=r[0]
print n

num=open('num.txt','r')
data2=num.read()
findata2=data2.split('\n')
finaldata2=[]
for rows in findata2:
    m=rows.split('\t')
    finaldata2.append(m)
for v in finaldata2:
    if n in v:
        if 'SalesRevenueNet' in v:
            if v[4]=='20170930' and v[5]=='1':
                SalesRevenueNet=float(v[7])
                print v
        if 'CostsAndExpenses' in v:
            if v[4]=='20170930' and v[5]=='1':
                CostsAndExpenses=float(v[7])
                print v
        if 'InterestExpense'in v:
            if v[4]=='20170930' and v[5]=='1':
                InterestExpense=float(v[7])
                print v
        if 'NetIncomeLoss'in v:
            if v[4]=='20170930' and v[5]=='1':
                NetIncomeLoss=float(v[7])
                print v
if (NetIncomeLoss-(SalesRevenueNet-CostsAndExpenses-InterestExpense)*0.65)/NetIncomeLoss<= 0.05:
    print 'NetIncomeLoss~~(SalesRevenueNet-CostsAndExpenses-InterestExpense)'
else:
    print 'false'

tag=open('tag.txt','r')
data3=tag.read()
finddata3=data3.split('\n')
tagdata=[]
for rows in finddata3:
    m=rows.split('\t')
    tagdata.append(m)

#define a function to get all possible tags 
def searchtag(tagname):
    m=[]
    for row in tagdata:
        if tagname in row[0]:
            if row[0] not in m:
                m.append(row[0])
    return m
searchtag("NetIncome")
searchtag("Assets")
searchtag("RetainedEarning")
searchtag("LongTermDebt")
searchtag("CashDividend")
TAGs={'NetIncome': ('NetIncomeLoss', 'ProfitLoss','NetIncome','TotalNetIncome'),
    'Total Assets': ('Assets','SubtotalAssets'),
    'Fixed Assets': ('PropertyPlantAndEquipmentNet',),
    'Current Assets': ('AssetsCurrent', 'CurrentAssets'),
    'Current Liabilities': ('LiabilitiesCurrent',),
    'Depreciation': ('DepreciationDepletionAndAmortization',),
    'Cash Dividend': ('CommonStockDividendsPerShareDeclared','CashDividendsDeclaredAndPaid','CashDividendDeclared','CashDividendMember'),
    'Interest Expense': ('InterestExpense', 'InterestIncomeExpenseNet'),
    'Long Term Debt':('LongTermDebtNet','LongTermDebtCurrent', 'LongTermDebt')}

#create a dataframe contain name and cik
names=[]
cik=[]
adsh=[]
for row in finaldata:
    try:
        names.append(row[2])
        cik.append(row[1])
        adsh.append(row[0])
    except:
        break

import pandas as pd

name_cik=pd.DataFrame({'name':names,'cik':cik,'adsh':adsh})
name_cik

#another way to get the dataframe directely
sub = pd.read_csv('sub.txt', sep='\t', index_col='adsh')
num = pd.read_csv('num.txt', sep='\t')

#create a new vacant dataframe to store the ratios
column2017 = pd.DataFrame(index=sub.index, columns=TAGs)
column2016 = pd.DataFrame(index=sub.index, columns=TAGs)
#search the value from num
for key in TAGs:
    for tag in TAGs[key]:
        for index, row in num.loc[(num['tag'] == tag) & (num['ddate'] == 20170930)].iterrows():
                if pd.isnull(column2017.loc[row['adsh']][key]):
                    column2017.loc[row['adsh']][key] = row['value']

measure7=pd.merge(sub[['cik', 'name']], column2017, how='outer', left_index=True, right_index=True)

#get data for 2016
for key in TAGs:
    for tag in TAGs[key]:
        for index, row in num.loc[(num['tag'] == tag) & (num['ddate'] == 20160930)].iterrows():
                if pd.isnull(column2016.loc[row['adsh']][key]):
                    column2016.loc[row['adsh']][key] = row['value']
measure6=pd.merge(sub[['cik', 'name']], column2016, how='outer', left_index=True, right_index=True)

#calculate the ratios
ratios=pd.DataFrame({'cik':measure7['cik'],'name':measure7['name'],
                     'NetIncome':measure7['NetIncome'],
                     'Retained Earning':measure7['NetIncome']-measure7['Cash Dividend'],
                     'Net Capital Spending':measure6['Fixed Assets']-measure7['Fixed Assets']+measure7['Depreciation'],
                     'Change in Net Working Capital':measure7['Current Assets']-measure7['Current Liabilities']
                     -measure6['Current Assets']+measure6['Current Liabilities'],
                     'Cash Flow To Creditors':measure7['Interest Expense']-measure7['Long Term Debt']+measure6['Long Term Debt']})
ratios.to_csv("SEC Ratio Analysis.csv",index=True,sep=',')


#generate data for report
searchtag("Operating")
searchtag("OperatingCash")
searchtag('Inventory')
TAGS={'Revenue': ('SalesRevenueServicesNet', 'SalesRevenueNet','NoninterestIncome','Revenues'),
      'NetIncome': ('NetIncomeLoss', 'ProfitLoss','NetIncome','TotalNetIncome'),
      'Operating Profit': ('OperatingIncomeLoss','OperatingIncome','OperatingGainLosses'),
      'Current Assets': ('Assets','AssetsCurrent', 'CurrentAssets'),
      'Operating Cash Flow': ('OutflowInflowDepositsOperatingCashFlows','OperatingCashFlowsDirectMethodAbstract',
      'NetCashProvidedByUsedInOperatingActivitiesContinuingOperation'),
      'Inventory': ('InventoryAdjustment','InventoryTotal','NetInventory')}
report2016 = pd.DataFrame(index=sub.index, columns=TAGS)
report2017 = pd.DataFrame(index=sub.index, columns=TAGS)
for key in TAGS:
    for tag in TAGS[key]:
        for index, row in num.loc[(num['tag'] == tag) & (num['ddate'] == 20160930)].iterrows():
                if pd.isnull(report2016.loc[row['adsh']][key]):
                    report2016.loc[row['adsh']][key] = tag,'|20160930|',row['value']
report2016.to_csv("report2016.csv",index=True,sep=',')
for key in TAGS:
    for tag in TAGS[key]:
        for index, row in num.loc[(num['tag'] == tag) & (num['ddate'] == 20170930)].iterrows():
                if pd.isnull(report2017.loc[row['adsh']][key]):
                    report2017.loc[row['adsh']][key] = tag,'|20170930|',row['value']
report2017.to_csv("report2017.csv",index=True,sep=',')