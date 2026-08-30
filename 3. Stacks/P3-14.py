def destroy_stack(stack):
    """
    Releases all nodes in the stack.

    Pre:
        stack is a valid Stack object.

    Post:
        All nodes are removed.
        Stack is destroyed.

    Returns:
        None
    """

    if stack is not None:

        # Delete all nodes in the stack
        while stack.top is not None:

            # Save current top node
            temp = stack.top

            # Move top to the next node
            stack.top = stack.top.link

            # Remove references from the old node
            temp.link = None
            temp.data = None

            # Decrement count
            stack.count -= 1

            # Remove reference to the node
            del temp

        # Stack is now empty
        stack.count = 0

        # Destroy stack object
        del stack

    return None