def is_operator(char):
    """
    Check whether a character is an operator.
    """
    return char in "+-*/"


def find_expr_len(expr_in):
    """
    Recursively determines the length of a prefix expression.

    Pre:
        expr_in is a valid prefix expression.

    Post:
        Length of the expression is returned.
    """

    # Check if the first character is an operator
    if is_operator(expr_in[0]):

        # Find length of first prefix expression
        len1 = find_expr_len(expr_in[1:])

        # Find length of second prefix expression
        len2 = find_expr_len(expr_in[1 + len1:])

    else:
        # Base case: first character is an operand
        len1 = 0
        len2 = 0

    # Return total length
    return len1 + len2 + 1


def main():
    # Prefix expression
    expr_in = "*+ABC"

    # Find expression length
    length = find_expr_len(expr_in)

    print("Prefix expression:", expr_in)
    print("Expression length:", length)


if __name__ == "__main__":
    main()