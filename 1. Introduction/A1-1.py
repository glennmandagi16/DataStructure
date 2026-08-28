def sample(page_number):
    line_count = 0
    lines_per_page = 5

    # Open the file
    with open("report.txt", "r") as file:

        # Loop until the end of the file
        for line in file:

            # Check if the page is full
            if line_count % lines_per_page == 0:
                page_number += 1

                # Write page heading
                print()
                print("=" * 40)
                print("REPORT - PAGE", page_number)
                print("=" * 40)

            # Write report line
            print(line.strip())

            # Increment line count
            line_count += 1

    # Return the number of lines printed and page number
    return line_count, page_number


# Main program
if __name__ == '__main__':
    page_number = 0

    line_count, page_number = sample(page_number)

    print()
    print("Number of lines printed:", line_count)
    print("Number of pages:", page_number)