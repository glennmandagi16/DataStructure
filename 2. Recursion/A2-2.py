def recursive_factorial(n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    else:
        return n * recursive_factorial(n - 1)


# Main program
if __name__ == "__main__":
    n = 5

    result = recursive_factorial(n)

    print("Factorial of", n, "is:", result)