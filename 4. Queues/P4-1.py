# ================= Queue ADT =================
# Queue ADT Type Definitions


class QueueNode:
    """
    Node structure for Queue ADT.

    C equivalent:

    typedef struct node
    {
        void* dataPtr;
        struct node* next;
    } QUEUE_NODE;
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """
    Queue metadata structure.

    C equivalent:

    typedef struct
    {
        QUEUE_NODE* front;
        QUEUE_NODE* rear;
        int count;
    } QUEUE;
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0


# ================= Function Definitions =================

def create_queue():
    """
    Creates and initializes an empty queue.

    Return:
        Queue object.
    """

    return Queue()


def destroy_queue(queue):
    """
    Deletes all nodes from the queue.

    Return:
        None.
    """

    while queue.front is not None:
        temp = queue.front
        queue.front = queue.front.next
        temp.next = None

    queue.rear = None
    queue.count = 0

    return None


def dequeue(queue):
    """
    Removes the front item from the queue.

    Return:
        Data if successful.
        None if queue is empty.
    """

    if empty_queue(queue):
        return None

    item = queue.front.data

    # If there is only one node
    if queue.front == queue.rear:
        queue.rear = None

    queue.front = queue.front.next
    queue.count -= 1

    return item


def enqueue(queue, item):
    """
    Inserts an item into the rear of the queue.

    Return:
        True if successful.
        False if queue is full.
    """

    if full_queue(queue):
        return False

    new_node = QueueNode(item)

    # If queue is empty
    if empty_queue(queue):
        queue.front = new_node
    else:
        queue.rear.next = new_node

    queue.rear = new_node
    queue.count += 1

    return True


def queue_front(queue):
    """
    Retrieves the item at the front
    without removing it.

    Return:
        Front data if successful.
        None if queue is empty.
    """

    if empty_queue(queue):
        return None

    return queue.front.data


def queue_rear(queue):
    """
    Retrieves the item at the rear
    without removing it.

    Return:
        Rear data if successful.
        None if queue is empty.
    """

    if empty_queue(queue):
        return None

    return queue.rear.data


def queue_count(queue):
    """
    Returns the number of elements in the queue.
    """

    return queue.count


def empty_queue(queue):
    """
    Determines whether the queue is empty.

    Return:
        True if empty.
        False if queue contains data.
    """

    return queue.count == 0


def full_queue(queue):
    """
    Determines whether the queue is full.

    Python manages memory automatically,
    so normally the queue is not full.

    Return:
        False.
    """

    return False