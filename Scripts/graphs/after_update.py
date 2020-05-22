#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
d = pd.read_csv(r"../Results_after_update2.csv")
df=pd.DataFrame(d)
packages=[]
before=[]
after=[]
for idx,row in df.iterrows():
    packages.append(row[0])
    before.append(row[1])
    after.append(row[2])
fig=plt.figure()
#ax = fig.add_subplot()
plt.plot([],[])
#print(packages)
#ax=fig.add_axes([0,0,1,1])
plt.figure(figsize=(20,10))
p1=plt.scatter(packages, before, color='r',s=150,marker='o',label='Before Update')
p2=plt.scatter(packages, after, color='b',s=150,marker='D',label='After Update')
z = np.polyfit(packages, before,1)
p = np.poly1d(z)
plt.plot(packages,p(packages),"r--")
y = np.polyfit(packages, after, 1)
p3 = np.poly1d(y)
plt.plot(packages,p3(packages),"b--")
plt.xlabel('#Packages', fontsize=15)
plt.ylabel('#Vulnerabilities',fontsize=15)
plt.legend(loc='upper left', bbox_to_anchor=(1.00, 1.00), shadow=True, ncol=1,labelspacing=1.2,borderpad=1.0)
#plt.show()
plt.savefig('afterupdatewithpackage.pdf',bbox_inches='tight')
