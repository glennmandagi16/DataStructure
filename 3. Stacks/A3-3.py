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

    # Allocate new node
    new_node = Node(data)

    # Make current top the second node
    new_node.next = stack.top

    # Make new node the top
    stack.top = new_node

    # Increment stack count
    stack.count += 1


def pop_stack(stack):
    """
    Pop the item from the top of the stack.

    Returns:
        (success, data)
        success = True if pop is successful.
        success = False if stack is empty.
    """

    # 1. Check if stack is empty
    if stack.top is None:
        return False, None

    # 2. Get data from the top node
    data_out = stack.top.data

    # 3. Make the second node the new top
    stack.top = stack.top.next

    # 4. Decrement stack count
    stack.count -= 1

    # 5. Operation successful
    return True, data_out


def main():
    # Create stack
    stack = Stack()

    # Push data
    push_stack(stack, 10)
    push_stack(stack, 20)
    push_stack(stack, 30)

    print("Initial stack:")
    current = stack.top

    while current is not None:
        print(current.data)
        current = current.next

    print("\nCount:", stack.count)

    # Pop data
    success, data = pop_stack(stack)

    if success:
        print("\nPopped data:", data)
    else:
        print("\nStack underflow!")

    print("\nStack after pop:")
    current = stack.top

    while current is not None:
        print(current.data)
        current = current.next

    print("\nCount:", stack.count)


if __name__ == "__main__":
    main()