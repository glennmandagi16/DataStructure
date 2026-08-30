class Stack:
    def __init__(self):
        # Set count to 0
        self.count = 0

        # Set top to None
        self.top = None


def create_stack():
    """
    Creates and initializes the stack.

    Pre:
        Nothing.

    Post:
        Stack structure created and initialized.

    Returns:
        Stack head.
    """

    # Allocate memory for stack head
    stack_head = Stack()

    # Return stack head
    return stack_head


def main():
    # Create and initialize stack
    stack = create_stack()

    # Display stack information
    print("Stack created successfully.")
    print("Count:", stack.count)
    print("Top:", stack.top)


if __name__ == "__main__":
    main()