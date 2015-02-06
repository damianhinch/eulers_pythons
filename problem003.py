# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 14:13:06 2015

Problem 3 

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: damianhinch
"""
####################################################
# Returns array of prime factors. Prime factor reduction
def highestPrimeFactor(inputNum):
    
    x = inputNum
    print('Finding the highest prime factor of:' + str(x))
    highestPrime = 0
    primeFactors = [1]
    if (x % 2 == 0 ):
        x = x/2                            
        primeFactors.append(2) 
    count = 3
    while count <= x:
        #print("Interation: %s" %(count))
        if x % count == 0:
            print("Factor found: %s" % (count))
            if is_prime(count) == True:
                x/=count # makes x smaller and hopefully makes finding later primes more viable
                primeFactors.append(count)
        count += 2
    
    print ("All primes: %s" %(primeFactors))
    highestPrime = primeFactors[-1]
    return highestPrime

####################################################

####################################################
#Calculates if a number is prime
def is_prime(n):
    print("Testing if %s is prime " %(n))
    if n <= 3:
        print(n >= 2)
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        print(False)
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            print(False)
            return False
            
    print(True)        
    return True
####################################################
#number = raw_input("Enter  number ")
#number = 13195
number = 600851475143
number2 = number * 123456789123456789
number3 = number ** 2  #approx 60 0s 

highestPFactor = highestPrimeFactor(number)
print("Highest prime of %s is : %s"  % (number, highestPFactor))
print("Highest prime of %s is : %s " % (number3, highestPrimeFactor(number3)))
#fin
