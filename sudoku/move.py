from typing import Tuple


class Move:
    def __init__(self, row: int, column: int, number: int) -> None:
        self.column = column
        self.row = row
        self.number = number

    @property
    def square(self) -> Tuple[int, int]:
        return self.row, self.column
