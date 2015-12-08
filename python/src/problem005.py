# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 14:13:06 2015

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

@author: damianhinch
"""

num = 20
found = False
counter = num

while found != True :
    counter = counter + num
    for i in range(num -1, 2, -1):
        if (counter % i) != 0:
            found = False
            break
        else:
            found = True

print(counter)

