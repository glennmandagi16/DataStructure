class StackNode:
    def __init__(self, data):
        # Pointer to data
        self.data = data

        # Pointer to next node
        self.link = None


class Stack:
    def __init__(self):
        # Number of elements in stack
        self.count = 0

        # Top node of stack
        self.top = None