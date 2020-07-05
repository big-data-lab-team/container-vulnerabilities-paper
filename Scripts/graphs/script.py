#!/usr/bin/env python3

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats as st
# Load the data
d = pd.read_csv(r"../../train3.csv")
d.head()
df=pd.DataFrame(d)
plt.figure(figsize=(200,20))
plt.rcParams["axes.labelweight"] = "bold"
b, a = np.polyfit(df['Packages'], df['Vulnerabilities'], 1)
xtest = np.linspace(df['Packages'].min(),df['Vulnerabilities'].max(),10)
colors = {'ubuntu:14.04' : '#2E37FE', 'ubuntu:16.04' : '#CAE1FF', 'ubuntu:17.04':'#5190ED','ubuntu:17.10':'#000085','ubuntu:18.04' : '#98F5FF','centos 6':'#800080','centos 7':'#b19cd9',
        'alpine:3.7.1':'#3CB371','alpine:3.8.4':'#00ff00','alpine:3.9.0':'#006400','debian:8':'#ffa500'}
markers = {"ubuntu:14.04": "o", "ubuntu:16.04": "o",'ubuntu:17.04':'o','ubuntu:17.10':'o','ubuntu:18.04' : 'o','centos 6':'o','centos 7':'o',
        "alpine:3.7.1":'o','alpine:3.8.4':"o","alpine:3.9.0":"o","debian:8":"o"}
marker_order=["ubuntu:14.04", "ubuntu:16.04",'ubuntu:17.04','ubuntu:17.10','ubuntu:18.04','centos 6','centos 7',
        "alpine:3.7.1",'alpine:3.8.4',"alpine:3.9.0","debian:8"]
with sns.plotting_context(rc={"legend.fontsize":25,"legend.markersize":18,"axes.titlesize":20,"font.weight":'heavy',"legend.labelspacing":20}):
  p1=sns.relplot(x="Packages",y="Vulnerabilities",hue="OS distribution",hue_order=marker_order,size="CRITICAL Vulnerabilities",sizes=(300,1450),data = df,palette=colors,markers=markers,style="OS distribution",height=10, aspect=2)
p1.set(xlabel='#Packages', ylabel='#Vulnerabilities')
p1.set(xticks=[i for i in range(0, max(df['Packages']) + 100, 50)],
       yticks=[i for i in range(0, max(df['Vulnerabilities']) + 20, 250)])
ax = p1.axes[0,0]
#ax.plot(xtest, a + b* xtest, '--')
leg = p1._legend
#lgnd = plt.legend(loc="right", numpoints=1, fontsize=20)
for i in range(1,12):
    leg.legendHandles[i]._sizes = [500]  # you can change this for suitable size

#p1.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
leg.set_bbox_to_anchor([1.01, 0.04])
leg._loc = 4
#leg.markerscale=2
leg.texts[12].set_text("HIGH \nVulnerabilities")

#leg(markerscale=6)
#z = np.polyfit(df['Packages'], df['Vulnerabilities'], 1)
#p = np.poly1d(z)
#plt.plot(df['Packages'],p(df['Packages']),"k--")
#leg._labelspacing=10
#sns.regplot(x="Packages", y="Vulnerabilities", data=df)
slope, intercept, r_value, p_value, std_err = st.linregress(df['Packages'],df['Vulnerabilities'])
line_df = pd.DataFrame()
line_df['line'] = slope*df['Packages']+intercept
print(std_err)
plt.plot(df['Packages'], line_df['line'],"k-",label='y=({:.2f})x+({:.2f})'.format(slope,intercept))
#plt.legend()
for idx,row in line_df.iterrows():
    l = row[0]
    ax.text(700,1050,'y=({:.2f})x+({:.2f})'.format(slope,intercept),weight='bold')
for idx,row in df.iterrows():
    x = row[3]
    y = row[2]
    text = row[6]
    alignment=row[8]
    v=row[9]
    rot=row[10]
    hoz=row[11]
    ver=row[12]
    ax.text(x+hoz,y+ver,text,fontsize=15, horizontalalignment=alignment,verticalalignment=v,rotation=rot,weight='bold')
#plt.legend(labelspacing=20)
plt.savefig('vuln_graph.pdf')
