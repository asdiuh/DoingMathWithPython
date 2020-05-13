#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:44:31 2020

@author: redhwanzaman1989
"""

from sympy import Symbol,Limit,S
x = Symbol('x')
Limit(1/x, x, S.Infinity)

n = Symbol('n')
Limit((1+1/n)**n,n,S.Infinity).doit()

from sympy import Symbol,Limit,S
p = Symbol('p',positive = True)
r = Symbol('r',positive = True)
t = Symbol('t',positive = True)
Limit(p*(1+r/n)**(n*t),n,S.Infinity).doit()


#differentiate
x = Symbol('x')
Fx = 5*x**2 + 2*x + 8
dx = Symbol('dx')
Limit((Fx.subs({x:x+dx}) - Fx.subs({x:x}))/dx,dx,0).doit()