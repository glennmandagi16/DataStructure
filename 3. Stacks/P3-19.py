class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.count = 0
        self.top = None


# ================= createStack =================
def create_stack():
    """
    Creates and initializes an empty stack.
    """

    return Stack()


# ================= pushStack =================
def push_stack(stack, data):
    """
    Pushes an item onto the stack.
    """

    new_node = StackNode(data)

    new_node.link = stack.top
    stack.top = new_node
    stack.count += 1

    return True


# ================= popStack =================
def pop_stack(stack):
    """
    Pops the item on the top of the stack.

    Returns:
        Data from the top of the stack.
        None if the stack is empty.
    """

    if stack.count == 0:
        return None

    temp = stack.top
    data_out = temp.data

    stack.top = temp.link
    stack.count -= 1

    del temp

    return data_out


# ================= stackTop =================
def stack_top(stack):
    """
    Retrieves data from the top of the stack
    without changing the stack.
    """

    if stack.count == 0:
        return None

    return stack.top.data


# ================= emptyStack =================
def empty_stack(stack):
    """
    Determines if the stack is empty.
    """

    return stack.count == 0


# ================= destroyStack =================
def destroy_stack(stack):
    """
    Releases all nodes in the stack.
    """

    while stack.top is not None:

        temp = stack.top
        stack.top = stack.top.link

        temp.data = None
        temp.link = None

        del temp

    stack.count = 0


# ================= isOperator =================
def is_operator(token):
    """
    Validates an operator.

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


# ================= calc =================
def calc(operand1, oper, operand2):
    """
    Given two values and an operator,
    determine the value of the formula.
    """

    if oper == '+':
        return operand1 + operand2

    elif oper == '-':
        return operand1 - operand2

    elif oper == '*':
        return operand1 * operand2

    elif oper == '/':
        return operand1 // operand2

    return 0


# ================= main =================
def main():

    # Local Definitions
    stack = create_stack()

    # Read postfix expression
    print("Postfix Expression Evaluation")
    print("-----------------------------")

    expression = input("Input formula: ")

    # Read postfix expression character by character
    for token in expression:

        # Character is operand
        if not is_operator(token):

            # Convert character to integer
            value = int(token)

            # Push operand onto stack
            push_stack(stack, value)

        # Character is operator
        else:

            # Get operand 2
            operand2 = pop_stack(stack)

            # Get operand 1
            operand1 = pop_stack(stack)

            # Calculate result
            value = calc(
                operand1,
                token,
                operand2
            )

            # Push result onto stack
            push_stack(stack, value)

    # Final result is in stack
    value = pop_stack(stack)

    # Print result
    print("The result is:", value)

    # Destroy stack
    destroy_stack(stack)


# ================= Program Start =================
if __name__ == "__main__":
    main()