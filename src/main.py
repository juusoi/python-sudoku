from sudoku_board import SudokuBoard
from sudoku_checker import SudokuChecker

# Example Sudoku board
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sudoku = SudokuBoard(board)


def check_sudoku(sudoku: SudokuBoard):
    sudoku_checker = SudokuChecker(sudoku)
    if sudoku_checker.is_valid_sudoku():
        print("Valid Sudoku")
    else:
        print("Invalid Sudoku")


if __name__ == "__main__":
    print(sudoku)
    check_sudoku(sudoku)
