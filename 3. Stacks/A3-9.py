class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.count = 0
        self.top = None


def push_stack(stack, data):
    """Push data onto the stack."""
    new_node = StackNode(data)

    new_node.link = stack.top
    stack.top = new_node
    stack.count += 1


def pop_stack(stack):
    """Pop and return data from the top of the stack."""

    if stack.count == 0:
        return None

    temp = stack.top
    data_out = temp.data

    stack.top = temp.link
    stack.count -= 1

    del temp

    return data_out


def empty_stack(stack):
    """Return True if the stack is empty."""

    return stack.count == 0


def parse_parens(source):
    """
    Parse a source program and check whether
    all opening and closing parentheses are paired.

    Pre:
        source contains source program text.

    Post:
        Reports unmatched parentheses.
    """

    # Create an empty stack
    stack = Stack()

    # Loop through every character in the source
    for character in source:

        # Opening parenthesis
        if character == '(':
            push_stack(stack, character)

        # Closing parenthesis
        elif character == ')':

            # Closing parenthesis without matching opening parenthesis
            if empty_stack(stack):
                print("Error: Closing parenthesis not matched")
            else:
                # Remove matching opening parenthesis
                pop_stack(stack)

    # Check for unmatched opening parentheses
    if not empty_stack(stack):
        print("Error: Opening parenthesis not matched")
    else:
        print("Parentheses are correctly matched.")


def main():
    print("Parentheses Parser")
    print("------------------")

    source = input("Enter source program: ")

    parse_parens(source)


if __name__ == "__main__":
    main()