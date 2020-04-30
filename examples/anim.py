#!/usr/bin/env python
# -*- no-plot -*-
"""
Compare line drawing performance of Matplotlib vs. GR
"""

from numpy import arange, sin, pi
from time import time, sleep
import os

os.environ["GKS_WSTYPE"] = "gksqt"

num_frames = 200

x = arange(0, 2 * pi, 0.01)

# create an animation using GR

from gr.pygr import plot

tstart = time()
for i in range(num_frames):
    plot(x, sin(x + i / 10.0))
    sleep(0.0001)

fps_gr = int(num_frames / (time() - tstart))
print('fps  (GR): %4d' % fps_gr)

# create the same animation using matplotlib

from matplotlib.pyplot import plot, draw, pause

tstart = time()
line, = plot(x, sin(x))
for i in range(num_frames):
    line.set_ydata(sin(x + i / 10.0))
    draw()
    pause(0.0001)

fps_mpl = int(num_frames / (time() - tstart))
print('fps (mpl): %4d' % fps_mpl)

print('  speedup: %6.1f' % (float(fps_gr) / fps_mpl))
