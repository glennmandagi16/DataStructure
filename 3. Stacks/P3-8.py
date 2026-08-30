class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.count = 0
        self.top = None


def push_stack(stack, data_in):
    """
    Push an item onto the stack.

    Pre:
        stack is a pointer to a valid stack.
        data_in contains data to be inserted.

    Post:
        Data is inserted into the stack.

    Returns:
        True if successful.
        False if memory allocation fails.
    """

    try:
        # Allocate/create a new node
        new_node = StackNode(data_in)

        # Link new node to current top
        new_node.link = stack.top

        # Make new node the new top
        stack.top = new_node

        # Increment stack count
        stack.count += 1

        return True

    except MemoryError:
        return False


def main():
    # Create an empty stack
    stack = Stack()

    # Push data
    success = push_stack(stack, 10)

    if success:
        print("Data 10 pushed successfully.")
    else:
        print("Push failed.")

    success = push_stack(stack, 20)

    if success:
        print("Data 20 pushed successfully.")
    else:
        print("Push failed.")

    success = push_stack(stack, 30)

    if success:
        print("Data 30 pushed successfully.")
    else:
        print("Push failed.")

    # Display stack
    print("\nStack count:", stack.count)
    print("Stack contents:")

    current = stack.top

    while current is not None:
        print(current.data)
        current = current.link


if __name__ == "__main__":
    main()