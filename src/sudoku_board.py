from typing import List


class SudokuBoard:
    def __init__(self, board: List[List[str]]):
        # Check if the board has the correct size
        if len(board) != 9 or any(len(row) != 9 for row in board):
            raise ValueError("Invalid Sudoku board size. It should be a 9x9 grid.")

        # Check if the cells contain valid values
        for row in board:
            for cell in row:
                if cell not in (".", "0") and (
                    not cell.isdigit() or int(cell) < 1 or int(cell) > 9
                ):
                    raise ValueError(
                        f"""Invalid cell value: {cell}. Only '.' or '0' for empty cells,
                         and digits from 1 to 9 are allowed."""
                    )

        self.board = board

    def __repr__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.board)
