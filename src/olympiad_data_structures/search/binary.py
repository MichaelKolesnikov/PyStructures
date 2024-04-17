from typing import Callable, Protocol, Any, TypeVar


class BinarySearcher:
    @staticmethod
    def first_true(left: int, right: int, check: Callable[[int], bool]) -> int:
        # [left, right)
        if right <= left or not check(right - 1):
            return right
        right -= 1
        while left < right:
            m = (left + right) // 2
            if check(m):
                right = m
            else:
                left = m + 1
        return left

    @staticmethod
    def last_true(left: int, right: int, check: Callable[[int], bool]) -> int:
        # (left, right]
        if left >= right or not check(left + 1):
            return left
        left += 1
        while left < right:
            m = (left + right + 1) // 2
            if check(m):
                left = m
            else:
                right = m - 1
        return left

    @staticmethod
    def real_search(left: float, right: float, check: Callable[[float], bool], eps: float = 0.001, non_decreasing: bool = True):
        while left + eps < right:
            middle = (left + right) / 2
            check_res = check(middle)
            if check_res and non_decreasing or not check_res and not non_decreasing:
                right = middle
            else:
                left = middle
        return left
