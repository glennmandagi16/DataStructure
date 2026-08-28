def print_reverse():
    # Read data
    data = input("Enter data (press Enter to stop): ")

    # Check if the input has ended
    if data == "":
        return

    # Recursive call
    print_reverse()

    # Print data after recursive call
    print(data)


# Main program
if __name__ == "__main__":
    print("Enter several items:")
    print_reverse()