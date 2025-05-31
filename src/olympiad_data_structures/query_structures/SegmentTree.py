from collections.abc import Callable


class SegmentTree[T]:
    class Children:
        def __init__(self, left: int, right: int) -> None:
            self.left: int = left
            self.right: int = right

        @staticmethod
        def create_from_vertex_number(vertex_number: int):
            return SegmentTree.Children(2 * vertex_number + 1, 2 * vertex_number + 2)

    def __init__(self, array: list[T], f: Callable[[T, T], T]):
        self.n = len(array)
        self.array = array
        self.f = f
        self.t = [0] * (4 * self.n)
        self._build(0, 0, self.n)

    def _build(self, vertex_number: int, l: int, r: int) -> None:
        if l == r - 1:
            self.t[vertex_number] = self.array[l]
            return
        m = (l + r) // 2
        children = SegmentTree.Children.create_from_vertex_number(vertex_number)
        self._build(children.left, l, m)
        self._build(children.right, m, r)
        self.t[vertex_number] = self.f(self.t[children.left], self.t[children.right])

    def _ask(self, vertex_number: int, l: int, r: int, ask_l: int, ask_r: int) -> int:
        if r <= ask_l or ask_r <= l:
            return 0  # vertex is red
        if ask_l <= l and r <= ask_r:
            return self.t[vertex_number]  # vertex is green
        # vertex is yellow
        children = SegmentTree.Children.create_from_vertex_number(vertex_number)
        m = (l + r) // 2
        return self.f(
            self._ask(children.left, l, m, ask_l, ask_r),
            self._ask(children.right, m, r, ask_l, ask_r)
        )

    def _alter(self, vertex_number: int, l: int, r: int, position: int, value: T) -> None:
        if l == r - 1:
            self.t[vertex_number] = value
            return
        children = SegmentTree.Children.create_from_vertex_number(vertex_number)
        m = (l + r) // 2
        if position < m:
            self._alter(children.left, l, m, position, value)
        else:
            self._alter(children.right, m, r, position, value)
        self.t[vertex_number] = self.f(self.t[children.left], self.t[children.right])

    def ask_value_on(self, left: int, right: int) -> T:
        return self._ask(0, 0, self.n, left, right + 1)

    def change_value(self, position: int, value: T):
        self._alter(0, 0, self.n, position, value)
