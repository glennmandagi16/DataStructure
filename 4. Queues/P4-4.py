# ================= dequeue =================
# This algorithm deletes a node from the queue.
#
# Pre:
#     queue has been created.
#
# Post:
#     Data from the queue front is returned
#     and the front element is deleted.
#
# Return:
#     Data if successful.
#     None if underflow.


def dequeue(queue):
    """
    Deletes the front node from the queue.

    Return:
        Data pointer if successful.
        None if underflow.
    """

    # Check if queue is empty
    if queue.count == 0:
        return None

    # Get data from the front node
    item = queue.front.data

    # Store the node that will be deleted
    delete_loc = queue.front

    # If there is only one item in the queue
    if queue.count == 1:

        # Queue becomes empty
        queue.rear = None
        queue.front = None

    else:

        # Move front to the next node
        queue.front = queue.front.next

    # Decrease queue count
    queue.count -= 1

    # Python automatically handles memory cleanup.
    delete_loc = None

    return item