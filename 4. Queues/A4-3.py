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

    Python manages memory automatically,
    so this normally returns False.
    """

    return False


def enqueue(queue, data_in):
    """
    Insert data into the queue.
    """

    # Check if queue is full
    if full_queue(queue):
        return False

    # Create new node
    new_node = QueueNode(data_in)

    # If queue is empty
    if empty_queue(queue):
        queue.front = new_node

    else:
        # Connect old rear to new node
        queue.rear.next = new_node

    # Set new node as rear
    queue.rear = new_node

    # Increment count
    queue.count += 1

    return True


def dequeue(queue):
    """
    ================= dequeue =================
    This algorithm deletes a node from a queue.

    Pre:
        queue is a metadata structure.

    Post:
        Data at the queue front is returned
        and the front element is deleted.

    Return:
        Data if successful.
        None if underflow.
    """

    # 1. If queue is empty
    if empty_queue(queue):
        return None

    # 2. Get data from front node
    item = queue.front.data

    # 3. If there is only one node
    if queue.front == queue.rear:
        queue.rear = None

    # 4. Move front to next node
    queue.front = queue.front.next

    # 5. Decrement queue count
    queue.count -= 1

    # 6. Return data
    return item


def main():

    # Create queue
    queue = Queue()

    # Enqueue data
    enqueue(queue, 10)
    enqueue(queue, 20)
    enqueue(queue, 30)

    print("Queue:")
    print(f"Count: {queue.count}")
    print(f"Front: {queue.front.data}")
    print(f"Rear: {queue.rear.data}")

    # Dequeue data
    item = dequeue(queue)
    print(f"\nDequeued: {item}")

    item = dequeue(queue)
    print(f"Dequeued: {item}")

    print(f"Remaining count: {queue.count}")


if __name__ == "__main__":
    main()