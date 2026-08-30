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


def full_stack(stack):
    """
    Determines whether memory is available.

    Returns:
        True if memory is unavailable.
        False if memory is available.
    """
    try:
        temp = StackNode(None)
        del temp
        return False
    except MemoryError:
        return True


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
    Pop and return the top data from the stack.

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
    Determines whether the stack is empty.

    Returns:
        True if empty.
        False if it contains data.
    """
    return stack.count == 0


def stack_count(stack):
    """
    Returns the number of elements in the stack.
    """
    return stack.count


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
    done = False
    stack = None

    # Create a stack
    stack = create_stack()

    if stack is None:
        print("Error: Unable to create stack.")
        return

    # Fill stack
    while not done:

        try:
            data = input("Enter a number: <EOF> to stop: ")

            # Convert input to integer
            data = int(data)

            # Check whether stack is full
            if full_stack(stack):
                done = True
            else:
                push_stack(stack, data)

        except EOFError:
            # Ctrl+D on Linux/macOS
            # Ctrl+Z then Enter on Windows
            done = True

        except ValueError:
            print("Please enter a valid integer.")

    # Print numbers in reverse
    print("\n\nThe list of numbers reversed:")

    while not empty_stack(stack):

        data = pop_stack(stack)

        if data is not None:
            print(f"{data:3d}")

    # Destroy stack
    destroy_stack(stack)


if __name__ == "__main__":
    main()