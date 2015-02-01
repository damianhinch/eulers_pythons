# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 15:28:05 2015

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

@author: Damian Hinch
"""

a = 0
mult = 0
rangeUpper = 1000
rangeLower = 1
for a in range (rangeLower, rangeUpper):
    if a % 3 == 0:
        mult += a
    elif a % 5 == 0:
        mult += a
        
print("Sum of multiples of 3 or 5 between " + str(rangeLower) 
+  " and " +  str(rangeUpper) + " is :")
print(mult)
            