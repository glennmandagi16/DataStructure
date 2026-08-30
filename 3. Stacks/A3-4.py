class Node:
    def __init__(self, data):
        # Store data in the node
        self.data = data

        # Link to the next node
        self.next = None


class Stack:
    def __init__(self):
        # Number of items in the stack
        self.count = 0

        # Top of the stack
        self.top = None


def push_stack(stack, data):
    """
    Push one item into the stack.
    """

    new_node = Node(data)

    # Make current top the second node
    new_node.next = stack.top

    # Make new node the top
    stack.top = new_node

    # Increment count
    stack.count += 1


def stack_top(stack):
    """
    Retrieve data from the top of the stack
    without changing the stack.

    Returns:
        (success, data)
        success = True if data is returned.
        success = False if stack is empty.
    """

    # 1. Check if stack is empty
    if stack.top is None:
        return False, None

    # 2. Get data from the top node
    data_out = stack.top.data

    # 3. Operation successful
    return True, data_out


def main():
    # Create stack
    stack = Stack()

    # Push data
    push_stack(stack, 10)
    push_stack(stack, 20)
    push_stack(stack, 30)

    print("Stack count before stackTop:", stack.count)

    # Retrieve top data without removing it
    success, data = stack_top(stack)

    if success:
        print("Top data:", data)
    else:
        print("Stack underflow!")

    # Verify that stack has not changed
    print("Stack count after stackTop:", stack.count)

    print("\nCurrent stack:")

    current = stack.top

    while current is not None:
        print(current.data)
        current = current.next


if __name__ == "__main__":
    main()