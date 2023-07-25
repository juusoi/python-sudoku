def is_valid_sudoku(board: list) -> bool:
    if not board or not is_valid_size(board):
        return False
    return all([is_valid_row(board), is_valid_column(board), is_valid_square(board)])


def is_valid_row(board: list) -> bool:
    return all(is_valid_unit(row) for row in board)


def is_valid_column(board: list) -> bool:
    return all(is_valid_unit([board[row][col] for row in range(9)]) for col in range(9))


def is_valid_square(board: list) -> bool:
    return all(
        is_valid_unit(
            [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
        )
        for i in range(0, 9, 3)
        for j in range(0, 9, 3)
    )


def is_valid_size(board: list) -> bool:
    return len(board) == 9 and all(len(row) == 9 for row in board)


def is_valid_unit(unit: list) -> bool:
    seen = set()
    for cell in unit:
        if cell != ".":
            if cell in seen or not cell.isdigit() or int(cell) < 1 or int(cell) > 9:
                return False
            seen.add(cell)
    return True
