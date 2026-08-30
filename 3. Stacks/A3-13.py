class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def count(self):
        return len(self.items)


def create_board(board_size):
    """
    Creates an empty chess board.
    """

    return [
        [0 for _ in range(board_size)]
        for _ in range(board_size)
    ]


def guarded(board, row, col, board_size):
    """
    Determines whether a position is guarded
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


def print_board(board, board_size):
    """
    Prints the chess board.
    """

    print("\nChess Board")
    print("-----------")

    for row in range(board_size):

        for col in range(board_size):

            if board[row][col] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


def queens8(board_size):
    """
    Places queens on a chess board so that
    no queen can capture any other queen.

    Pre:
        board_size is the number of rows and columns.

    Post:
        A valid queen arrangement is printed.
    """

    # Create stack
    stack = Stack()

    # Create board
    board = create_board(board_size)

    # Start at first row
    row = 0

    # Start column
    col = -1

    # Continue until all rows are processed
    while row < board_size:

        # Try columns in current row
        col += 1

        while col < board_size and row < board_size:

            # Check whether position is safe
            if not guarded(board, row, col, board_size):

                # Place queen
                board[row][col] = 1

                # Push row-column position
                stack.push((row, col))

                # Move to next row
                row += 1

                # Start next row from first column
                col = -1

            else:

                # Try next column
                col += 1

        # If all columns have been tried
        # and there are still rows remaining,
        # backtrack.
        if row < board_size:

            while not stack.is_empty():

                # Remove previous queen
                previous_row, previous_col = stack.pop()

                board[previous_row][previous_col] = 0

                # Try next column from previous row
                row = previous_row
                col = previous_col

                col += 1

                if col < board_size:
                    break

    # Print board
    print_board(board, board_size)

    return


def main():

    print("Eight Queens Problem")
    print("--------------------")

    # Read board size
    board_size = int(
        input("Enter board size: ")
    )

    # Solve queens problem
    queens8(board_size)


if __name__ == "__main__":
    main()