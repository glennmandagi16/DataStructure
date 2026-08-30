class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # Number of elements in the stack
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


def stack_count(stack):
    """
    Return the number of elements currently in the stack.

    Pre:
        stack is a valid stack metadata structure.

    Post:
        Returns the number of elements in the stack.

    Returns:
        Integer count of elements in the stack.
    """

    # Return stack count
    return stack.count


def main():
    # Create stack
    stack = Stack()

    # Display initial count
    print("Initial stack count:", stack_count(stack))

    # Push data
    push_stack(stack, 10)
    print("After push 10:", stack_count(stack))

    push_stack(stack, 20)
    print("After push 20:", stack_count(stack))

    push_stack(stack, 30)
    print("After push 30:", stack_count(stack))


if __name__ == "__main__":
    main()