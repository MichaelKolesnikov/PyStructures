from collections.abc import Sequence

from olympiad_data_structures.exception.olympiad_data_structures_exception import OlympiadDataStructuresException


class InvalidToAlphabetException(OlympiadDataStructuresException):
    def __init__(self, to_base: int, to_alphabet: Sequence[str]):
        super().__init__(f"Base: {to_base}, alphabet: {to_alphabet}")
