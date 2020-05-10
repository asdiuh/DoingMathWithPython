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

def update_position(i):
#    t = intervals[i]
#    x = u*math.cos(theta)*t
#    y = u*math.sin(theta)*t - 0.5*g*t*t
    circle.center = i, i
    return circle,

theta = 45
u = 10
g = 9.8
theta = math.radians(theta)
t_flight = 2*u*math.sin(theta)/g
intervals = []
start = 0
interval = 0.005
while start < t_flight:
    intervals.append(start)
    start = start + interval
xmax = u*math.cos(theta)*intervals[-1]
t_max = u*math.sin(theta)/g
ymax = u*math.sin(theta)*t_max - 0.5*g*t_max**2
fig = plt.gcf()
circle = plt.Circle((0,0), 1.0)
ax = plt.axes(xlim=(0, xmax), ylim=(0, ymax))
ax.add_patch(circle)
anim = animation.FuncAnimation(fig, update_position,
                               fargs=(circle,),
                               frames=100, interval=1,
                               repeat=False)
plt.title('Projectile Motion')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

create_animation(45, 15)

#**********************************************************
from matplotlib import pyplot as plt
from matplotlib import animation
import math

def interval(end):
    time = []
    i = 0
    while i <= end:
        time.append(i)
        i = i + .01
    return time

def throw(u,theta):
    g = 9.8
    theta = math.radians(theta)
    uy = u*math.sin(theta)
    ux = u*math.cos(theta)
    t = 2 * uy/g
    print(t)
    time = interval(t)
    print(time)
    Sx = []
    Sy = []
    for i in time:
        t = i
        Sx.append(ux*t)
        Sy.append(uy*t - 0.5*g*t**2)
    plt.plot(Sx,Sy)

throw(15,60)


import matplotlib.pyplot as plt
import animation as animation

#***************************************************************

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

g = 9.8 #value of gravity
v = 10.0 #initial velocity
theta = 40
theta = 40.0 * np.pi / 180.0 #initial angle of launch in radians
t = 2 * v * np.sin(theta) / g
t = np.arange(0, 0.1, 0.01) #time of flight into an array
x = np.arange(0, 0.1, 0.01)
line, = ax.plot(x, v * np.sin(theta) * x - (0.5) * g * x**2) # plot of x and y in time

def animate(i):
    """change the divisor of i to get a faster (but less precise) animation """
    line.set_xdata(v * np.cos(theta) * (t + i /100.0))
    line.set_ydata(v * np.sin(theta) * (x + i /100.0) - (0.5) * g * (x + i / 100.0)**2)  
    return line,

plt.axis([0.0, 10.0, 0.0, 5.0])
ax.set_autoscale_on(False)

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))
plt.show()

#**********************************************************

import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def update_radius(i, circle):
    circle.radius = i
    circle.center = i,i
    return circle,

u = 45
theta = 45
theta = math.radians(theta)
g = 9.8
ux = u*math.sin(theta)
uy = u*math.cos(theta)
total_time = 2*uy/g
vx = ux
vy = uy - g*t

fig=plt.gcf()
ax=plt.axes(xlim=(-10,10),ylim=(-10,10))
ax.set_aspect('equal')
#circle=create_circle()
circle = plt.Circle((0, 0), 0.05)
ax.add_patch(circle)
anim=FuncAnimation(fig,
                   update_radius,
                   fargs=(circle,),
                   frames=200,
                   interval=1)
plt.show()

#*****************************************************

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

g = 9.8 #value of gravity
v = 10 #initial velocity
theta = 15
theta = math.radians(theta) #initial angle of launch in radians
t = 2 * u * math.sin(theta) / g
t = np.arange(0, 0.1, 0.01) #time of flight into an array
x = np.arange(0, 0.1, 0.01)
line, = ax.plot(x, v * np.sin(theta) * x - (0.5) * g * x**2) # plot of x and y in time

def animate(i):
    """change the divisor of i to get a faster (but less precise) animation """
    line.set_xdata(v * np.cos(theta) * (t + i /100.0))
    line.set_ydata(v * np.sin(theta) * (x + i /100.0) - (0.5) * g * (x + i / 100.0)**2)  
    return line,

plt.axis([0.0, 10.0, 0.0, 5.0])
ax.set_autoscale_on(False)

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))
plt.show()

#*****************************************************

import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def update_radius(i, circle):
    circle.radius = 10
#    x = 
    circle.center = i,i
    return circle,

u = 40
theta = 30
g = 9.8
theta = math.radians(theta)
ux = u*math.cos(theta)
uy = u*math.sin(theta)
t = 2 * uy / g
interval = t/100
t1 = []
num = 0
while num <= t:
    t1.append(num)
    num = num + interval

fig=plt.gcf()
ax=plt.axes(xlim=(-200,200),ylim=(-200,200))
ax.set_aspect('equal')
#circle=create_circle()
circle = plt.Circle((0, 0), 10)
ax.add_patch(circle)
anim=FuncAnimation(fig,
                   update_radius,
                   fargs=(circle,),
                   frames=200,
                   interval=1)
plt.show()


#*************************************************************
from matplotlib import pyplot as plt
from matplotlib import animation
import math
import numpy as np
g = 9.8
def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    t = float(t)
    x = u*math.cos(theta)*t
    y = u*math.sin(theta)*t - 0.5*g*t*t
#    circle.center = i, i
    circle.center = x, y
    return circle,
u = 30
theta = 45
t_flight = 2*u*math.sin(theta)/g
intervals = []
start = 0
interval = 0.005
while start < t_flight:
    intervals.append(float(start))
    start = start + interval
xmin = 0
xmax = u*math.cos(theta)*intervals[-1]
ymin = 0
t_max = u*math.sin(theta)/g
ymax = u*math.sin(theta)*t_max - 0.5*g*t_max**2 + 10
fig = plt.gcf()
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
ax.set_aspect('equal')
circle = plt.Circle((xmin, ymin), 1.0)
ax.add_patch(circle)
anim = animation.FuncAnimation(fig, update_position,
                    fargs=(circle, intervals, u, theta),
                    frames=len(intervals), interval=.000001,
                    repeat=True)
#len(intervals)
plt.title('Projectile Motion')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#**************************************************

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
        intervals.append(float(start))
        start = start + interval
    return intervals
def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    t = float(t)
    x = u*math.cos(theta)*t
    y = u*math.sin(theta)*t - 0.5*g*t*t
    circle.center = x, y
#    circle.radius = i*0.5
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
    ax.set_aspect('equal')
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

u = 45
theta = 45
theta = math.radians(theta)
create_animation(u, theta)


