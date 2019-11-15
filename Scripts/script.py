#!/usr/bin/env python3

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
#tips = sns.load_dataset("tips")
df = pd.read_csv(r"../train.csv")
df.head()
#p1=sns.regplot(data=df, x="OS_Packages", y="Vulnerabilities",fit_reg=False,marker="o", color="skyblue", scatter_kws={'s':800})
#sns.palplot(
#colors=sns.color_palette("Blues")
colors = {'ubuntu:14.04' : '#2E37FE', 'ubuntu:16.04' : '#CAE1FF', 'ubuntu:17.04':'#5190ED','ubuntu:17.10':'#104E8B','ubuntu:18.04' : '#98F5FF','centos 6':'#800080','centos 7':'#b19cd9',
        'alpine:3.7.1':'#ff4c4c','alpine:3.8.4':'#ff0000','alpine:3.9.0':'#990000','debian:8':'#3CB371'}
with sns.plotting_context(rc={"legend.fontsize":25}):
  p1=sns.relplot(x="Packages",y="Vulnerabilities",hue="OS distribution",size="CRITICAL Vulnerabilities",sizes=(100,1500), data = df,palette=colors)
#p1=p1.palplot(sns.color_palette(flatui))
#ax = sns.scatterplot(df.OS_Packages, df.Vulnerabilities,hue=df.names, alpha = 1.0,s = df.High_Vulnerabilities,sizes=(200,700))
# Show the plot
#for line in range(0,df.shape[0]):
#     ax.text(df.OS_Packages[line]+0.2, df.Vulnerabilities[line], df.names[line], horizontalalignment='center', size='small', color='black', weight='normal')
#p1.set(xlim(0,1500))
#p1.set(xlim=0,1500)
#p1 = (p1.set_axis_labels("Tip","Total bill(USD)").
  p1.set(xlim=(0,None))
p1.set(xlabel='#Packages', ylabel='#Vulnerabilities by Anchore')
#p1.set(title="#Packages Vs #Vulnerabilities")
#p1._legend.set_title("High Vulnerabilties")
#subtitle_legend(p1, legend_format=legend_format)
ax = p1.axes[0,0]
for idx,row in df.iterrows():
    x = row[3]
    y = row[2]
    text = row[6]
    ax.text(x+.05,y,text, horizontalalignment='left')
plt.show()
