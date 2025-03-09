import re


def get_arabic_value_of_roman_symbol(character: str) -> int:
    return {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }.get(character, 0)


def check_roman_numeral_correctness(roman_numeral: str) -> bool:
    return bool(re.fullmatch("M{,3}(?:D?(C{,3})|CM|C?D|)(?:L?(X{,3})|XC|X?L|)(?:V?(I{,3})|IX|I?V|)", roman_numeral))


def convert_roman_to_arabic(number: str) -> int:
    if not check_roman_numeral_correctness(number):
        return -1

    arabic_number = 0
    prev_arabic_value = float('inf')

    for i in range(len(number)):
        cur_arabic_value = get_arabic_value_of_roman_symbol(number[i])

        if prev_arabic_value >= cur_arabic_value:
            arabic_number += cur_arabic_value
        else:
            arabic_number += cur_arabic_value - 2 * prev_arabic_value

        prev_arabic_value = cur_arabic_value

    return arabic_number


def convert_arabic_to_roman(arabic_number: int) -> str:
    if not (0 < arabic_number < 4000):
        return ""

    result = []
    roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    arabic = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    for i in range(len(roman)):
        while arabic_number >= arabic[i]:
            result.append(roman[i])
            arabic_number -= arabic[i]
    return "".join(result)
