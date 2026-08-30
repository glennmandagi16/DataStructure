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

    Pre:
        stack is passed by reference.
        data contains the data to be pushed.

    Post:
        data has been pushed onto the stack.
    """

    # 1. Allocate new node
    new_node = Node(data)

    # 2. Store data in new node
    # Data was stored when Node(data) was created.

    # 3. Make current top node the second node
    new_node.next = stack.top

    # 4. Make new node the top
    stack.top = new_node

    # 5. Increment stack count
    stack.count += 1


def main():
    # Create stack
    stack = Stack()

    # Push data into stack
    push_stack(stack, 10)
    push_stack(stack, 20)
    push_stack(stack, 30)

    # Display stack
    print("Stack:")
    
    current = stack.top

    while current is not None:
        print(current.data)
        current = current.next

    print("\nCount:", stack.count)


if __name__ == "__main__":
    main()