'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from primeUtilities import is_prime

max_range = 1000000
sum = 0

for i in range(1, max_range, 2):
    if is_prime()