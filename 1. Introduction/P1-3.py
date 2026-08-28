class Node:
    def __init__(self, data_ptr):
        self.data_ptr = data_ptr
        self.link = None


def create_node(item_ptr):
    """
    Creates a node and stores the data in it.

    Pre:
        item_ptr is the data to be stored.

    Post:
        A node is created and returned.
    """
    node_ptr = Node(item_ptr)
    return node_ptr


def main():
    # Local Definitions
    new_data = 7

    # Create a new node
    node = create_node(new_data)

    # Get data from the node
    node_data = node.data_ptr

    # Print data from node
    print("Data from node:", node_data)


if __name__ == "__main__":
    main()