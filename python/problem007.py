"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from primeUtilities import is_prime

primeToFind = 10001
counter = 1
primeCount = 1
primeNumber = 2

while (primeCount < primeToFind):
    counter+=2
    if (is_prime(counter)):
        primeCount+=1
        primeNumber = counter

print "Prime #", primeToFind, " is:",primeNumber
