# -*- coding: utf-8 -*-

# In[]
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

# In[]
cancer = load_breast_cancer()
print(cancer.DESCR)

# In[]
cancer.keys()  # sklearn.utils.Bunch

# In[]
cancer['data']  # numpy.ndarray
cancer.data

# In[]
cancer['data'].shape
cancer.data.shape

# In[]
cancer.feature_names

# In[]
cancer.target

# In[]
cancer.target_names

# In[]
X = pd.DataFrame(cancer.data)
y = pd.DataFrame(cancer.target)
df = pd.DataFrame(data=np.c_[cancer['data'], cancer['target']],
                  columns=np.append(cancer['feature_names'], 'target'))

# In[]
s = df.target.value_counts()
s.sort_index(inplace=True)
s.index = ['malignant', 'benign']
s
