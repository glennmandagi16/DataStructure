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


def destroy_stack(stack):
    """
    Delete all nodes from the stack.

    Pre:
        stack is passed by reference.

    Post:
        Stack is empty and all nodes are deleted.
    """

    # 1. If stack is not empty
    if stack.top is not None:

        # Loop while stack is not empty
        while stack.top is not None:

            # Delete the top node
            stack.top = stack.top.next

            # Decrement count
            stack.count -= 1

    # 2. Delete stack head
    # In Python, the object will be garbage collected
    stack.top = None
    stack.count = 0


def main():
    # Create stack
    stack = Stack()

    # Push some data
    push_stack(stack, 10)
    push_stack(stack, 20)
    push_stack(stack, 30)

    print("Before destroy:")
    print("Stack count:", stack.count)
    print("Top:", stack.top.data)

    # Destroy stack
    destroy_stack(stack)

    print("\nAfter destroy:")
    print("Stack count:", stack.count)
    print("Top:", stack.top)


if __name__ == "__main__":
    main()