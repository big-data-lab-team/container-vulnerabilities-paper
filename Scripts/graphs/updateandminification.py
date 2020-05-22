#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
d = pd.read_csv(r"../updateandminification.csv")
df=pd.DataFrame(d)
packages=[]
before=[]
update=[]
delete=[]
for idx,row in df.iterrows():
    packages.append(row[0])
    before.append(row[1])
    update.append(row[2])
    delete.append(row[3])
fig=plt.figure()
#ax = fig.add_subplot()
plt.plot([],[])
#print(packages)
#ax=fig.add_axes([0,0,1,1])
plt.figure(figsize=(20,10))
p1=plt.scatter(packages, before, color='r',s=150,marker='o',label='Before')
p2=plt.scatter(packages, update, color='b',s=150,marker='D',label='After Update')
p3=plt.scatter(packages,delete, color='g',s=150,marker='*',label='After Minification')
z = np.polyfit(packages, before,1)
p = np.poly1d(z)
plt.plot(packages,p(packages),"r--")
y = np.polyfit(packages, update, 1)
p4 = np.poly1d(y)
plt.plot(packages,p4(packages),"b--")
x = np.polyfit(packages, delete,1)
p5 = np.poly1d(x)
plt.plot(packages,p5(packages),"g--")
plt.xlabel('#Packages', fontsize=15)
plt.ylabel('#Vulnerabilities',fontsize=15)
plt.legend(loc='upper left', bbox_to_anchor=(1.00, 1.00), shadow=True, ncol=1,labelspacing=1.2,borderpad=1.0)
#plt.show()
plt.savefig('updateandminification.pdf',bbox_inches='tight')
