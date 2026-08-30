def post_fix_evaluate(expr):
    """
    A3-11: postFixEvaluate

    Evaluates a postfix expression and returns its value.

    Pre:
        expr is a valid postfix expression.

    Post:
        Postfix value computed.

    Return:
        Value of expression.
    """

    # Create stack
    stack = []

    # Loop for each character
    for character in expr:

        # If character is an operand
        if character.isdigit():

            # Push operand onto stack
            stack.append(int(character))

        # Character is an operator
        else:

            # Pop operand 2
            operand2 = stack.pop()

            # Pop operand 1
            operand1 = stack.pop()

            # Calculate value
            if character == '+':
                value = operand1 + operand2

            elif character == '-':
                value = operand1 - operand2

            elif character == '*':
                value = operand1 * operand2

            elif character == '/':
                value = operand1 // operand2

            # Push result onto stack
            stack.append(value)

    # Pop final result
    result = stack.pop()

    # Return result
    return result


# Main program
if __name__ == "__main__":

    print("Postfix Expression Evaluation")
    print("-----------------------------")

    expression = input("Input postfix expression: ")

    result = post_fix_evaluate(expression)

    print("The result is:", result)