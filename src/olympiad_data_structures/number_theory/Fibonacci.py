import math

from olympiad_data_structures.number_theory.binary_power import binary_power


class Fibonacci:
    @staticmethod
    def get_fibonacci_number_o1(n):
        sqrt5 = math.sqrt(5)
        return (
                binary_power(
                    (1 + sqrt5) / 2, n
                )
                -
                binary_power(
                    (1 - sqrt5) / 2, n
                )
        ) / sqrt5

    @staticmethod
    def get_fibonacci_number_o1_approximately(n):
        sqrt5 = math.sqrt(5)
        return (
                binary_power(
                    (1 + sqrt5) / 2, n
                )
        ) / sqrt5


