'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from primeUtilities import primes_in_range

max_range = 2000000
sum = 0

number_list = range(1, max_range)
number_list_prime = primes_in_range(number_list)
sum = 0
for prime in number_list_prime:
    sum += prime
print(sum)
