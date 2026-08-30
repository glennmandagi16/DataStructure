class StackNode:
    def __init__(self, data):
        # Store character data
        self.data = data

        # Link to the next node
        self.link = None


def push(stack_top, char_in):
    """
    Inserts a node into linked-list stack.

    Pre:
        stack_top is the top of a valid stack.

    Post:
        char_in is inserted into the stack.

    Return:
        True if successful.
        False if memory allocation fails.
    """

    try:
        # Allocate/create a new node
        new_node = StackNode(char_in)

        # Link new node to the current top
        new_node.link = stack_top[0]

        # Make new node the new top
        stack_top[0] = new_node

        # Operation successful
        success = True

    except MemoryError:
        # Memory allocation failed
        success = False

    return success


def main():
    # Initialize stack
    stack_top = [None]

    # Push characters
    success = push(stack_top, 'A')

    if success:
        print("Push successful.")
    else:
        print("Push failed.")

    # Display top
    if stack_top[0] is not None:
        print("Top:", stack_top[0].data)


if __name__ == "__main__":
    main()