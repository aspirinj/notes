# -*- coding: utf-8 -*-

# In[]
import pandas as pd
import numpy as np
import scipy as sc
import scipy.sparse as sp
import seaborn as sns

# In[]
"""
Pandas - counting rows
"""
df = pd.DataFrame(np.arange(9).reshape(3,3))
print(df)
print(df.shape)

# three methods
df.shape
df[0].count()
len(df.index)
