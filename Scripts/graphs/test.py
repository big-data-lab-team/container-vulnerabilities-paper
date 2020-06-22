#from matplotlib import pyplot as plt
#import pandas as pd
#import seaborn as sns
#import numpy as np
#
#d = {'x-axis':[71,35,61,253,145,157,218,241,291,277,159,167,171,188,240,254,258,269,277,288,298,347,349,353,360,380,441,443,506,528,530,537,538,566,600,762,815,889], 
#        'y-axis': [5,5,15,79,75,641,172,867,289,67,75,112,46,150,70,70,897,391,671,54,353,275,191,189,432,526,591,516,507,838,874,934,934,1086,698,913,1717,1482],
#        'text':['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38'], 
#        'size':[4,4,3,54,22,162,3,44,9,0,22,4,12,67,32,32,46,6,159,17,13,3,4,3,11,79,15,12,5,19,22,20,20,34,18,27,50,35],'hue':['good','bad','average','poor','good','bad','average','poor','good','bad','average','poor','poor','poor','poor','poor','poor','poor','poor','good','bad','good','bad','good','bad','good','bad','good','bad','good','bad','average','average','average','average','average','average','average']}
#df = pd.DataFrame(d)
#b, a = np.polyfit(df['x-axis'], df['y-axis'], 1)
#xtest = np.linspace(df['x-axis'].min(),df['x-axis'].max(),10)
#with sns.plotting_context(rc={"legend.fontsize":25,"legend.markersize":18,"axes.titlesize":20,"font.weight":'heavy',"legend.labelspacing":20}):
#  p1 = sns.relplot(x='x-axis', y='y-axis',hue='hue',size='size',sizes=(300,1450),data=df,height=10, aspect=2 )
#ax = p1.axes[0,0]
##ax.plot(xtest, a + b* xtest, '--')
#for idx,row in df.iterrows():
#    x = row[0]
#    y = row[1]
#    text = row[2]
#    ax.text(x+.05,y,text, horizontalalignment='left')
##z = np.polyfit(df['x-axis'], df['y-axis'], 1)
##p = np.poly1d(z)
##plt.plot(df['x-axis'],p(df['x-axis']),"k--")
#p1.set(xticks=[i for i in range(0, max(df['x-axis']) + 50, 50)],
#       yticks=[i for i in range(0, max(df['y-axis']) + 500, 500)])
#
#
#plt.show()

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import scipy.stats as st


d = {'x-axis':[71,35,61,253,145,157,218,241,291,277,159,167,171,188,240,254,258,269,277,288,298,347,349,353,360,380,441,443,506,528,530,537,538,566,600,762,815,889],
    'y-axis': [5,5,15,79,75,641,172,867,289,67,75,112,46,150,70,70,897,391,671,54,353,275,191,189,432,526,591,516,507,838,874,934,934,1086,698,913,1717,1482],
    'text':['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38'],
    'size':[4,4,3,54,22,162,3,44,9,0,22,4,12,67,32,32,46,6,159,17,13,3,4,3,11,79,15,12,5,19,22,20,20,34,18,27,50,35],'hue':['good','bad','average','poor','good','bad','average','poor','good','bad','average','poor','poor','poor','poor','poor','poor','poor','poor','good','bad','good','bad','good','bad','good','bad','good','bad','good','bad','average','average','average','average','average','average','average']}

df = pd.DataFrame(d)

p1 = sns.relplot(x='x-axis', y='y-axis',hue='hue',size='size',sizes=(300,1450),data=df,height=10, aspect=2 )
p1._legend.remove()
ax = p1.axes[0,0]
for idx,row in df.iterrows():
    x = row[0]
    y = row[1]
    text = row[2]
    ax.text(x+.05,y,text, horizontalalignment='left')
p1.set(xticks=[i for i in range(0, max(df['x-axis']) + 50, 50)],
       yticks=[i for i in range(0, max(df['y-axis']) + 500, 500)])

#Regression part

slope, intercept, r_value, p_value, std_err = st.linregress(df['x-axis'],df['y-axis'])
line_df = pd.DataFrame()
line_df['line'] = slope*df['x-axis']+intercept
p,= plt.plot(df['x-axis'], line_df['line'],label='{:.2f}x+{:.2f}'.format(slope,intercept))

# adding legends for seaborn relplot
lgnd = plt.legend(loc="right", numpoints=1, fontsize=20)
for i in range(2,6):
    lgnd.legendHandles[i]._sizes = [600]  # you can change this for suitable size

plt.show()
