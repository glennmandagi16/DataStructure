class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        # Initialize stack count
        self.count = 0

        # Initialize top as None
        self.top = None


def create_stack():
    """
    Create an empty stack.

    Pre:
        Nothing.

    Post:
        Returns an empty stack.
    """

    try:
        # Create a new Stack object
        stack = Stack()

        return stack

    except MemoryError:
        # Memory allocation failed
        return None


def main():
    # Create an empty stack
    stack = create_stack()

    if stack is not None:
        print("Stack created successfully.")
        print("Stack count:", stack.count)
        print("Stack top:", stack.top)
    else:
        print("Error: Unable to create stack.")


if __name__ == "__main__":
    main()