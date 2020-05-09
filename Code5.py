#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:41:28 2020

@author: redhwanzaman1989
"""

from sympy import FiniteSet
s = FiniteSet(2,4,6)
s

from sympy import FiniteSet
from fractions import Fraction
s = FiniteSet(1, 1.5, Fraction(1,5))
s
4 in s

s = FiniteSet()
s

members = [1,2,3]
s = FiniteSet(*members)
s = FiniteSet(*members)
s

from sympy import FiniteSet
s = FiniteSet(1,2,3)
for member in s:
    print(member)

from sympy import FiniteSet
s = FiniteSet(3,4,5)
t = FiniteSet(5,4,3)
s == t


s = FiniteSet(1)
t = FiniteSet(1,2)
s.is_subset(t)
t.is_subset(s)
t.is_superset(s)
s = FiniteSet(1,2,3)
ps = s.powerset()
ps

len(ps)


#is 53 prime?
for i in range(1,54):
    if i == 1:
        print('i = 1')
    elif i == 53:
        print('i = 53')
    elif int(i) != 1 or int(i) != 53:
        if 53%i == 0:
            print('prime, iteration = {0}'.format(i))
        else: print('not prime')

primes = [1,2]
for i in range(3,104987):
    primes_staging = []
    for j in range(2,int(i)): #2,3,4
        if i%j == 0: #5,2,3,4
            primes_staging.append(1)
    if sum(primes_staging) == 0:
        print('{0} is a prime number!'.format(i))
        primes.append(i)

#print(primes)


#T = 2 * pi * (L/g)^0.5

from sympy import pi, Symbol
from sympy.plotting import plot
x = Symbol('x')
plot(pi*x, (x, -2,1))


from sympy import FiniteSet, pi

pendulum_list = [15,18,21,22.5,25]
pendulum_set = FiniteSet(15,18,21,22.5,25)
def pendulum(number):
    for i in number:
        L = i/100
        g = 9.8
        T = 2 * pi * (L/g)**0.5
        print('length: {0}, T: {1:.3f}'.format(float(L), float(T)))

pendulum(pendulum_list)
pendulum(pendulum_set)

#whats the difference between using lists and sets?

#apply same deal as before but with different g's
length_set = FiniteSet(15,18,21,22.5,25)
gravity_set = FiniteSet(9.78, 9.8, 9.83)
length_gravity_all = length_set*gravity_set
print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)','Gravity(m/s^2)'
      ,'Time Period(s)'))
for i in length_gravity_all:
    L = i[0]/100
    g = i[1]
    T = 2*pi*(L/g)**0.5
    print('{0:^15}{1:^15}{2:^15.3f}'.format(float(L),float(g),
          float(T)))

#new format types

#probability
#probability = length of event set/length of sample space
#probability of a fair dice landing on a number
from sympy import FiniteSet
sample_space = FiniteSet(1,2,3,4,5,6)
event_space = []

def dice_roll1(number):
    for i in sample_space:
        if i in number:
            event_space.append(i)
    probability = len(event_space)/len(sample_space)
    return probability
p_list = [1,2,3]
a = dice_roll1(p_list)

#1. define sample space
#2. cycle through sample space 
#   and identify valid outcomes to determine event space
#3. event space / sample space = probability

#roll 20 sided die, whats the probability of rolling a prime?
sample_space = range(1,21)
event_space = []
def check_primes(sample_space):
    for number in sample_space:
        if number == 1:
            return True
        else:
            for j in range(2,number):
                if number%j ==0:
                    return False
    return True

check_primes(sample_space)


#find all primes from 1 to 1000
#for each number in 2 to 1000, divide by all integers and find remainder
#cycle through
prime=[]
def primes(ceiling):
    for i in range(1,int(ceiling)):
        x = True
        if i==1:
            x = True
        else:
            for j in range(2,i):
                if i%j==0:
                    x = False
        if x:
            print('{0} is a prime number!'.format(i))
            prime.append(i)
    return prime

prime1 = primes(1000)

import matplotlib.pyplot as plt
plt.plot(range(1,len(prime1)+1), prime1)



