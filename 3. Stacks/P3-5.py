class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


def push(stack_top, char_in):
    """
    Insert a character into the stack.
    """

    try:
        new_node = StackNode(char_in)

        # Link new node to current top
        new_node.link = stack_top[0]

        # Make new node the top
        stack_top[0] = new_node

        return True

    except MemoryError:
        return False


def pop(stack_top):
    """
    Remove and return the top character from the stack.

    Returns:
        (True, data) if successful.
        (False, None) if stack is empty.
    """

    # Check if stack is empty
    if stack_top[0] is None:
        return False, None

    # Get data from top node
    data_out = stack_top[0].data

    # Move top to the next node
    stack_top[0] = stack_top[0].link

    return True, data_out


def print_stack(stack_top):
    """
    Print a singly linked stack.

    Pre:
        stack_top is a pointer to a valid stack.

    Post:
        Data in stack is printed.
    """

    print("Stack contained: ", end="")

    # Pop and print every element
    while True:
        success, print_data = pop(stack_top)

        if not success:
            break

        print(print_data, end="")

    print()


def main():
    # Initialize stack
    stack_top = [None]

    # Push data
    push(stack_top, 'A')
    push(stack_top, 'B')
    push(stack_top, 'C')
    push(stack_top, 'D')
    push(stack_top, 'E')

    # Print stack
    print_stack(stack_top)

    # Check stack after printing
    if stack_top[0] is None:
        print("Stack is now empty.")


if __name__ == "__main__":
    main()