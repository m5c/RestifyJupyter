"""
2D plotter module that creates visualizations of test success rates for population / population
subsets and for one or two selected applications.
Inspired by: https://stackoverflow.com/a/7230921
"""

import matplotlib as mpl
from matplotlib import pyplot
import numpy as np

# make values from -5 to 5, for this example
zvals = np.random.rand(100, 100) * 10 - 5

# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['blue', 'black', 'red'])
bounds = [-6, -2, 2, 6]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
img = pyplot.imshow(zvals, interpolation='nearest',
                    cmap=cmap, norm=norm)

# make a color bar
pyplot.colorbar(img, cmap=cmap,
                norm=norm, boundaries=bounds, ticks=[-5, 0, 5])

pyplot.show()
