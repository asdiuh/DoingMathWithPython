#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:12:57 2020

@author: redhwanzaman1989
"""
def calculate_mean(number):
    s = sum(number)
    l = len(number)
    mean = s/l
    print('mean is {0}'.format(mean))
    return mean
    
def calculate_median(number):
    number = money
    number1 = sorted(number)
    n = len(number1)
    print(n)
    if (n%2) == 1:
        print('odd')
        m = (n+1) / 2
        median = number[m]

    elif (n%2) == 0:
        print('even')
        n = len(number)
        m1 = int(n/2)
        m2 = int(n/2 + 1)
        median = (float(number[m1]) + float(number[m2]))/2
        print('median is {0}'.format(median))
        
    return median
    print('median is {0}'.format(median))    
        
money = [
        806.75,
        801.92,
        774.01,
        587.03,
        797.51,
        908.04,
        859.05,
        528.03,
        978.42,
        911.05
        ]

calculate_mean(money)
calculate_median(money)


#find mode
simplelist = [4,2,1,3,4]
from collections import Counter
c = Counter(simplelist)
c


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from collections import Counter


# from collections import Counter
# SimpleList = [4,2,1,3,4]
# c = Counter(SimpleList)
# c.most_common()
# print('Counter = ',c)
# print('list of most common: ',c.most_common())
# a = c.most_common()
# print('first element of most common (method 1): ',a[0])
# print('first element of most common using a different method (method 2): ', 
#c.most_common(1))
# print('as can be seen, the difference between method 1 and method 2 is that 
#method 2 results in a list with a tuple as the first element, 
#whilst method 1 results in just a tuple')
# print('method 1: ', c.most_common()[0], ', and method 2: ', c.most_common(1))

# going to create a function that identifies the mode

# from collections import Counter

# def mode(number):
#     count_list = Counter(number)
#     mode_list = count_list.most_common()
#     print('count_list = ', count_list)
#     print('mode_list = ', mode_list)
#     print('mode is :', mode_list[0][0],', and it appears ', 
#mode_list[0][1], ' times')
#     return

# mode(number)

# def mode_updated(number):
#     count_list = Counter(number)
#     mode_list = count_list.most_common()
#     max_number = mode_list[0][1]
#     final_modes = []
#     for i in range(0, len(mode_list)):
#         if mode_list[i][1] == max_number:
#             final_modes.append(mode_list[i][0])
        
    # print(count_list)
    # print(mode_list)
    # print(max_number)
    # print('modes are: ', final_modes, 'and it appears: ', max_number, 
    #' times')
    # print('number\tfrequency')
    # m = 0
    # for j in mode_list:
    #     print('{0}\t{1}'.format(j[0], j[1]))

# number = [1,3,4,5,5,5,5,5,4,4,4,4]
# number = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
# mode_updated(number)

# def find_range(number):
#     lowest = min(number)
#     highest = max(number)
#     r = highest - lowest
#     return lowest, highest, r
    
# lowest, highest, r = find_range(number)
# print('lowest = {0}, highest = {1}, range = {2}'.format(lowest, highest, r))

#variance is defined as sigma((x - mean(x))^2)/n

def DescriptiveStatistics(number):
    n = len(number)
    total = sum(number)
    mean = total/n
    minimum = min(number)
    maximum = max(number)
    range_number = maximum - minimum
    mode1 = Counter(number)
    mode2 = mode1.most_common()
    mode_number = []
    mode_frequency = []
    max_number = mode2[0][1]
    for j in mode2:
        if j[1] == max_number:
            mode_number.append(j[0])
            mode_frequency.append(j[1])
    var1 = []
    for k in range(0,n):
        var1.append((number[k] - mean)**2)
    variance = sum(var1)/n
    standard_deviation = variance**(0.5)
    
    print('n = {0}'.format(n))
    print('total = {0}'.format(total))
    print('mean = {0}'.format(mean))
    print('mode1 = {0}'.format(mode1))
    print('mode2 = {0}'.format(mode2))
    print('max_number = {0}'.format(max_number))
    print('mode_number = {0}'.format(mode_number))
    print('mode_frequency = {0}'.format(mode_frequency))    
    print('variance = {0}'.format(variance))
    print('standard_deviation = {0}'.format(standard_deviation))


# number = [53, 60, 69, 58, 82, 73, 9, 23, 24, 13,
# 67,67,67,67,67,67,67,10,10,10,10,10,10,10]

donations1 = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
donations2 = [382, 389, 377, 397, 396, 368, 369, 392,
398, 367, 393, 396]

# DescriptiveStatistics(number)
print('end')
DescriptiveStatistics(donations1)
print('end')
DescriptiveStatistics(donations2)

plt.plot(range(1,len(donations1)+1),sorted(donations1))
plt.plot(range(1,len(donations2)+1),sorted(donations2))
plt.show()

number1 = [1,2,3]
number2 = [4,5,6]

def correl(number1, number2):
  cov1 = []
  varx = []
  vary = []
  n1 = len(number1)
  n2 = len(number2)
  if n1==n2:
    mean1 = sum(number1)/n1
    mean2 = sum(number2)/n2
    for i in range(0,n1):
      cov1.append((number1[i] - mean1)*(number2[i] - mean2))
      varx.append((number1[i] - mean1)**2)
      vary.append((number2[i] - mean2)**2)
    cov = sum(cov1)/n1
    varx = sum(varx)/n1
    vary = sum(vary)/n2
    sdx = varx**0.5
    sdy = vary**0.5
    correlation = cov/(sdx*sdy)
    print('cov = {0}'.format(cov))
    print('varx = {0}'.format(varx))
    print('vary = {0}'.format(vary))
    print('sdx = {0}'.format(sdx))
    print('sdy = {0}'.format(sdy))
    print('correlation = {0}'.format(correlation))
  else:
    print('different_lengths')

correl(number1, number2)

  
  
import matplotlib.pyplot as plt

high_school = [90 ,92 ,95 ,96 ,87 ,87 ,90 ,95 ,98 ,96]
college = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

plt.plot(high_school, college, 'o')
plt.show()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
curDir = os.getcwd()
os.chdir('/home/redhwanzaman1989/DoingMathWithPython')

def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s = s + float(line)
#            print(line)
    print('Sum of of the numbers: {0}'.format(s))

sum_data('myfile.txt')


def read_files(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers

a = read_files('myfile.txt')

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

if __name__ == '__main__':
    data = read_files('myfile.txt')
    mean = calculate_mean(data)
    print('Mean: {0}'.format(mean))


import csv
import matplotlib.pyplot as plt

def read_csv(filename):
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        next (reader)
        for row in reader :
            print(row)
            numbers.append(row[0])
            squared.append(row[1])
        return numbers, squared
numbers, squared = read_csv('Number Squared.csv')
    
plt.scatter(numbers, squared)
plt.plot([9,10,22], [81,100,484])






