class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, capacity):
        # Number of items in the stack
        self.count = 0

        # Top of the stack
        self.top = None

        # Maximum capacity of the stack
        self.capacity = capacity


def push_stack(stack, data):
    """
    Push one item into the stack.
    """

    # Check if stack is full
    if full_stack(stack):
        print("Stack is full. Cannot push", data)
        return False

    # Create new node
    new_node = Node(data)

    # Make current top the second node
    new_node.next = stack.top

    # Make new node the top
    stack.top = new_node

    # Increment count
    stack.count += 1

    return True


def full_stack(stack):
    """
    Determine if the stack is full.

    Pre:
        stack is a valid stack metadata structure.

    Post:
        Returns the stack status.

    Returns:
        True if stack is full.
        False if memory/capacity is available.
    """

    # Check whether stack has reached its capacity
    if stack.count >= stack.capacity:
        return True
    else:
        return False


def main():
    # Create stack with maximum capacity of 3
    stack = Stack(3)

    # Push data
    push_stack(stack, 10)
    push_stack(stack, 20)
    push_stack(stack, 30)

    # Check whether stack is full
    if full_stack(stack):
        print("Stack is full.")
    else:
        print("Stack is not full.")

    # Try to push another item
    push_stack(stack, 40)


if __name__ == "__main__":
    main()