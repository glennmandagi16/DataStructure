class Queue:
    """
    Queue metadata structure.
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0


def create_queue():
    """
    ================= create_queue =================
    Creates and initializes queue structure.

    Pre:
        Nothing.

    Post:
        Queue metadata elements have been initialized.

    Return:
        Queue object.
    """

    # Allocate queue head
    queue = Queue()

    # Initialize queue
    queue.front = None
    queue.rear = None
    queue.count = 0

    return queue


def main():
    # Create queue
    queue = create_queue()

    print("Queue created successfully.")
    print(f"Front: {queue.front}")
    print(f"Rear: {queue.rear}")
    print(f"Count: {queue.count}")


if __name__ == "__main__":
    main()