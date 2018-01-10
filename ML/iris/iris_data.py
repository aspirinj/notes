# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 00:35:41 2018

@author: Howard
"""


# In[]
from sklearn.datasets import load_iris
data = load_iris()
data.target[[10, 25, 50]]

# In[]
list(data.target_names)


