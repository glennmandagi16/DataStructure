def compare(ptr1, ptr2):
    """
    Integer specific compare function.

    Returns:
        1  if ptr1 >= ptr2
        -1 if ptr1 < ptr2
    """
    if ptr1 >= ptr2:
        return 1
    else:
        return -1


def larger(data_ptr1, data_ptr2, compare_function):
    """
    Compares two data values and returns the larger value.
    """
    if compare_function(data_ptr1, data_ptr2) > 0:
        return data_ptr1
    else:
        return data_ptr2


def main():
    # Local Definitions
    i = 7
    j = 8

    # Find the larger value
    lrg = larger(i, j, compare)

    # Print the result
    print("Larger value is:", lrg)


if __name__ == "__main__":
    main()