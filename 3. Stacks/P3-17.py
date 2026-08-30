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
    Push data onto the stack.
    """
    new_node = StackNode(data)

    new_node.link = stack.top
    stack.top = new_node
    stack.count += 1

    return True


def pop_stack(stack):
    """
    Pop the top item from the stack.

    Returns:
        Data from the top node.
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


def empty_stack(stack):
    """
    Determines whether the stack is empty.
    """
    return stack.count == 0


def destroy_stack(stack):
    """
    Destroy all nodes in the stack.
    """

    while stack.top is not None:
        temp = stack.top
        stack.top = stack.top.link

        temp.data = None
        temp.link = None

        del temp

    stack.count = 0

    return None


def parse_parens(filename):
    """
    Reads a source program from a file and checks
    whether all opening and closing parentheses are paired.

    Pre:
        filename is the name of the source file.

    Post:
        Reports whether parentheses are correctly paired.
    """

    # Error messages
    clos_miss = "Close paren missing at line"
    open_miss = "Open paren missing at line"

    # Create stack
    stack = create_stack()

    # Start line count
    line_count = 1

    try:
        # Open source file
        with open(filename, "r") as file:

            # Read characters from source code
            for token in file.read():

                # Count lines
                if token == '\n':
                    line_count += 1

                # Opening parenthesis
                if token == '(':

                    # Push opening parenthesis onto stack
                    push_stack(stack, token)

                # Closing parenthesis
                elif token == ')':

                    # Check whether stack is empty
                    if empty_stack(stack):
                        print(f"{open_miss} {line_count}")

                        destroy_stack(stack)
                        return False

                    else:
                        # Remove matching opening parenthesis
                        pop_stack(stack)

        # Check for unmatched opening parentheses
        if not empty_stack(stack):
            print(f"{clos_miss} {line_count}")

            destroy_stack(stack)
            return False

        # Destroy stack
        destroy_stack(stack)

        print(f"Parsing is OK: {line_count} Lines parsed.")

        return True

    except FileNotFoundError:
        print(f"Error opening {filename}")
        return False


def main():
    """
    Main program.
    """

    print("Parentheses Parser")
    print("------------------")

    # Get filename
    file_id = input("Enter file ID for file to be parsed: ")

    # Parse file
    parse_parens(file_id)


if __name__ == "__main__":
    main()