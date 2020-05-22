import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data to plot
d = pd.read_csv(r"../allResults.csv")
df=pd.DataFrame(d)
imageID=[]
before=[]
afterUpdate=[]
afterMinification=[]
afterUpdateANDminify=[]
for idx,row in df.iterrows():
    imageID.append(row[0])
    before.append(row[1])
    afterUpdate.append(row[2])
    afterMinification.append(row[3])
    afterUpdateANDminify.append(row[4])


n_groups = len(imageID)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.20
opacity = 0.7

rects1 = plt.bar(index, before, bar_width,
alpha=opacity,
color='b',
label='Originally')

rects2 = plt.bar(index + bar_width, afterUpdate, bar_width,
alpha=opacity,
color='g',
label='After Update')

rects3 = plt.bar(index + 2*bar_width, afterMinification, bar_width,
alpha=opacity,
color='r',
label='After Minification')

rects4 = plt.bar(index + 3*bar_width, afterUpdateANDminify, bar_width,
alpha=opacity,
color='c',
label='After update and minification')

plt.xlabel('Images', fontsize=15,fontweight='bold')
plt.ylabel('#Vulnerabilities',fontsize=15, fontweight='bold')
#plt.title('Vulnerabilities by experiments')
plt.xticks(index + bar_width, imageID)
plt.legend()

plt.tight_layout()
plt.show()
