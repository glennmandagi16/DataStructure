def full_queue(queue):
    """
    ================= full_queue =================
    Determines if a queue is full.

    The queue is considered full if memory
    cannot be allocated for another node.

    Pre:
        queue is a metadata structure.

    Return:
        True if full.
        False if there is room for another node.
    """

    # Python manages memory automatically.
    # Normally the queue is not considered full.
    return False