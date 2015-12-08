import unittest
import sys

sys.path.append('../src')
from python.src.primeUtilities import is_prime_sieve_eratosthenes, primes_in_range

class TestPrimeUtilities(unittest.TestCase):

    def test_is_prime_sieve_eratosthenes_detects_non_primes(self):
        self.assertFalse(is_prime_sieve_eratosthenes(1))
        self.assertFalse(is_prime_sieve_eratosthenes(4))
        self.assertFalse(is_prime_sieve_eratosthenes(9))
        self.assertFalse(is_prime_sieve_eratosthenes(15))

    def test_is_prime_sieve_eratosthenes_detects_primes(self):
        self.assertTrue(is_prime_sieve_eratosthenes(2))
        self.assertTrue(is_prime_sieve_eratosthenes(3))
        self.assertTrue(is_prime_sieve_eratosthenes(5))
        self.assertTrue(is_prime_sieve_eratosthenes(11))

    def test_prime_utilities_primes_in_range_find_primes_in_list(self):
        number_list = [1, 2, 3, 5, 8]
        number_list_primes = [2, 3, 5]
        self.assertEqual(number_list_primes, primes_in_range(number_list))

    def test_prime_utilities_primes_in_range_empty_list(self):
        number_list = []
        number_list_primes = []
        self.assertEqual(number_list_primes, primes_in_range(number_list))

    def test_prime_utilities_primes_in_range_duplicates(self):
        number_list = [1, 1, 2, 3, 3, 5, 8, 9, 9, 9, 11, 11]
        number_list_primes = [2, 3, 3, 5, 11, 11]
        self.assertEqual(number_list_primes, primes_in_range(number_list))


if __name__ == '__main__':
    unittest.main()