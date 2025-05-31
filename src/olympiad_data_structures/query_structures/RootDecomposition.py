from typing import Optional


class RootDecomposition:
    class Block:
        def __init__(self):
            self.block: list[int] = []
            self.result_of_operation: Optional[int] = None
            self.coefficient_not_yet_used: Optional[int] = None

        def __len__(self):
            return len(self.block)

        def _make_real_changes(self):
            if self.coefficient_not_yet_used is not None:
                for i in range(len(self)):
                    self.block[i] = ...
                ...

        def __getitem__(self, index):
            return self.block[index]

        def get_full_result(self):
            if self.coefficient_not_yet_used is None:
                return self.result_of_operation
            return ...

        def get_part_result_on(self, l: int, r: int):
            self._make_real_changes()
            ...

        def affect_entire_block(self, x):
            if self.coefficient_not_yet_used is None:
                self.coefficient_not_yet_used = x
                return
            self.coefficient_not_yet_used = ...

        def act_on_part_of_block(self, l: int, r: int, x) -> None:
            self._make_real_changes()
            for i in range(l, r + 1):
                self.block[i] = ...
            self.result_of_operation = ...

        def add_new_element(self, element):
            self.block.append(element)
            if len(self) == 1:
                self.result_of_operation = element
            else:
                self.result_of_operation = ...

    def __init__(self, array: list[int]):
        self.length = len(array)
        self.block_length = int(self.length**0.5)
        self.block_count = 0
        self.blocks: list[RootDecomposition.Block] = []
        for i in range(self.length):
            number_block_with_a_i = i // self.block_length
            if self.block_count == number_block_with_a_i:
                self.blocks.append(RootDecomposition.Block())
                self.block_count += 1
            self.blocks[number_block_with_a_i].add_new_element(array[i])

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        block_number = index // self.block_length
        position_in_block = index % self.block_length
        return self.blocks[block_number][position_in_block]

    def get_result_on(self):
        ...

    def act(self, l: int, r: int, x):
        ...
