def is_valid_sudoku(board: list) -> bool:
    if not is_valid_size(board):
        return False

    if not is_valid_row(board):
        return False

    if not is_valid_column(board):
        return False

    if not is_valid_square(board):
        return False

    return True


def is_valid_row(board: list) -> bool:
    for row in board:
        if not is_valid_unit(row):
            return False
    return True


def is_valid_column(board: list) -> bool:
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_unit(column):
            return False
    return True


def is_valid_square(board: list) -> bool:
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
            if not is_valid_unit(square):
                return False
    return True


def is_valid_size(board: list) -> bool:
    if len(board) != 9:
        return False

    for row in board:
        if len(row) != 9:
            return False

    return True


def is_valid_unit(unit: list) -> bool:
    seen = set()
    for cell in unit:
        if cell != ".":
            if cell in seen or not cell.isdigit() or int(cell) < 1 or int(cell) > 9:
                return False
            seen.add(cell)
    return True
