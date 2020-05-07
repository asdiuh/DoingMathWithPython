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













