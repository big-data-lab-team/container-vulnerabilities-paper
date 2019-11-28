#!/usr/bin/env python3

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

d = {'x-axis':[100,915,298,299], 'y-axis': [1515,1450,1313,1315],
     'text':['point1','point2','point3','point4']}
df = pd.DataFrame(d)

p1 = sns.relplot(x='x-axis', y='y-axis',data=df )
ax = p1.axes[0,0]
for idx,row in df.iterrows():
    x = row[0]
    y = row[1]
    text = row[2]
    ax.text(x+.05,y,text, horizontalalignment='left')

p1.set(xticks=[i for i in range(0, max(df['x-axis']) + 50, 50)],
       yticks=[i for i in range(0, max(df['y-axis']) + 500, 500)])


plt.show()
