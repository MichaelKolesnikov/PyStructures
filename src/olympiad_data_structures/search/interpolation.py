class InterpolationSearcher:
    @staticmethod
    def interpolation_search_with_non_decreasing(sequence: list[int], key: int):
        left = 0
        right = len(sequence) - 1

        while sequence[left] < key < sequence[right]:
            middle = left + (key - sequence[left]) * (right - left) // (sequence[right] - sequence[left])
            if sequence[middle] < key:
                left = middle + 1
            elif sequence[middle] > key:
                right = middle - 1
            else:
                return middle

        if sequence[left] == key:
            return left
        elif sequence[right] == key:
            return right
        return -1

    @staticmethod
    def interpolation_search_with_non_increasing(sequence: list[int], key: int):
        left = 0
        right = len(sequence) - 1

        while sequence[right] < key < sequence[left]:
            middle = right - (key - sequence[right]) * (right - left) // (sequence[left] - sequence[right])
            if sequence[middle] < key:
                right = middle - 1
            elif sequence[middle] > key:
                left = middle + 1
            else:
                return middle

        if sequence[left] == key:
            return left
        elif sequence[right] == key:
            return right
        return -1

    @staticmethod
    def interpolation_search(sequence: list[int], key: int, non_decreasing: bool = True):
        if non_decreasing:
            return InterpolationSearcher.interpolation_search_with_non_decreasing(sequence, key)
        return InterpolationSearcher.interpolation_search_with_non_increasing(sequence, key)
