#!/usr/bin/env python3

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# Load the data
d = pd.read_csv(r"../train3.csv")
d.head()
df=pd.DataFrame(d)
plt.figure(figsize=(200,20))
plt.rcParams["axes.labelweight"] = "bold"
colors = {'ubuntu:14.04' : '#2E37FE', 'ubuntu:16.04' : '#CAE1FF', 'ubuntu:17.04':'#5190ED','ubuntu:17.10':'#000085','ubuntu:18.04' : '#98F5FF','centos 6':'#800080','centos 7':'#b19cd9',
        'alpine:3.7.1':'#3CB371','alpine:3.8.4':'#00ff00','alpine:3.9.0':'#006400','debian:8':'#ffa500'}
markers = {"ubuntu:14.04": "o", "ubuntu:16.04": "o",'ubuntu:17.04':'o','ubuntu:17.10':'o','ubuntu:18.04' : 'o','centos 6':'o','centos 7':'o',
        "alpine:3.7.1":'o','alpine:3.8.4':"o","alpine:3.9.0":"o","debian:8":"o"}
p1=sns.relplot(x="Packages",y="Vulnerabilities",hue="OS distribution",size="CRITICAL Vulnerabilities",sizes=(300,1450),data = df,palette=colors,markers=markers,style="OS distribution",height=10, aspect=2,legend=False)
p1.set(xlabel='#Packages', ylabel='#Vulnerabilities')
p1.set(xticks=[i for i in range(0, max(df['Packages']) + 100, 50)],
       yticks=[i for i in range(0, max(df['Vulnerabilities']) + 20, 250)])
ax = p1.axes[0,0]
#leg = p1._legend
#p1.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
#leg.set_bbox_to_anchor([1.01, 0.04])
#leg._loc = 4
#leg.texts[12].set_text("CRITICAL \nVulnerabilities")
#leg.remove()
z = np.polyfit(df['Packages'], df['Vulnerabilities'], 1)
p = np.poly1d(z)
plt.plot(df['Packages'],p(df['Packages']),"k--")



d = pd.read_csv(r"../Results_after_update2.csv")
df=pd.DataFrame(d)
packages=[]
#before=[]
after=[]
for idx,row in df.iterrows():
    packages.append(row[0])
    #before.append(row[1])
    after.append(row[2])
plt.plot([],[])
p2=plt.scatter(packages, after, color='r',s=150,marker='2',label='Vulnerabilities after update')
y = np.polyfit(packages, after, 1)
p3 = np.poly1d(y)
plt.plot(packages,p3(packages),"r--")
plt.legend(loc='upper left', shadow=True, ncol=2,labelspacing=1.2,borderpad=1.0,prop={'size': 14})
#leg.remove()

#leg._labelspacing=10
#for idx,row in df.iterrows():
#    x = row[3]
#    y = row[2]
#    text = row[6]
#    alignment=row[8]
#    v=row[9]
#    rot=row[10]
#    hoz=row[11]
#    ver=row[12]
#    ax.text(x+hoz,y+ver,text,fontsize=15, horizontalalignment=alignment,verticalalignment=v,rotation=rot,weight='bold')
#plt.legend(labelspacing=20)
plt.savefig('test.pdf')
