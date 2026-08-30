class Position:
    """
    Stores the row and column position of a queen.
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col


class Stack:
    """
    Stack ADT used to store queen positions.
    """

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def count(self):
        return len(self.items)


def create_stack():
    """
    Creates an empty stack.
    """

    return Stack()


def destroy_stack(stack):
    """
    Destroys the stack.
    """

    stack.items.clear()


def get_size():
    """
    Gets the size of the chess board.
    """

    while True:

        try:
            board_size = int(
                input("Enter board size: ")
            )

            if board_size > 0:
                return board_size

            print("Board size must be greater than 0.")

        except ValueError:
            print("Please enter a valid integer.")


def guarded(board, row, col, board_size):
    """
    Determines whether the position is guarded
    by another queen.

    Returns:
        True  - position is guarded
        False - position is safe
    """

    # Check column
    for r in range(row):
        if board[r][col] == 1:
            return True

    # Check upper-left diagonal
    r = row - 1
    c = col - 1

    while r >= 0 and c >= 0:

        if board[r][c] == 1:
            return True

        r -= 1
        c -= 1

    # Check upper-right diagonal
    r = row - 1
    c = col + 1

    while r >= 0 and c < board_size:

        if board[r][c] == 1:
            return True

        r -= 1
        c += 1

    return False


def fill_board(stack, board_size):
    """
    Places queens on the chess board using
    backtracking and a stack.
    """

    # Create an empty board
    board = [
        [0 for _ in range(board_size)]
        for _ in range(board_size)
    ]

    row = 0

    while row < board_size:

        placed = False

        # Try every column in current row
        for col in range(board_size):

            if not guarded(
                board,
                row,
                col,
                board_size
            ):

                # Place queen
                board[row][col] = 1

                # Store position in stack
                position = Position(row, col)
                stack.push(position)

                row += 1
                placed = True

                break

        # No safe position found
        if not placed:

            # Backtrack
            if stack.is_empty():
                print("No solution exists.")
                return board

            position = stack.pop()

            board[position.row][position.col] = 0

            row = position.row

            # Try next column in previous row
            next_col = position.col + 1

            found_next = False

            while next_col < board_size:

                if not guarded(
                    board,
                    row,
                    next_col,
                    board_size
                ):

                    board[row][next_col] = 1

                    new_position = Position(
                        row,
                        next_col
                    )

                    stack.push(new_position)

                    row += 1

                    found_next = True
                    break

                next_col += 1

            if not found_next:
                continue

    # Save board information in stack object
    stack.board = board

    return board


def print_board(stack, board_size):
    """
    Prints the chess board and queen positions.
    """

    board = getattr(
        stack,
        "board",
        None
    )

    if board is None:
        print("Board is empty.")
        return

    print("\nChess Board")
    print("-----------")

    # Column numbers
    print("   ", end="")

    for col in range(board_size):
        print(f"{col + 1} ", end="")

    print()

    # Print rows
    for row in range(board_size):

        print(f"{row + 1:2} ", end="")

        for col in range(board_size):

            if board[row][col] == 1:
                print("Q ", end="")
            else:
                print(". ", end="")

        print()


def main():
    """
    Main program.
    """

    print("Eight Queens Program")
    print("====================")

    # Get board size
    board_size = get_size()

    # Create stack
    stack = create_stack()

    # Fill board
    fill_board(
        stack,
        board_size
    )

    # Print board
    print_board(
        stack,
        board_size
    )

    # Destroy stack
    destroy_stack(stack)

    print("\nWe hope you enjoyed Eight Queens.")


if __name__ == "__main__":
    main()