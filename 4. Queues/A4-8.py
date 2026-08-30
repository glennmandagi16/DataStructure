def destroy_queue(queue):
    """
    ================= destroy_queue =================
    Deletes all data from a queue.

    Pre:
        queue is a metadata structure.

    Post:
        All data have been deleted.
    """

    # Delete all nodes
    while queue.front is not None:

        # Store the current front node
        temp = queue.front

        # Move front to the next node
        queue.front = queue.front.next

        # Remove reference to the deleted node
        temp.next = None

    # Reset rear
    queue.rear = None

    # Reset count
    queue.count = 0