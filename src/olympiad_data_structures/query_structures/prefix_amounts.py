class PrefixAmounts1D:
    def __init__(self, container):
        assert hasattr(container, '__getitem__'), "Container must have operator []"
        assert hasattr(type(container[0]), '__add__'), "Type T must have operator +"

        self.prefix_amounts = [0] * len(container)
        self.prefix_amounts[0] = container[0]
        for i in range(1, len(container)):
            self.prefix_amounts[i] = self.prefix_amounts[i - 1] + container[i]

    def size(self):
        return len(self.prefix_amounts)

    def ask(self, left, right):
        return self.prefix_amounts[right] - (0 if left == 0 else self.prefix_amounts[left - 1])


class PrefixAmounts2D:
    def __init__(self, container):
        assert hasattr(container, '__getitem__'), "Container must have operator []"
        assert hasattr(container[0], '__getitem__'), "Container[0] must have operator []"
        assert hasattr(type(container[0][0]), '__add__'), "Type T must have operator +"
        self.n = len(container)
        self.m = len(container[0])
        self.prefix_amounts = [[0] * self.m for _ in range(self.n)]
        self.prefix_amounts[0][0] = container[0][0]
        for i in range(1, self.n):
            self.prefix_amounts[i][0] = self.prefix_amounts[i - 1][0] + container[i][0]
        for j in range(1, self.m):
            self.prefix_amounts[0][j] = self.prefix_amounts[0][j - 1] + container[0][j]
        for i in range(1, self.n):
            for j in range(1, self.m):
                self.prefix_amounts[i][j] = (container[i][j] +
                                             self.prefix_amounts[i - 1][j] +
                                             self.prefix_amounts[i][j - 1] -
                                             self.prefix_amounts[i - 1][j - 1])

    def size(self) -> tuple[int, int]:
        return self.n, self.m

    def ask(self, i_left: int, j_left: int, i_right: int, j_right):
        answer = self.prefix_amounts[i_right][j_right]
        if i_left == 0:
            if j_left == 0:
                return answer
            return answer - self.prefix_amounts[i_left][j_left - 1]
        if j_left == 0:
            return answer - self.prefix_amounts[i_left - 1][j_left]
        return (answer -
                self.prefix_amounts[i_left - 1][j_right] -
                self.prefix_amounts[i_right][j_left - 1] +
                self.prefix_amounts[i_left - 1][j_left - 1])

