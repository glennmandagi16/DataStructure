def guarded(board, chk_row, chk_col, board_size):
    """
    ===================== guarded ======================
    Checks rows, columns, and diagonals for guarding
    queens.

    Pre:
        board contains current positions for queens.
        chk_row and chk_col are the position for the
        new queen.
        board_size is the number of rows and columns
        in the board.

    Post:
        Returns True if the position is guarded.
        Returns False if the position is not guarded.
    """

    # Local Definitions
    row = 0
    col = 0

    # Check current column for a queen
    col = chk_col

    for row in range(1, chk_row + 1):
        if board[row][col] == 1:
            return True

    # Check diagonal right-up
    row = chk_row - 1
    col = chk_col + 1

    while row > 0 and col <= board_size:
        if board[row][col] == 1:
            return True

        row -= 1
        col += 1

    # Check diagonal left-up
    row = chk_row - 1
    col = chk_col - 1

    while row > 0 and col > 0:
        if board[row][col] == 1:
            return True

        row -= 1
        col -= 1

    # No queen is guarding this position
    return False