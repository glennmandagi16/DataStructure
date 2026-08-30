class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.count = 0
        self.top = None


def create_stack():
    """
    Creates and initializes an empty stack.
    """
    return Stack()


def push_stack(stack, data):
    """
    Pushes an item onto the stack.
    """
    new_node = StackNode(data)

    new_node.link = stack.top
    stack.top = new_node
    stack.count += 1

    return True


def pop_stack(stack):
    """
    Pops the item from the top of the stack.

    Returns:
        Top data if successful.
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


def stack_top(stack):
    """
    Retrieves data from the top of the stack
    without changing the stack.

    Returns:
        Top data if successful.
        None if stack is empty.
    """

    if stack.count == 0:
        return None

    return stack.top.data


def empty_stack(stack):
    """
    Determines whether the stack is empty.
    """
    return stack.count == 0


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


def priority(operator):
    """
    Returns the priority of an operator.

    Higher number = higher priority.
    """

    if operator in ("+", "-"):
        return 1

    elif operator in ("*", "/"):
        return 2

    elif operator == "^":
        return 3

    else:
        return 0


def is_operator(character):
    """
    Determines whether a character is an operator.
    """

    return character in "+-*/^"


def in_to_postfix(formula):
    """
    Converts an infix formula to postfix notation.

    Pre:
        formula is a valid infix expression.

    Post:
        Returns the postfix expression.
    """

    # Create stack
    stack = create_stack()

    # Initialize postfix expression
    post_fix_expr = ""

    # Process every character in formula
    for character in formula:

        # Ignore spaces
        if character.isspace():
            continue

        # Open parenthesis
        if character == '(':

            push_stack(stack, character)

        # Close parenthesis
        elif character == ')':

            # Pop operators until '(' is found
            while (
                not empty_stack(stack)
                and stack_top(stack) != '('
            ):
                token_out = pop_stack(stack)
                post_fix_expr += token_out

            # Remove '(' from stack
            if not empty_stack(stack):
                pop_stack(stack)

        # Operator
        elif is_operator(character):

            # Check operators already in stack
            while (
                not empty_stack(stack)
                and stack_top(stack) != '('
                and priority(character) <= priority(stack_top(stack))
            ):
                token_out = pop_stack(stack)
                post_fix_expr += token_out

            # Push current operator
            push_stack(stack, character)

        # Operand
        else:

            # Add operand directly to postfix expression
            post_fix_expr += character

    # Formula completely processed.
    # Pop remaining operators.
    while not empty_stack(stack):

        token_out = pop_stack(stack)

        # Avoid adding unmatched '('
        if token_out != '(':
            post_fix_expr += token_out

    # Destroy stack
    destroy_stack(stack)

    return post_fix_expr


def main():
    print("Infix to Postfix Conversion")
    print("---------------------------")

    formula = input("Enter an infix formula: ")

    postfix = in_to_postfix(formula)

    print("\nInfix formula :", formula)
    print("Postfix formula:", postfix)


if __name__ == "__main__":
    main()