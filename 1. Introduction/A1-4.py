def multi_matrix(matrix1, matrix2, size):
    # Create matrix3 filled with zeros
    matrix3 = []

    for row in range(size):
        result_row = []

        for column in range(size):
            total = 0

            # Multiply row of matrix1 by column of matrix2
            for k in range(size):
                total += matrix1[row][k] * matrix2[k][column]

            # Store sum in matrix3
            result_row.append(total)

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

    # Multiply matrix1 by matrix2
    matrix3 = multi_matrix(matrix1, matrix2, size)

    # Print matrix1
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    # Print matrix2
    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    # Print result
    print("\nMatrix 3 (Result):")
    for row in matrix3:
        print(row)


if __name__ == "__main__":
    main()