from math import sqrt


def is_prime(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    else:
        return True


def is_prime_RabinMiller(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True
