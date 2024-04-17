import random
import unittest
from random import randint
from functools import reduce
from src.olympiad_data_structures.number_theory import EratosthenesSieve, Factorizer, gcd_lcm
from src.olympiad_data_structures.query_structures import sparse_table as st
from src.olympiad_data_structures.PointVector import PointVector
from src.olympiad_data_structures.search import BinarySearcher
from src.olympiad_data_structures.search import InterpolationSearcher
from typing import Callable


class TestBinarySearcher(unittest.TestCase):
    def test_first_true(self):
        for index in [randint(-100, 100) for _ in range(100)]:
            f: Callable[[int], bool] = lambda i: i >= index
            result = BinarySearcher.first_true(-101, 101, f)
            self.assertEqual(result, index)
        index = 105
        f: Callable[[int], bool] = lambda i: i >= index
        result = BinarySearcher.first_true(-101, 101, f)
        self.assertEqual(result, 101)

    def test_last_true(self):
        for index in [randint(-100, 100) for _ in range(100)]:
            f: Callable[[int], bool] = lambda i: i <= index
            result = BinarySearcher.last_true(-101, 101, f)
            self.assertEqual(result, index)
        index = -105
        f: Callable[[int], bool] = lambda i: i <= index
        result = BinarySearcher.last_true(-101, 101, f)
        self.assertEqual(result, -101)

    def test_non_decreasing_function(self):
        delta = 0.001
        for rand_real_number in [random.uniform(0, 90) for _ in range(50)]:
            def f(x):
                return x**3 >= rand_real_number

            result = BinarySearcher.real_search(-10, 10, f, eps=delta, non_decreasing=True)
            self.assertTrue(abs(rand_real_number**(1/3) - result) < delta)

    def test_non_increasing_function(self):
        delta = 0.001
        for rand_real_number in [random.uniform(0, 90) for _ in range(50)]:
            def f(x):
                return -x ** 3 >= rand_real_number

            result = BinarySearcher.real_search(-10, 10, f, eps=delta, non_decreasing=False)
            self.assertTrue(abs(-(rand_real_number ** (1 / 3)) - result) < delta)


class TestInterpolationSearcher(unittest.TestCase):
    def test_non_decreasing_sequence(self):
        sequence = [1, 3, 5, 7, 9, 11, 13, 15]
        key = 7
        result = InterpolationSearcher.interpolation_search(sequence, key)
        self.assertEqual(result, 3)

    def test_non_increasing_sequence(self):
        sequence = [15, 13, 11, 9, 7, 5, 3, 1]
        key = 7
        result = InterpolationSearcher.interpolation_search(sequence, key, non_decreasing=False)
        self.assertEqual(result, 4)

    def test_key_not_found(self):
        sequence = [2, 4, 6, 8, 10]
        key = 5
        result = InterpolationSearcher.interpolation_search(sequence, key)
        self.assertEqual(result, -1)


class TestPointVector(unittest.TestCase):

    def test_initialization(self):
        v = PointVector(1, 2, 3)
        self.assertEqual(len(v), 3)
        self.assertEqual(v.coordinates, [1, 2, 3])

    def test_addition(self):
        v1 = PointVector(1, 2, 3)
        v2 = PointVector(4, 5, 6)
        result = v1 + v2
        self.assertEqual(result.coordinates, [5, 7, 9])

    def test_subtraction(self):
        v1 = PointVector(1, 2, 3)
        v2 = PointVector(4, 5, 6)
        result = v2 - v1
        self.assertEqual(result.coordinates, [3, 3, 3])

    def test_scalar_multiplication(self):
        v = PointVector(1, 2, 3)
        result = v * 2
        self.assertEqual(result.coordinates, [2, 4, 6])

    def test_scalar_division(self):
        v = PointVector(2, 4, 6)
        result = v / 2
        self.assertEqual(result.coordinates, [1, 2, 3])

    def test_magnitude(self):
        v = PointVector(3, 4)
        self.assertEqual(v.magnitude(), 5)

    def test_normalize(self):
        v = PointVector(3, 4)
        normalized = v.normalize()
        self.assertAlmostEqual(normalized.magnitude(), 1.0)

    def test_dot_product(self):
        v1 = PointVector(1, 2, 3)
        v2 = PointVector(4, 5, 6)
        result = v1.dot_product(v2)
        self.assertEqual(result, 32)

    def test_cross_product(self):
        v1 = PointVector(1, 0, 0)
        v2 = PointVector(0, 1, 0)
        result = v1.cross_product(v2)
        self.assertEqual(result.coordinates, [0, 0, 1])


class TestEratosthenesSieve(unittest.TestCase):
    def test_prime(self) -> None:
        size = 10**7
        test_size = 10**2
        sieve = EratosthenesSieve(size)
        sieve.build()
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


class SparseTableTest(unittest.TestCase):
    def test_min_function(self):
        v = [1, 3, 2, 5, 4]
        sparse_table = st.SparseTableWithIdempotency(v, min)

        self.assertEqual(sparse_table.ask_value(1, 3), 2)
        self.assertEqual(sparse_table.ask_value(0, 4), 1)
        self.assertEqual(sparse_table.ask_value(2, 4), 2)

    def test_max_function(self):
        v = [1, 3, 2, 5, 4]
        sparse_table = st.SparseTableWithIdempotency(v, max)

        self.assertEqual(sparse_table.ask_value(1, 3), 5)
        self.assertEqual(sparse_table.ask_value(0, 4), 5)
        self.assertEqual(sparse_table.ask_value(2, 4), 5)

    def test_sum_function(self):
        v = [1, 3, 2, 5, 4]
        sparse_table = st.SparseTable(v, lambda a, b: a + b)

        self.assertEqual(sparse_table.ask_value(1, 3), 10)
        self.assertEqual(sparse_table.ask_value(0, 4), 15)
        self.assertEqual(sparse_table.ask_value(2, 4), 11)

    def test_mul_function(self):
        v = [1, 3, 2, 5, 4]
        sparse_table = st.SparseTable(v, lambda a, b: a * b)

        self.assertEqual(sparse_table.ask_value(1, 3), 30)
        self.assertEqual(sparse_table.ask_value(0, 4), 120)
        self.assertEqual(sparse_table.ask_value(2, 4), 40)


class SparseTableWithIdempotencyTest(unittest.TestCase):
    def test_gcd_function(self):
        v = [12, 18, 24, 36, 48]
        sparse_table = st.SparseTable(v, lambda a, b: gcd_lcm.get_greatest_common_divisor(a, b))

        self.assertEqual(sparse_table.ask_value(1, 3), 6)
        self.assertEqual(sparse_table.ask_value(0, 4), 6)
        self.assertEqual(sparse_table.ask_value(2, 4), 12)

    def test_lcm_function(self):
        v = [12, 18, 24, 36, 48]
        sparse_table = st.SparseTable(v, lambda a, b: gcd_lcm.lcm(a, b))

        self.assertEqual(sparse_table.ask_value(1, 3), 72)
        self.assertEqual(sparse_table.ask_value(0, 4), 144)
        self.assertEqual(sparse_table.ask_value(2, 4), 144)


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
