from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
 
# Make a Basic Venn
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels = ('Anchore', 'Clair-scanner', 'Vuls'))
 
# Custom it
v.get_label_by_id('100').set_text('4453')
v.get_label_by_id('010').set_text('673')
v.get_label_by_id('110').set_text('1031')
v.get_label_by_id('001').set_text('325')
v.get_label_by_id('101').set_text('657')
v.get_label_by_id('011').set_text('2220')
v.get_label_by_id('111').set_text('10691')
for text in v.set_labels:
    text.set_fontsize(18)
for text in v.subset_labels:
    text.set_fontsize(15)
# Show it
#plt.savefig('venn.pdf',dpi=2000)
plt.show()
