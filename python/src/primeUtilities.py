from math import sqrt
from math import floor


def is_prime(x):  # naive approach, return true if x is prime
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    else:
        return True


def is_prime_sieve_eratosthenes(x):
    if x == 1:
        return False
    if x < 4:
        return True
    if (x % 2) == 0:
        return False
    if x < 9:
        return True
    if (x % 3) == 0:
        return False
    else:
        r = floor(sqrt(x))
        f = 5
        while f <= r:
            if x % f == 0:
                return False
            if x % (f + 2) == 0:
                return False
            f += 6  # Primes take the form 6k +- 1
    return True  # all other cases


def is_prime_rabin_miller(a):  # return if x is prime using Rabin Miller method
    if a < 2:
        return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True


def primes_in_range(number_list):  # return a sub-set of range containing all the prime numbers in that range
    primes = []
    for number in number_list:
        if is_prime_sieve_eratosthenes(number):
            primes.append(number)
    return primes
