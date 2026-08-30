class QueueNode:
    """
    Node for the queue.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """
    Queue metadata structure.
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0


def empty_queue(queue):
    """
    Determine whether the queue is empty.

    Return:
        True if empty.
        False if not empty.
    """

    return queue.count == 0


def full_queue(queue):
    """
    Determine whether the queue is full.

    Return:
        True if full.
        False if memory is available.
    """

    # Python manages memory automatically.
    return False


def enqueue(queue, data_in):
    """
    ================= enqueue =================
    This algorithm inserts data into a queue.

    Pre:
        queue is a metadata structure.

    Post:
        data_in has been inserted.

    Return:
        True if successful.
        False if overflow.
    """

    # 1. Check if queue is full
    if full_queue(queue):
        return False

    # 2. Allocate new node
    new_node = QueueNode(data_in)

    # 3. Move data into new node
    new_node.data = data_in

    # 4. Set new node next to None
    new_node.next = None

    # 5. Check if queue is empty
    if empty_queue(queue):

        # Inserting into empty queue
        queue.front = new_node

    else:

        # Point old rear to new node
        queue.rear.next = new_node

    # 6. Set rear to new node
    queue.rear = new_node

    # 7. Increment queue count
    queue.count += 1

    # 8. Return successful
    return True


def main():

    # Create queue
    queue = Queue()

    # Insert data
    enqueue(queue, 10)
    enqueue(queue, 20)
    enqueue(queue, 30)

    # Display queue information
    print("Queue created.")
    print(f"Count: {queue.count}")
    print(f"Front: {queue.front.data}")
    print(f"Rear: {queue.rear.data}")


if __name__ == "__main__":
    main()