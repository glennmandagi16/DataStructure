class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.count = 0
        self.top = None


def create_stack():
    """
    Create an empty stack.

    Returns:
        A new empty Stack object.
    """
    try:
        return Stack()
    except MemoryError:
        return None


def push_stack(stack, data_in):
    """
    Push data onto the stack.

    Returns:
        True if successful.
        False if memory allocation fails.
    """
    try:
        new_node = StackNode(data_in)

        new_node.link = stack.top
        stack.top = new_node
        stack.count += 1

        return True

    except MemoryError:
        return False


def pop_stack(stack):
    """
    Pop the top item from the stack.

    Returns:
        Top data if successful.
        None if stack is empty.
    """

    if stack.count == 0:
        return None

    temp = stack.top
    data_out = temp.data

    stack.top = temp.link
    stack.count -= 1

    del temp

    return data_out


def empty_stack(stack):
    """
    Check whether the stack is empty.

    Returns:
        True if empty.
        False otherwise.
    """

    return stack.count == 0


def destroy_stack(stack):
    """
    Destroy all nodes in the stack.
    """

    if stack is not None:

        while stack.top is not None:
            temp = stack.top
            stack.top = stack.top.link

            temp.data = None
            temp.link = None

            del temp

        stack.count = 0

    return None


def main():
    # Local Definitions
    num = 0
    digit = 0
    stack = None

    # Create Stack
    stack = create_stack()

    if stack is None:
        print("Error: Unable to create stack.")
        return

    # Prompt and read a number
    num = int(input("Enter an integer: "))

    # Create 0s and 1s and push them into the stack
    if num == 0:
        print("The binary number is : 0")
    else:
        while num > 0:

            # Get remainder
            digit = num % 2

            # Push digit into stack
            push_stack(stack, digit)

            # Divide number by 2
            num = num // 2

        # Binary number created. Now print it
        print("The binary number is : ", end="")

        while not empty_stack(stack):

            digit = pop_stack(stack)

            print(digit, end="")

        print()

    # Destroying Stack
    destroy_stack(stack)


if __name__ == "__main__":
    main()