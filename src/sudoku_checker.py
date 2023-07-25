from src.sudoku_board import SudokuBoard
from src.unit import Unit


class SudokuChecker:
    def __init__(self, sudoku_board: SudokuBoard):
        self.board = sudoku_board.board

    def is_valid_sudoku(self) -> bool:
        if not self.board or not self.is_valid_size():
            return False
        return all(
            [self.is_valid_row(), self.is_valid_column(), self.is_valid_square()]
        )

    def is_valid_row(self) -> bool:
        return all(Unit(row).is_valid() for row in self.board)

    def is_valid_column(self) -> bool:
        return all(
            Unit([self.board[row][col] for row in range(9)]).is_valid()
            for col in range(9)
        )

    def is_valid_square(self) -> bool:
        return all(
            Unit(
                [
                    self.board[row][col]
                    for row in range(i, i + 3)
                    for col in range(j, j + 3)
                ]
            ).is_valid()
            for i in range(0, 9, 3)
            for j in range(0, 9, 3)
        )

    def is_valid_size(self) -> bool:
        return len(self.board) == 9 and all(len(row) == 9 for row in self.board)
