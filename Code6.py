#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:18:22 2020

@author: redhwanzaman1989
"""

import matplotlib.pyplot as plt
x = [1,2,3]
y = [1,2,3]
fig=plt.figure()
ax=plt.axes()
plt.plot(x,y)
plt.show()


circle = plt.Circle((0, 0), radius = 0.5)
ax=plt.gca()
ax.set_aspect('equal')
ax.add_patch(circle)
plt.axis('scaled')
plt.show()




import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
plt.show()

anim.save('sine_wave.gif', writer='imagemagick')