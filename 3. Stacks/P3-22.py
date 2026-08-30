def fill_board(stack, board_size):
    """
    =================== fill_board ====================
    Position chess queens on game board so that no queen
    can capture any other queen.

    Pre:
        board_size is the number of rows and columns
        on the board.

    Post:
        Queen positions are filled in the stack.
    """

    # Create an empty board
    # 0 = no queen
    # 1 = queen
    board = [
        [0 for _ in range(9)]
        for _ in range(9)
    ]

    # Initial position
    row = 1
    col = 0

    # Continue while there are rows to fill
    while row <= board_size:

        # Try columns in current row
        while col <= board_size and row <= board_size:

            # Move to next column
            col += 1

            # Check whether position is safe
            if not guarded(
                board,
                row,
                col,
                board_size
            ):

                # Place queen
                board[row][col] = 1

                # Create POSITION
                p_pos = Position(row, col)

                # Push position onto stack
                stack.push(p_pos)

                # Move to next row
                row += 1

                # Reset column
                col = 0

        # Backtracking
        while col >= board_size:

            # Pop previous queen position
            p_pos = stack.pop()

            # Restore previous row and column
            row = p_pos.row
            col = p_pos.col

            # Remove queen
            board[row][col] = 0

        # Continue
        # with the next available position

    return