def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False

    # Check 3x3 squares
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            square = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
            if not is_valid_set(square):
                return False

    return True


def is_valid_set(nums):
    nums = [n for n in nums if n != "."]
    return len(nums) == len(set(nums))
