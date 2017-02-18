import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#import scipy
#import pandas as pd
import quandl as qn
#import csv

mydata_cl=qn.get("CHRIS/CME_CL2.6",start_date="2017-01-03", end_date="2017-02-03", transformation='diff') #gives you pandas dataframe directly
mydata_s=qn.get("CHRIS/CME_S2.6",start_date="2017-01-03", end_date="2017-02-03", transformation='diff')
mydata_gc=qn.get("CHRIS/CME_GC2.6",start_date="2017-01-03", end_date="2017-02-03", transformation='diff')

#print(np.log(mydata_cl.Settle+1+np.max(np.abs(mydata_cl.Settle))))
#print(mydata_cl.Settle)

#print (mydata_cl.Settle.shift(-1))
#print (np.log(mydata_cl.Settle.shift(-1) - mydata_cl.Settle))

mydata_cl.to_csv('cl2.csv')
mydata_s.to_csv('s2.csv')
mydata_gc.to_csv('gc2.csv')
fig1 = plt.figure(1)
sns.kdeplot(np.log(mydata_cl.Settle+1+np.max(np.abs(mydata_cl.Settle))))
#sns.kdeplot(np.log(mydata_cl.Settle+1))
#sns.distplot((mydata_cl), bins=5)
plt.title('Crude Oil')
fig2 = plt.figure(2)
sns.kdeplot(np.log(mydata_s.Settle+1+np.max(np.abs(mydata_s.Settle))))
#sns.kdeplot(np.log(mydata_s.Settle+1))
#sns.distplot(mydata_s, bins=5)
plt.title('Soy Beans')
fig3 = plt.figure(3)
sns.kdeplot(np.log(mydata_gc.Settle+1+np.max(np.abs(mydata_gc.Settle))))
#sns.kdeplot(np.log(mydata_gc.Settle+1))
#sns.distplot(mydata_gc, bins=5)
plt.title('Gold')
plt.show()