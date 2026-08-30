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

        # Increment count
        stack.count += 1

        return True

    except MemoryError:
        return False


def pop_stack(stack):
    """
    Pop the item on the top of the stack.

    Pre:
        stack is a pointer to a valid stack.

    Post:
        Returns data from the top if successful.
        Returns None if stack is empty.
    """

    # Check for underflow
    if stack.count == 0:
        return None

    # Save the top node
    temp = stack.top

    # Get data from the top node
    data_out = stack.top.data

    # Move top to the next node
    stack.top = stack.top.link

    # Delete reference to the old node
    del temp

    # Decrement stack count
    stack.count -= 1

    return data_out


def main():
    # Create stack
    stack = Stack()

    # Push data
    push_stack(stack, 10)
    push_stack(stack, 20)
    push_stack(stack, 30)

    print("Stack count before pop:", stack.count)

    # Pop data
    data = pop_stack(stack)

    if data is not None:
        print("Popped data:", data)
    else:
        print("Stack underflow.")

    print("Stack count after pop:", stack.count)

    # Display remaining stack
    print("\nRemaining stack:")

    current = stack.top

    while current is not None:
        print(current.data)
        current = current.link


if __name__ == "__main__":
    main()