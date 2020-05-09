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

'''***********************************************************'''

#import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def update_radius(i, circle):
    circle.radius = i*0.5
    return circle,

fig=plt.gcf()
ax=plt.axes(xlim=(-10,10),ylim=(-10,10))
ax.set_aspect('equal')
#circle=create_circle()
circle = plt.Circle((0, 0), 0.05)
ax.add_patch(circle)
anim=FuncAnimation(fig,
                   update_radius,
                   fargs=(circle,),
                   frames=30,
                   interval=50)
plt.show()

#*************************************************************

red_list = ["red1","red2","red3","red4","red5","red6","red7","red8","red9"]
for i,c in enumerate(red_list,1):
    print(i,c)

#*************************************************************
#book projectile motion
'''
Animate the trajectory of an object in projectile motion
'''
from matplotlib import pyplot as plt
from matplotlib import animation
import math
g = 9.8

def get_intervals(u, theta):
    t_flight = 2*u*math.sin(theta)/g
    intervals = []
    start = 0
    interval = 0.005
    while start < t_flight:
        intervals.append(start)
        start = start + interval
    return intervals

def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = u*math.cos(theta)*t
    y = u*math.sin(theta)*t - 0.5*g*t*t
    circle.center = x, y
    return circle,

def create_animation(u, theta):
    intervals = get_intervals(u, theta)
    xmin = 0
    xmax = u*math.cos(theta)*intervals[-1]
    ymin = 0
    t_max = u*math.sin(theta)/g
    ymax = u*math.sin(theta)*t_max - 0.5*g*t_max**2
    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    circle = plt.Circle((xmin, ymin), 1.0)
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_position,
                                   fargs=(circle, intervals, u, theta),
                                   frames=len(intervals), interval=1,
                                   repeat=False)
    plt.title('Projectile Motion')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

theta = math.radians(45)
u = 45
create_animation(u, theta)














