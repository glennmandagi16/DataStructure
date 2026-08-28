class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def create_node(item):
    """
    Creates a node and stores data in it.

    Pre:
        item is the data to be stored.

    Post:
        A node is created and returned.
    """
    node = Node(item)
    return node


# Main program
if __name__ == "__main__":
    data = 100

    node_ptr = create_node(data)

    print("Data:", node_ptr.data)
    print("Link:", node_ptr.link)