import random


class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


def push(stack, data_in):
    """
    Push data into the stack.

    Returns:
        True if successful.
        False if unsuccessful.
    """

    try:
        # Create a new node
        new_node = StackNode(data_in)

        # Link new node to current top
        new_node.link = stack[0]

        # Make new node the top
        stack[0] = new_node

        return True

    except MemoryError:
        return False


def insert_data(stack):
    """
    Create random character data and insert
    them into a linked-list stack.

    Pre:
        stack is a reference to the top node.

    Post:
        Stack has been created with 10 characters.
    """

    print("Creating characters: ", end="")

    # Create 10 nodes
    for node_count in range(10):

        # Generate uppercase character
        char_in = chr(random.randint(0, 25) + ord('A'))

        # Display generated character
        print(char_in, end="")

        # Push character into stack
        success = push(stack, char_in)

        # Check whether push was successful
        if not success:
            print("\nError 100: Out of Memory")
            exit(100)

    print()


def print_stack(stack):
    """
    Print all elements in the stack.
    """

    print("\nStack contents:")

    current = stack[0]

    while current is not None:
        print(current.data)
        current = current.link


def main():
    print("Beginning Simple Stack Program\n")

    # Initialize stack top
    stack_top = [None]

    # Insert random data
    insert_data(stack_top)

    # Display stack
    print_stack(stack_top)

    print("\nEnd Simple Stack Program")


if __name__ == "__main__":
    main()