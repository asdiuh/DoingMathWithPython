#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:15:56 2020

@author: redhwanzaman1989
"""

#page 51

from pylab import plot, show, legend, title, xlabel, ylabel, axis, savefig
import matplotlib.pyplot as plt
import math
#from collections import namedtuple


x_numbers = [1,2,3]
y_numbers = [2,4,6]

#plot(x_numbers, y_numbers, marker = 'o')
#plot(x_numbers, y_numbers)
plot(x_numbers, y_numbers,'o')
show()

nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55,55.3,54,56.7,56.4,57.3]
years = range(2000,2013)
#plot(nyc_temp, marker = 'o')
plot(years, nyc_temp, marker = 'o')

nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1,13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012, marker = 'o')
legend([2000,2006,2012])
title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
axis(ymin = 0)
savefig('mygraph.png')
savefig('/home/redhwanzaman1989/Python Webscraper/mygraph.png')

'''
import matplotlib.pyplot

def create_graph():
    x_numbers = [1,2,3]
    y_numbers = [2,4,6]
    matplotlib.pyplot.plot(x_numbers, y_numbers)
    matplotlib.pyplot.show()

create_graph()
'''

def draw_graph(x,y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Distance in metres')
    plt.ylabel('Gravitational force in Newtons')
    plt.title('Gravitational force and distance')
    plt.show()
    
def generate_F_r():
    r = range(100, 1001, 50)
    F = []
    G = 6.674 * 10**-11
    m1 = .5
    m2 = 1.5
    
    for dist in r:
        force = G * m1 * m2 / dist**2
        F.append(force)
    
    draw_graph(r,F)

generate_F_r()

def frange(start, final, increment):
    l = []
    while start <= final:
        l.append(start)
        start = start + increment
    return l

if __name__ == '__main__':
    empty_list = []
    l = range(1,10)
    for num in l:
        empty_list.append(num/2)

x = []
y = []

for i in range(-100, 100):
    x.append(i)
    y.append(i**2)

plot(x,y)


def frange(start, final, increment):
    l = []
    while start <= final:
        l.append(start)
        start = start + increment
        
    return l 

def draw_trajectory(u, theta):
    g = 9.8
    theta = math.radians(theta)
    t_flight = 2*u*math.sin(theta)/g
    l = frange(0, t_flight, .001)
    x=[]
    y=[]
    for t in l:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*(t**2))
    plt.plot(x,y)
    plt.xlabel('horizontal distance thrown')
    plt.ylabel('height reached')
    plt.title('projectile motion of a ball')

for i in range(1,90):    
    draw_trajectory(30,i)


if __name__ == '__main__':    
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('Invalid inputs')
    else:
        draw_trajectory(u,theta)


boston_temp = [4,3,5,4,6,5,5,5,5]
la_temp = [23,18,22,17,21,16,20,22,16]
x_axis = range(1,len(boston_temp)+1)
time = ['10am','1pm','4pm','7pm','10pm','1am','4am','7am','10am']

plt.plot(x_axis, boston_temp,x_axis, la_temp)
plt.xticks(x_axis,time)
show()
#74


'''
Quadratic function calculator
'''
# Assume values of x
x_values = range(-1200,1100)
x_decimals = []
y_values = []
for x in x_values:
    # Calculate the value of the quadratic function
    x = x/100
    x_decimals.append(x)
    y = x**2 + 2*x + 1
    y_values.append(y)
    print('x={0} y={1}'.format(x, y))


plt.plot(x_decimals,y_values)


def frange(start, final, increment):
    l = []
    while start <= final:
        l.append(start)
        start = start + increment
        
    return l 

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

def red_macro(x,y,z):
    l = []

    if not z:
        print('Invalid arguments')
        return
        
    if x < y:
        while x <= y:
            l.append(x)
            x = x+z
        return l
    elif x > y:
        while x >= y:
            l.append(x)
            x = x - z
        return l

#a = red_macro(10,-5,.001)
#print(a)

def red_prod_function(u, theta):
#if someone throws a ball in the air, you need the angle (theta) they threw
#and the speed (u) they threw it. This speed can then be broken down into 
#2 separate componenets - sin and cos theta
#therefore uy = u*sin(theta) and ux = u*cos(theta)
#if you take vx and vy as the instantaneous velocity at a given time
#assume that ux remains constant
#vy will decelerate at 9.8m/s
#if g is 9.8, then that implies that the equation of speed is the integral of 
#that
#vy = uyt - 9.8t = u*sin(theta)*t - 0.5*9.8*t
    g = 9.8
    theta = math.radians(theta)
    ux = u * math.cos(theta)
    uy = u * math.sin(theta)
#    vx = ux
#    vy = uy - g*t
    total_time = 2 * uy / g
    a = red_macro(0,total_time, .01)
    sx_plot = []
    sy_plot = []
    for i in a:
        sx = ux*i
        sy = uy*i - 0.5*g*i**2
        sx_plot.append(sx)
        sy_plot.append(sy)
    plot(sx_plot,sy_plot)

def number_call(number):
    j = 1
    while j <= number:
        print(' ')        
        print('For throw {0} of {1: .0f}'.format(j,number)) 
        j = j+1
        u = float(input('How fast was the ball thrown? (in m/s) '))
        theta = float(input('What angle was the ball thrown? (in degrees) '))
        red_prod_function(u, theta)
    print(' ')

def final_call():
    while True:
        number = float(input('How many times did you throw the ball? '))
        number_call(number)
        loop_end = input('Would you like to plot more throws? (n) for No ')
        if loop_end in ('n', 'N'):
            break

try:
    final_call()
except ValueError:
    print('Invalid input entered ')
finally:
    print('Program ended')

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

steps = [16247,15520,10392,16971,14356,13707,12308,19231]
day = ['Monday1','Tuesday',
       'Wednesday','Thursday',
       'Friday','Saturday','Sunday',
       'Monday2']
bar_axis = range(1,len(steps)+1)

plt.barh(bar_axis, steps)
plt.xlabel('Number of steps')
plt.ylabel('Day')
plt.yticks(bar_axis, day)



#create first n numbers of the fibonacci sequence and plot them

import matplotlib.pyplot as plt

def fibonnaci(number):
    fib_final = []
    fib_plot = []
    for i in range(0,number+1):
        if int(i) == 0:
            fib_final.append(1)
        elif int(i) == 1:
            fib_final.append(1)
        else: 
            # print(i)
            n3 = fib_final[int(i-2)] + fib_final[int(i-1)]
            # print(n3)
            fib_final.append(n3)
    for j in range(0,len(fib_final)-1):
        print(j)
        fib_plot.append(fib_final[int(j+1)] / fib_final[int(j)])
    print(fib_plot)
    print(fib_final)
    plt.plot(range(1,len(fib_plot)+1), fib_plot)
    return

fibonnaci(20)










