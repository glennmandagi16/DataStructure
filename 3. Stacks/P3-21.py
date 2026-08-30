def get_size():
    """
    ===================== get_size ======================
    Prompt user for a valid board size.

    Pre:
        Nothing

    Post:
        Valid board size returned.
    """

    print(
        "Welcome to Eight Queens. You may select\n"
        "a board size from 4 x 4 to 8 x 8. I will\n"
        "then position a queen in each row of the\n"
        "board so no queen may capture another\n"
        "queen. Note: There are no solutions for\n"
        "boards less than 4 x 4.\n"
    )

    # Ask for board size
    board_size = int(
        input("Please enter the board size: ")
    )

    # Validate board size
    while board_size < 4 or board_size > 8:

        print(
            "Board size must be greater than 3 "
            "and less than 9."
        )

        print(
            f"You entered {board_size}."
        )

        print(
            "Please re-enter. Thank you.\n"
        )

        board_size = int(
            input("Your board size: ")
        )

    return board_size