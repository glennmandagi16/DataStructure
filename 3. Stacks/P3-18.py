class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.count = 0
        self.top = None


# ================= create_stack =================
def create_stack():
    """
    Creates and initializes an empty stack.

    Returns:
        Stack object
    """
    return Stack()


# ================= push_stack =================
def push_stack(stack, data):
    """
    Pushes data onto the stack.

    Returns:
        True if successful
        False if memory allocation fails
    """

    try:
        new_node = StackNode(data)

        new_node.link = stack.top
        stack.top = new_node
        stack.count += 1

        return True

    except MemoryError:
        return False


# ================= pop_stack =================
def pop_stack(stack):
    """
    Pops the top item from the stack.

    Returns:
        Data from the top of the stack.
        None if stack is empty.
    """

    if stack.count == 0:
        return None

    temp = stack.top
    data_out = temp.data

    stack.top = temp.link
    stack.count -= 1

    del temp

    return data_out


# ================= stack_top =================
def stack_top(stack):
    """
    Retrieves data from the top of the stack
    without changing the stack.

    Returns:
        Top data.
        None if stack is empty.
    """

    if stack.count == 0:
        return None

    return stack.top.data


# ================= empty_stack =================
def empty_stack(stack):
    """
    Determines if the stack is empty.
    """

    return stack.count == 0


# ================= destroy_stack =================
def destroy_stack(stack):
    """
    Destroys all nodes in the stack.
    """

    while stack.top is not None:
        temp = stack.top
        stack.top = stack.top.link

        temp.data = None
        temp.link = None

        del temp

    stack.count = 0

    return None


# ================= priority =================
def priority(token):
    """
    Determines priority of an operator.

    Returns:
        2 for * and /
        1 for + and -
        0 for other characters
    """

    if token == '*' or token == '/':
        return 2

    if token == '+' or token == '-':
        return 1

    return 0


# ================= is_operator =================
def is_operator(token):
    """
    Determines whether token is an operator.

    Returns:
        True if token is an operator.
        False otherwise.
    """

    if (token == '*' or
            token == '/' or
            token == '+' or
            token == '-'):

        return True

    return False


# ================= main =================
def main():

    # Local Definitions
    postfix = ""
    stack = None

    # Create Stack
    stack = create_stack()

    # Read infix formula
    formula = input("Enter an infix formula: ")

    # Parse formula character by character
    for token in formula:

        # Opening parenthesis
        if token == '(':

            push_stack(stack, token)

        # Closing parenthesis
        elif token == ')':

            data = pop_stack(stack)

            while data != '(':

                postfix += data

                data = pop_stack(stack)

        # Operator
        elif is_operator(token):

            # Check priority of operator at stack top
            data = stack_top(stack)

            while (
                not empty_stack(stack)
                and priority(token) <= priority(data)
            ):

                data = pop_stack(stack)

                postfix += data

                data = stack_top(stack)

            # Push current operator
            push_stack(stack, token)

        # Character is operand
        else:

            postfix += token

    # Infix formula empty.
    # Pop remaining operators into postfix
    while not empty_stack(stack):

        data = pop_stack(stack)
        postfix += data

    # Print postfix formula
    print("The postfix formula is:", postfix)

    # Destroy stack
    destroy_stack(stack)


# ================= Program Start =================
if __name__ == "__main__":
    main()