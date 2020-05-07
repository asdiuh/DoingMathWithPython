#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:43:27 2020

@author: redhwanzaman1989
"""
'''
print("Hello SPYDER")
1+2
1+3.5
-1+2.5
100-45
-1.1+5
3*2
3.5*1.5
3/2
4/2
#floor operator
3//2
-3//2
#modular arithmetic operator %
9%2
#exponential **
2**2
2**10
1**10
8**(1/3)
5+5*5
(5+5)*5
a = 3
a+1
a  =5
a+1
type(3)
type(3.8)

print("Hello SPYDER")

from fractions import Fraction
f = Fraction(3/4)
Fraction(3/4) + 1 + 1.5
Fraction(3/4) + Fraction(1/4) + 1
#imaginary numbers denoted by j instead of i
a = 2 + 3j
type(a)
b = 3 + 3j
a + b
a - b
(a*b)
(a/b)
z = 2+3j
z.real
z.imag
z.conjugate()
(z.real**2 + z.imag**2)**.5
abs(z)
a = input()
1
a

print("Hello SPYDER")

s1 = 'a string'
s1 = "a string"
a = '1'
int(a) + 1
float(a) + 1
int('2.0')

try:
    a = float(input('Enter a number: '))
except ValueError:
    print('You entered an invalid number')
    
a = input('Input an integer')
a = int(input())

def is_factor(a,b):
    if b % a == 0 :
        return True
    else:   
        return False

is_factor(4,1024)

for a in range(1,4):
    print(a)
    
for a in range(5):
    print(a)
    
for a in range(1,10,2):
    print(a)
'''

# Python program to execute  
# main directly 
# if name = main means youre running the code directly in the IDE
# if youre importing the file, then name wont = main
print("Always executed")
  
if __name__ == "__main__": 
    print("Executed when invoked directly")
else: 
    print("Executed when imported")
    
def multipication_tables(a):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
        
if __name__ == '__main__':
    a = input('Enter a number: ')
    multipication_tables(int(a))
    
#page 36

'''
Unit converter distance or temperature
'''
'''
def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))
    
def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))
    
if __name__ == '__main__':

    print_menu()

choice = input('Which conversion would you like to do?: ')

if choice == '1':
    km_miles()
    
if choice == '2':
    miles_km()
    
'''

def roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))

if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a), float(b), float(c))
    
def func_1():
    print('Odd/Even Program')
    
def seq_num():
    print('The next {0} {1} numbers, starting from {2} are :'.format(b,c,a))
    for i in range(1,b+1):
        print('{0}'.format(a + (i * 2)))

if __name__ == '__main__':

    func_1()

a = int(input('Please input a number: '))
b = int(input('How long would you like the sequence? '))

if a%2 == 1:
    print('Number is odd')
    c = 'odd'
if a%2 == 0:
    print('Number is even')
    c = 'even'
    
seq_num()


def multi_1():
    print('Multiplication table program')

def multi_2():
    for i in range(1,int(b)+1):
        print('{0:.0f} x {1} = {2:.0f}'.format(a, i, a*i))
        
if __name__ == '__main__':
    
    multi_1()
    print('  ')
    a = float(input('What multiplication table would you like to see? '))
    b = float(input('how many multiples would you like to see? '))
    if a%1 == 0 and b%1 == 0:
        multi_2()
    else: print('Please ensure both numbers are integers')
    

def unit_converter_1():
    print('1. Km to Miles')
    print('2. Miles to Km')
    print('3. Celcius to Farenheit')
    print('4. Farenheit to Celcius')
    print('5. Kg to Pounds')
    print('6. Pounds to Kg')

def miles_to_km():
    km = miles * 1.609
    print('{0} Miles is equal to {1} Kilometeres'.format(miles, km))
    
def km_to_miles():
    miles = km / 1.609
    print('{0} Kilometres is equal to {1} Miles'.format(km, miles))    

def far_to_cel():
    cel = (far - 32)*(5/9)
    print('{0} Farenheit is equal to {1} Celcius'.format(far, cel))
    
def cel_to_far():
    far = (cel * 9/5) + 32
    print('{0} degrees Celcius is equal to {1} degrees Farenheit'.format(cel, far))
    
def lb_to_kg():
    kg = lb / 2.20462
    print('{0} lb is equal to {1} kg'.format(lb, kg))
    
def kg_to_lb():
    lb = kg * 2.20462
    print('{0} kg is equal to {1} lb'.format(kg, lb))
    
if __name__ == '__main__':
    
    while True:        
        unit_converter_1()
        choice = float(input('What conversion would you like to do? '))
        
        if int(choice) == 1:
            miles = float(input('Enter miles: '))
            miles_to_km()
            
        if int(choice) == 2:
            km = float(input('Enter Km: '))
            km_to_miles()
            
        if int(choice) == 3:
            far = float(input('Enter Farenheit: '))
            far_to_cel()
    
        if int(choice) == 4:
            cel = float(input('Enter Celcius: '))
            cel_to_far()
    
        if int(choice) == 5:
            lb = float(input('Enter Pounds: '))
            lb_to_kg()
            
        if int(choice) == 6:
            kg = float(input('Enter Kg: '))
            kg_to_lb()
            
        
        print(' ')
        loop_end = input('End Program? (y) for Yes ')
        
        if loop_end == 'y':
            break
