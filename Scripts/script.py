#!/usr/bin/env python3

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
#tips = sns.load_dataset("tips")
df = pd.read_csv(r"train.csv")
df.head()
#p1=sns.regplot(data=df, x="OS_Packages", y="Vulnerabilities",fit_reg=False,marker="o", color="skyblue", scatter_kws={'s':800})
p1=sns.relplot(x="Packages",y="Vulnerabilities",hue="OS",size="High",sizes=(600,1500), data = df)
#ax = sns.scatterplot(df.OS_Packages, df.Vulnerabilities,hue=df.names, alpha = 1.0,s = df.High_Vulnerabilities,sizes=(200,700))
# Show the plot
#for line in range(0,df.shape[0]):
#     ax.text(df.OS_Packages[line]+0.2, df.Vulnerabilities[line], df.names[line], horizontalalignment='center', size='small', color='black', weight='normal')
p1.set(xlabel='#Packages', ylabel='#Vulnerabilities by Anchore')
p1.set(title="#Packages Vs #Vulnerabilities")
ax = p1.axes[0,0]
for idx,row in df.iterrows():
    x = row[3]
    y = row[2]
    text = row[5]
    ax.text(x+.05,y,text, horizontalalignment='left')
plt.show()
