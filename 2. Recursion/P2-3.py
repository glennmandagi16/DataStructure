OPERATORS = "+-*/"


def find_expr_len(expr_in):
    """
    Determine the length of the first expression
    in a prefix expression.

    Pre:
        expr_in contains a valid prefix expression.

    Post:
        Length of the expression is returned.
    """

    # Check if the first character is an operator
    if expr_in[0] in OPERATORS:

        # Find length of first expression
        len1 = find_expr_len(expr_in[1:])

        # Find length of second expression
        len2 = find_expr_len(expr_in[1 + len1:])

    else:
        # Base case: first character is an operand
        len1 = 0
        len2 = 0

    # Return length of expression
    return len1 + len2 + 1


def pre_to_post_fix(prefix_in):
    """
    Convert prefix expression to postfix format.

    Pre:
        prefix_in is a valid prefix expression.

    Post:
        Expression is converted to postfix.
    """

    # Base case: one character is an operand
    if len(prefix_in) == 1:
        return prefix_in

    # Get the operator
    operator = prefix_in[0]

    # Find the length of the first expression
    len_prefix = find_expr_len(prefix_in[1:])

    # Get the first expression
    temp1 = prefix_in[1:1 + len_prefix]

    # Convert first expression to postfix
    postfix1 = pre_to_post_fix(temp1)

    # Get the second expression
    temp2 = prefix_in[1 + len_prefix:]

    # Convert second expression to postfix
    postfix2 = pre_to_post_fix(temp2)

    # Concatenate postfix expressions and operator
    postfix = postfix1 + postfix2 + operator

    return postfix


def main():
    # Local Definitions
    prefix_expr = "-+*ABC/EF"

    # Convert prefix to postfix
    postfix_expr = pre_to_post_fix(prefix_expr)

    # Display results
    print("Begin prefix to postfix conversion")
    print()
    print("Prefix expr:", prefix_expr)
    print("Postfix expr:", postfix_expr)
    print()
    print("End prefix to postfix conversion")


if __name__ == "__main__":
    main()