# -*- coding: utf-8 -*-


# In[]
# cmap is only used if c is an array of floats
import matplotlib.pyplot as plt
cm = plt.cm.get_cmap('RdYlBu')
xy = range(20)
z = xy
plt.scatter(xy, xy, c=z, vmin=0, vmax=20, s=35, cmap=cm)
plt.colorbar()
plt.show()



