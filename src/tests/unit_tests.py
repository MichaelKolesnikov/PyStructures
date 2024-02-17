import unittest
from random import randint
from functools import reduce
from src.olympiad_data_structures.number_theory import EratosthenesSieve, Factorizer


class TestEratosthenesSieve(unittest.TestCase):
    def test_prime(self) -> None:
        size = 10**7
        test_size = 10**2
        sieve = EratosthenesSieve()
        sieve.build(size)
        test_numbers = [randint(1, size - 1) for _ in range(test_size)]
        for test_number in test_numbers:
            self.assertEqual(sieve.is_prime(test_number), sieve.is_prime_sqrt_method(test_number))


class TestFactorizer(unittest.TestCase):
    def test_factorization(self) -> None:
        size = 10**5
        test_size = 10**2
        factorizer = Factorizer()
        factorizer.build(size)
        test_numbers = [randint(1, size - 1) for _ in range(test_size)]
        for test_number in test_numbers:
            self.assertEqual(reduce(lambda x, y: x * y, factorizer.factorize(test_number), 1), test_number)


if __name__ == "__main__":
    unittest.main()
