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
    #print('Finding the highest prime factor of:' + str(x))
    highestPrime = 0
    primeFactors = [1]
    if (x % 2 == 0 ):
        x = x/2                            
        primeFactors.append(2) 
    count = 3
    while count <= x:
        #print("Interation: %s" %(count))
        if x % count == 0:
            #print("Factor found: %s" % (count))
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
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
####################################################
    
####################################################
# Returns array of prime factors. Prime factor reduction but going backwards
def highestPrimeFactorBackwards(inputNum):
    
    x = inputNum
    highestPrime = 0
    if (x % 2 == 0 ):
        x = x/2                            
    count = x
    found = False
    while count >= 3 and found == False:
        if x % count == 0:
            if is_prime(count) == True:
                highestPrime = count
                found = True
        count -= 2
    
    return highestPrime

####################################################

import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0)
        return ret
    return wrap

@timing
def do_work(number):
  highestPFactor = highestPrimeFactor(number)
  print("Highest prime of %s is : %s"  % (number, highestPFactor))

@timing
def do_work_backwards(number):
    highestPFactor = highestPrimeFactorBackwards(number)
    print("Highest prime of %s is : %s (using backwards)"  % (number, highestPFactor))

numberBack1 = 9
numberBackTurn = 160 #This is where the tide turns and fowards becomes slower (what is the reasoan for this random number!!??)
numberBack2 = 13195
numberOfDeath = 600851475143

do_work(numberBack1)
do_work_backwards(numberBack1)
do_work(numberBackTurn)
do_work_backwards(numberBackTurn)
do_work(numberBack2)
do_work_backwards(numberBack2)
#Backwards won't finish
do_work(numberOfDeath)
print("Is that all ya got?")
#do_work_backwards(numberOfDeath)
do_work(numberOfDeath * 200)
do_work(numberOfDeath ** 2)
#do_work(numberOfDeath ** 4)

