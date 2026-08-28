def towers(n, source, dest, auxiliary):
    """
    Move disks from source to destination using recursion.

    Pre:
        The tower consists of n disks.
        Source, destination, and auxiliary towers are given.

    Post:
        Steps for the moves are printed.
    """

    # Display current recursive call
    print(f"Towers ({n}, {source}, {dest}, {auxiliary})")

    # Base case
    if n == 1:
        towers.step += 1
        print(
            f"\t\t\tStep {towers.step:3d}: "
            f"Move from {source} to {dest}"
        )

    # Recursive case
    else:
        # Move n - 1 disks from source to auxiliary
        towers(n - 1, source, auxiliary, dest)

        # Move the largest disk from source to destination
        towers.step += 1
        print(
            f"\t\t\tStep {towers.step:3d}: "
            f"Move from {source} to {dest}"
        )

        # Move n - 1 disks from auxiliary to destination
        towers(n - 1, auxiliary, dest, source)


# Static variable used to count the steps
towers.step = 0


def main():
    # Ask the user for the number of disks
    num_disks = int(input("Please enter number of disks: "))

    print("Start Towers of Hanoi.\n")

    # Start Tower of Hanoi
    towers(num_disks, "A", "C", "B")

    print("\nI Hope you didn't select 64 and end the world!")


if __name__ == "__main__":
    main()