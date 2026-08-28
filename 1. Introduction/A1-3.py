def add_matrix(matrix1, matrix2, size):
    # Create matrix3 to store the result
    matrix3 = []

    # Loop through rows
    for row in range(size):

        # Create a new row
        result_row = []

        # Loop through columns
        for column in range(size):

            # Add matrix1 and matrix2 cells
            total = matrix1[row][column] + matrix2[row][column]

            # Store sum in matrix3
            result_row.append(total)

        # Add the row to matrix3
        matrix3.append(result_row)

    return matrix3


def main():
    # Define matrix1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Define matrix2
    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # Size of matrix
    size = 3

    # Add matrix1 and matrix2
    matrix3 = add_matrix(matrix1, matrix2, size)

    # Print the result
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nMatrix 3 (Result):")
    for row in matrix3:
        print(row)


if __name__ == "__main__":
    main()