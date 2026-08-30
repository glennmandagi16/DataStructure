class StackNode:
    def __init__(self, data):
        # Data stored in the node
        self.data = data

        # Link to the next node
        self.link = None


def push(stack, data_in):
    """
    Push data into the stack.

    Returns:
        True if successful.
        False if unsuccessful.
    """

    # Create a new node
    new_node = StackNode(data_in)

    # Link new node to current top
    new_node.link = stack[0]

    # Make new node the top
    stack[0] = new_node

    return True


def pop(stack):
    """
    Pop the top item from the stack.

    Returns:
        (True, data) if successful.
        (False, None) if stack is empty.
    """

    # Check if stack is empty
    if stack[0] is None:
        return False, None

    # Get data from top node
    data_out = stack[0].data

    # Move top to the next node
    stack[0] = stack[0].link

    return True, data_out


def insert_data(stack):
    """
    Insert data into the stack.
    """

    print("Enter characters to push onto the stack.")
    print("Enter '0' to stop.")

    while True:
        data = input("Enter data: ")

        if data == "0":
            break

        # Push only the first character
        push(stack, data[0])


def print_stack(stack):
    """
    Print all data currently in the stack.
    """

    print("\nStack contents:")

    current = stack[0]

    if current is None:
        print("Stack is empty.")
        return

    while current is not None:
        print(current.data)
        current = current.link


def main():
    # Beginning of program
    print("Beginning Simple Stack Program\n")

    # Stack top initially contains nothing
    p_stack_top = [None]

    # Insert data
    insert_data(p_stack_top)

    # Print stack
    print_stack(p_stack_top)

    print("\nEnd Simple Stack Program")


if __name__ == "__main__":
    main()