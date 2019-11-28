#!/usr/bin/env python3

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
d = pd.read_csv(r"../train.csv")
d.head()
df=pd.DataFrame(d)
#p1=sns.regplot(data=df, x="OS_Packages", y="Vulnerabilities",fit_reg=False,marker="o", color="skyblue", scatter_kws={'s':800})
#sns.palplot(
#colors=sns.color_palette("Blues")
colors = {'ubuntu:14.04' : '#2E37FE', 'ubuntu:16.04' : '#CAE1FF', 'ubuntu:17.04':'#5190ED','ubuntu:17.10':'#000085','ubuntu:18.04' : '#98F5FF','centos 6':'#800080','centos 7':'#b19cd9',
        'alpine:3.7.1':'#3CB371','alpine:3.8.4':'#00ff00','alpine:3.9.0':'#006400','debian:8':'#ffa500'}
markers = {"ubuntu:14.04": "s", "ubuntu:16.04": "s",'ubuntu:17.04':'s','ubuntu:17.10':'s','ubuntu:18.04' : 's','centos 6':'X','centos 7':'X',
        "alpine:3.7.1":'o','alpine:3.8.4':"o","alpine:3.9.0":"o","debian:8":"D"}
with sns.plotting_context(rc={"legend.fontsize":25,"font.size":18,"axes.titlesize":20}):
 # plt.ylim(0,1500)
  p1=sns.relplot(x="Packages",y="Vulnerabilities",hue="OS distribution",size="CRITICAL Vulnerabilities",sizes=(20,2000),data = df,palette=colors,markers=markers,style="OS distribution",height=10, aspect=2)
#p1.set(xlim(0,1500))
#p1.set(xlim=0,1500)
#p1.set(xlim=(0,1500))
  #p1.set(xticks(range(1,916)))
p1.set(xlabel='#Packages', ylabel='#Vulnerabilities by Anchore')
p1.set(xticks=[i for i in range(0, max(df['Packages']) + 10, 50)],
       yticks=[i for i in range(0, max(df['Vulnerabilities']) + 20, 250)])
ax = p1.axes[0,0]
leg = p1._legend
leg.set_bbox_to_anchor([1, 0])  # coordinates of lower left of bounding box
leg._loc = 4  # if required you can set the loc
leg.texts[12].set_text("CRITICAL \nVulnerabilities")
for idx,row in df.iterrows():
    x = row[3]
    y = row[2]
    text = row[5]
    alignment=row[8]
    v=row[9]
    rot=row[10]
    #ax.set_xlim([0, 900])
    ax.text(x+.05,y,text,fontsize=13, horizontalalignment=alignment,verticalalignment=v,rotation=rot)
#plt.ylim(0,1500)

plt.show()
