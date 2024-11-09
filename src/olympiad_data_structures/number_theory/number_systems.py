from collections.abc import Sequence

from olympiad_data_structures.number_theory.exception.InvalidToAlphabetException import InvalidToAlphabetException


def convert_number_system(number_in_from_base: str, from_base: int, to_base: int, to_alphabet: Sequence[str] | None = None) -> str:
    default_alphabet = [chr(i) for i in range(ord('0'), ord('9') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    if to_alphabet is None:
        to_alphabet = default_alphabet
    if len(to_alphabet) < to_base:
        raise InvalidToAlphabetException(to_base, to_alphabet)

    number_in_10_base = 0
    k = 1 # from_base^0, from_base^1, from_base^2, ...
    for i in range(len(number_in_from_base) - 1, -1, -1):
        number_in_10_base += k * default_alphabet.index(number_in_from_base[i])
        k *= from_base

    answer = ""
    while number_in_10_base > 0:
        answer = to_alphabet[number_in_10_base % to_base] + answer
        number_in_10_base //= to_base
    if not answer:
        answer = '0'
    return answer
