# ================= enqueue =================
# This algorithm inserts data into a queue.
#
# Pre:
#     queue has been created.
#
# Post:
#     data have been inserted.
#
# Return:
#     True if successful.
#     False if overflow.


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def enqueue(queue, item):
    """
    Insert an item into the queue.
    """

    # Allocate new node
    # In Python, object creation replaces malloc().
    try:
        new_ptr = QueueNode(item)
    except MemoryError:
        return False

    # Store data in new node
    new_ptr.data = item

    # Set next pointer to None
    new_ptr.next = None

    # If queue is empty
    if queue.count == 0:
        # Inserting into empty queue
        queue.front = new_ptr
    else:
        # Connect old rear to new node
        queue.rear.next = new_ptr

    # Increment queue count
    queue.count += 1

    # Set new node as rear
    queue.rear = new_ptr

    return True