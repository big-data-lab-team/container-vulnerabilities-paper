#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
df = pd.read_csv(r"train.csv")
df.head()
sns.relplot(x="Views", y="Upvotes", data = df)
#sns.plt.show()
