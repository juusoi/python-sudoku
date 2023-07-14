def solve_sudoku(board: list) -> list:
    if not board:
        return board

    solve(board)
    return board


def solve(board: list) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for num in range(1, 10):
                    if is_valid(board, row, col, str(num)):
                        board[row][col] = str(num)
                        if solve(board):
                            return True
                        else:
                            board[row][col] = "."
                return False
    return True


def is_valid(board: list, row: int, col: int, num: str) -> bool:
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
        if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num:
            return False
    return True
