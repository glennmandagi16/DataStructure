# ================= create_queue =================
# Allocates and initializes a queue structure.
#
# Pre:
#     Nothing
#
# Post:
#     Queue has been allocated and initialized.
#
# Return:
#     Queue object if successful.


class Queue:
    def __init__(self):
        # Initialize front to None
        self.front = None

        # Initialize rear to None
        self.rear = None

        # Initialize count to 0
        self.count = 0


def create_queue():
    """
    Creates and initializes an empty queue.

    Return:
        Queue object.
    """

    queue = Queue()

    return queue