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
    """

    try:
        new_node = StackNode(data_in)

        # Link new node to current top
        new_node.link = stack.top

        # Make new node the top
        stack.top = new_node

        # Increment stack count
        stack.count += 1

        return True

    except MemoryError:
        return False


def stack_top(stack):
    """
    Retrieves data from the top of the stack
    without changing the stack.

    Pre:
        stack is a pointer to a valid stack.

    Post:
        Returns top data if successful.
        Returns None if stack is empty.
    """

    # Check whether stack is empty
    if stack.count == 0:
        return None

    # Return data from the top node
    return stack.top.data


def main():
    # Create stack
    stack = Stack()

    # Push data
    push_stack(stack, 10)
    push_stack(stack, 20)
    push_stack(stack, 30)

    print("Stack count before stackTop:", stack.count)

    # Get top data without removing it
    data = stack_top(stack)

    if data is not None:
        print("Top data:", data)
    else:
        print("Stack is empty.")

    # Verify that stack has not changed
    print("Stack count after stackTop:", stack.count)
    print("Current top:", stack.top.data)


if __name__ == "__main__":
    main()