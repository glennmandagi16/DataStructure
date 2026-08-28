def towers(num_disks, source, dest, auxiliary):
    """
    Recursively move disks from source to destination.

    Pre:
        num_disks is the number of disks to be moved.
        source, dest, and auxiliary towers are given.

    Post:
        Steps for moving the disks are printed.
    """

    # Print current operation
    print("Towers:", num_disks, source, dest, auxiliary)

    # Base case
    if num_disks == 1:
        print("Move from", source, "to", dest)

    # Recursive case
    else:
        # Move num_disks - 1 from source to auxiliary
        towers(num_disks - 1, source, auxiliary, dest)

        # Move the largest disk from source to destination
        print("Move from", source, "to", dest)

        # Move num_disks - 1 from auxiliary to destination
        towers(num_disks - 1, auxiliary, dest, source)


def main():
    # Number of disks
    num_disks = 3

    # Define the towers
    source = "A"
    dest = "C"
    auxiliary = "B"

    # Start Tower of Hanoi
    towers(num_disks, source, dest, auxiliary)


if __name__ == "__main__":
    main()