def is_operand(char):
    """
    Check whether a character is an operand.
    """
    return char.isalnum()


def find_expr_len(prefix):
    """
    Find the length of the first expression in a prefix expression.
    """

    # Base case: one character is an operand
    if len(prefix) == 1:
        return 1

    # If the first character is an operand,
    # the first expression has length 1
    if is_operand(prefix[0]):
        return 1

    # The first character is an operator.
    # Find the length of the first operand/expression.
    first_length = find_expr_len(prefix[1:])

    # Find the length of the second expression
    second_length = find_expr_len(prefix[1 + first_length:])

    # Operator + first expression + second expression
    return 1 + first_length + second_length


def pre_to_postfix(prefix_in):
    """
    Convert a prefix expression to a postfix expression.

    Pre:
        prefix_in is a valid prefix expression.

    Post:
        Returns the converted postfix expression.
    """

    # Base case: one character is an operand
    if len(prefix_in) == 1:
        return prefix_in

    # First character must be an operator
    operator = prefix_in[0]

    # Find the length of the first expression
    length_of_expr = find_expr_len(prefix_in[1:])

    # Get the first expression
    temp1 = prefix_in[1:1 + length_of_expr]

    # Convert first expression to postfix
    postfix1 = pre_to_postfix(temp1)

    # Get the second expression
    temp2 = prefix_in[1 + length_of_expr:]

    # Convert second expression to postfix
    postfix2 = pre_to_postfix(temp2)

    # Concatenate postfix expressions and operator
    postfix = postfix1 + postfix2 + operator

    return postfix


def main():
    # Prefix expression
    prefix_in = "*+ABC"

    # Convert prefix to postfix
    postfix = pre_to_postfix(prefix_in)

    # Display result
    print("Prefix expression :", prefix_in)
    print("Postfix expression:", postfix)


if __name__ == "__main__":
    main()