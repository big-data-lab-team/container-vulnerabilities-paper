#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
d = pd.read_csv(r"../Results_with_deleted_number_of_packages.csv")
df=pd.DataFrame(d)
packages=[]
diff=[]
for idx,row in df.iterrows():
    packages.append(row[0])
    diff.append(row[1])
fig=plt.figure()
#ax = fig.add_subplot()
plt.plot([],[])
#print(packages)
#ax=fig.add_axes([0,0,1,1])
plt.figure(figsize=(20,10))
p1=plt.scatter(packages, diff, color='r',s=150,marker='o',label='Reduced vulnerabilities after minification')
z = np.polyfit(packages, diff,1)
p = np.poly1d(z)
plt.plot(packages,p(packages),"r--")
plt.xlabel('#Deleted Packages', fontsize=15)
plt.ylabel('#Reduced Vulnerabilities',fontsize=15)
plt.legend(loc='upper left', bbox_to_anchor=(1.00, 1.00), shadow=True, ncol=1,labelspacing=1.2,borderpad=1.0)
#plt.show()
plt.savefig('graphwithdeletedpackages.pdf',bbox_inches='tight')
