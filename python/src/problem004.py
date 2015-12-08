# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 14:13:06 2015

Problem 4

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. 

@author: damianhinch
"""

"""
Just brute force... Take a 3 digit number, multiple it, check if palindorome.
If you find another, check which is bigger. Will take at most 999 * 999 
iterations, roughly 998001.
"""

def findBiggestPalindromeXDigits(digits):
    
    lowerLimit = 10 ** (digits - 1)
    upperLimit = 0
    for k in xrange (digits, 0, -1):
        upperLimit = upperLimit + 9 * (10 ** (k-1)) 

    highestPalindrome = 0
    factor1 = 0
    factor2 = 0
    for i in xrange(lowerLimit, upperLimit):
        for j in xrange(lowerLimit, upperLimit):
            product = i * j
            if isPalindrome(product):
                if highestPalindrome < product:
                    highestPalindrome = product
                    factor1 = i
                    factor2 = j
         
    print("Factors %s,%s yielding %s" %(factor1, factor2, highestPalindrome))           
    return highestPalindrome


def isPalindrome(palindrome):
    num = str(palindrome)
    lenNum = len(num)
    for i in xrange(0, lenNum/2): # rounds down so sorts out problem with odd number of digits
        if num[i] != num[lenNum-i-1]:
            return False
    
    return True 


print("The highest palindrome is %s" %(findBiggestPalindromeXDigits(3)))