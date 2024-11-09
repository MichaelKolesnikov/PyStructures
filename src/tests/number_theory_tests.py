import unittest
from olympiad_data_structures.number_theory.number_systems import convert_number_system

class TestConvertNumberSystem(unittest.TestCase):

    def test_binary_to_decimal(self):
        self.assertEqual(convert_number_system("1010", 2, 10), "10")

    def test_decimal_to_binary(self):
        self.assertEqual(convert_number_system("10", 10, 2), "1010")

    def test_hexadecimal_to_decimal(self):
        self.assertEqual(convert_number_system("A", 16, 10), "10")

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(convert_number_system("255", 10, 16), "FF")

    def test_custom_alphabet(self):
        self.assertEqual(convert_number_system("10", 10, 36), "A")

    def test_binary_to_octal(self):
        self.assertEqual(convert_number_system("1010", 2, 8), "12")

    def test_octal_to_binary(self):
        self.assertEqual(convert_number_system("12", 8, 2), "1010")

    def test_large_number(self):
        number_in_from_base = "1111111111111111111111111111111"
        right_answer = int(number_in_from_base, 2)
        self.assertEqual(convert_number_system(number_in_from_base, 2, 10), str(right_answer))

    def test_zero(self):
        self.assertEqual(convert_number_system("0", 10, 2), "0")

    def test_ege1(self):
        task_alphabet = "АКРУ"
        number_in_from_base = str(350 - 1)
        from_base = 10
        to_base = len(task_alphabet)
        right_answer = "КККУК"
        self.assertEqual(convert_number_system(number_in_from_base, from_base, to_base, task_alphabet), right_answer)

    def test_ege2(self):
        task_alphabet = "АКРУ"
        number_in_from_base = str(350 - 1)
        from_base = 10
        to_base = len(task_alphabet)
        right_answer = "КККУК"
        self.assertEqual(convert_number_system(number_in_from_base, from_base, to_base, task_alphabet), right_answer)

if __name__ == '__main__':
    unittest.main()