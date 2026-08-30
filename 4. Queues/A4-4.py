def queue_front(queue):
    """
    ================= queue_front =================
    Retrieves data at the front of the queue
    without changing queue contents.

    Pre:
        queue is a metadata structure.

    Post:
        Data at the front is returned.

    Return:
        Front data if successful.
        None if underflow.
    """

    # Check if queue is empty
    if queue.count == 0:
        return None

    # Get data from front
    data_out = queue.front.data

    return data_out