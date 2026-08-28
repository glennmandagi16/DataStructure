def compare(ptr1, ptr2):
    """
    Float specific compare function.

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
    Returns the larger value using the compare function.
    """
    if compare_function(data_ptr1, data_ptr2) > 0:
        return data_ptr1
    else:
        return data_ptr2


def main():
    # Local Definitions
    f1 = 73.4
    f2 = 81.7

    # Find the larger value
    lrg = larger(f1, f2, compare)

    # Print the result
    print(f"Larger value is: {lrg:5.1f}")


if __name__ == "__main__":
    main()