def print_board(stack, board_size):
    """
    =================== print_board ====================
    Print positions of chess queens on a game board.

    Pre:
        stack contains positions of queens.
        board_size is the number of rows and columns.

    Post:
        Queen positions are printed.
    """

    # Check if stack is empty
    if stack.empty():
        print("There are no positions on this board")
        return

    print("\nPlace queens in following positions:")

    # Reverse stack for printing
    out_stack = Stack()

    while not stack.empty():
        pos = stack.pop()
        out_stack.push(pos)

    # Print board
    while not out_stack.empty():
        pos = out_stack.pop()

        print(
            f"Row {pos.row}-Col {pos.col}:\t|",
            end=""
        )

        for col in range(1, board_size + 1):

            if pos.col == col:
                print(" Q |", end="")
            else:
                print("   |", end="")

        print()

    # Destroy output stack
    out_stack.destroy()