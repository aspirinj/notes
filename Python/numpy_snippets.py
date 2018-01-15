# -*- coding: utf-8 -*-

# In[]
import numpy as np

# In[]
"""
vector form vs matrix form
"""

a = np.array(1,2) # error
b = np.array([1,2])
c = np.array([[1],[2]])

b.shape
c.shape

b.reshape(-1,1).shape



# In[]
"""
bincount, only valid for dtype('int64')
"""
x = np.array([1,1,1,2,2,2,5,8,1,1])
y = np.bincount(x)
print(x, '\n', y, '\n')


