class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.count = 0
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


def empty_stack(stack):
    """
    Determine if the stack is empty.

    Pre:
        stack is a valid stack metadata structure.

    Post:
        Returns the stack status.

    Returns:
        True if stack is empty.
        False if stack contains data.
    """

    # Check whether count is 0
    if stack.count == 0:
        return True
    else:
        return False


def main():
    # Create stack
    stack = Stack()

    # Check empty stack
    if empty_stack(stack):
        print("Stack is empty.")
    else:
        print("Stack contains data.")

    # Add data
    push_stack(stack, 10)
    push_stack(stack, 20)

    # Check stack again
    if empty_stack(stack):
        print("Stack is empty.")
    else:
        print("Stack contains data.")


if __name__ == "__main__":
    main()