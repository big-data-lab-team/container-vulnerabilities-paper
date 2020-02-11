#!/usr/bin/env python3

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
d = pd.read_csv(r"../train.csv")
d.head()
df=pd.DataFrame(d)
colors = {'ubuntu:14.04' : '#2E37FE', 'ubuntu:16.04' : '#CAE1FF', 'ubuntu:17.04':'#5190ED','ubuntu:17.10':'#000085','ubuntu:18.04' : '#98F5FF','centos 6':'#800080','centos 7':'#b19cd9',
        'alpine:3.7.1':'#3CB371','alpine:3.8.4':'#00ff00','alpine:3.9.0':'#006400','debian:8':'#ffa500'}
markers = {"ubuntu:14.04": "o", "ubuntu:16.04": "o",'ubuntu:17.04':'o','ubuntu:17.10':'o','ubuntu:18.04' : 'o','centos 6':'o','centos 7':'o',
        "alpine:3.7.1":'o','alpine:3.8.4':"o","alpine:3.9.0":"o","debian:8":"o"}
with sns.plotting_context(rc={"legend.fontsize":25,"font.size":18,"axes.titlesize":20,"font.weight":'heavy',"legend.labelspacing":20}):
  p1=sns.relplot(x="Packages",y="Vulnerabilities",hue="OS distribution",size="CRITICAL Vulnerabilities",sizes=(1000,4000),data = df,palette=colors,markers=markers,style="OS distribution",height=10, aspect=2)
p1.set(xlabel='#Packages', ylabel='#Vulnerabilities')
p1.set(xticks=[i for i in range(0, max(df['Packages']) + 100, 50)],
       yticks=[i for i in range(0, max(df['Vulnerabilities']) + 20, 250)])
ax = p1.axes[0,0]
leg = p1._legend
#p1.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
leg.set_bbox_to_anchor([1.01, 0.04])
leg._loc = 4
leg.texts[12].set_text("CRITICAL \nVulnerabilities")
leg._labelspacing=50
for idx,row in df.iterrows():
    x = row[3]
    y = row[2]
    text = row[6]
    alignment=row[8]
    v=row[9]
    rot=row[10]
    hoz=row[11]
    ver=row[12]
    ax.text(x+hoz,y+ver,text,fontsize=30, horizontalalignment=alignment,verticalalignment=v,rotation=rot,weight='bold')
#plt.legend(labelspacing=20)
plt.show()
