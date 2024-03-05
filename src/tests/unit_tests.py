import unittest
from random import randint
from functools import reduce
from src.olympiad_data_structures.number_theory import EratosthenesSieve, Factorizer, gcd_lcm


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


class TestMathFunctions(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd_lcm.gcd(10, 25), 5)
        self.assertEqual(gcd_lcm.gcd(14, 28), 14)
        self.assertEqual(gcd_lcm.gcd(17, 23), 1)
        self.assertEqual(gcd_lcm.gcd(100, 75), 25)

    def test_lcm(self):
        self.assertEqual(gcd_lcm.lcm(10, 25), 50)
        self.assertEqual(gcd_lcm.lcm(14, 28), 28)
        self.assertEqual(gcd_lcm.lcm(17, 23), 391)
        self.assertEqual(gcd_lcm.lcm(100, 75), 300)

    def test_get_greatest_common_divisor(self):
        self.assertEqual(gcd_lcm.get_greatest_common_divisor(10, 25), 5)
        self.assertEqual(gcd_lcm.get_greatest_common_divisor(14, 28), 14)
        self.assertEqual(gcd_lcm.get_greatest_common_divisor(17, 23), 1)
        self.assertEqual(gcd_lcm.get_greatest_common_divisor(100, 75), 25)

    def test_get_greatest_common_multiple(self):
        self.assertEqual(gcd_lcm.get_greatest_common_multiple(10, 25), 50)
        self.assertEqual(gcd_lcm.get_greatest_common_multiple(14, 28), 28)
        self.assertEqual(gcd_lcm.get_greatest_common_multiple(17, 23), 391)
        self.assertEqual(gcd_lcm.get_greatest_common_multiple(100, 75), 300)

    def test_extended_euclidean_algorithm(self):
        self.assertEqual(gcd_lcm.extended_euclidean_algorithm(10, 25), (5, -2, 1))
        self.assertEqual(gcd_lcm.extended_euclidean_algorithm(14, 28), (14, 1, 0))
        self.assertEqual(gcd_lcm.extended_euclidean_algorithm(17, 23), (1, -4, 3))
        self.assertEqual(gcd_lcm.extended_euclidean_algorithm(100, 75), (25, 1, -1))


if __name__ == "__main__":
    unittest.main()
