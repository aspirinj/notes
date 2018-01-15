# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


# In[]
"""
cmap is only used if c is an array of floats
"""

cm = plt.cm.get_cmap('RdYlBu')
xy = range(20)
z = xy
plt.scatter(xy, xy, c=z, vmin=0, vmax=20, s=35, cmap=cm)
plt.colorbar()
plt.show()



# In[]
"""
Get fig, ax
"""

fig, ax = plt.subplots(1, 1)
# or
fig, (ax1, ax2) = plt.subplots(2, 1)
