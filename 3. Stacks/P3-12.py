def full_stack(stack):
    """
    Determines if the stack is full.

    In this implementation, "full" means
    that available memory is exhausted.

    Pre:
        stack is a valid Stack object.

    Returns:
        True  if memory is full.
        False if memory is available.
    """

    try:
        # Try to create a temporary node
        temp = StackNode(None)

        # Temporary node is no longer needed
        del temp

        return False

    except MemoryError:
        # Memory allocation failed
        return True