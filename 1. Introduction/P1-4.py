class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def create_node(item):
    node = Node(item)
    return node


def main():
    # Local Definitions
    new_data = 7

    # Create node 1
    node = create_node(new_data)

    # Create node 2
    new_data = 75
    node.link = create_node(new_data)

    # Get data from node 1
    node_data = node.data
    print("Data from node 1:", node_data)

    # Get data from node 2
    node_data = node.link.data
    print("Data from node 2:", node_data)


if __name__ == "__main__":
    main()