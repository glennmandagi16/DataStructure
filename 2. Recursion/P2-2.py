def fib(num):
    """
    Calculates the nth Fibonacci number.

    Pre:
        num identifies Fibonacci number

    Post:
        Returns nth Fibonacci number
    """

    # Base Case
    if num == 0 or num == 1:
        return num

    # Recursive Case
    return fib(num - 1) + fib(num - 2)


def main():
    # Local Declarations
    series_size = 10

    # Statements
    print("Print a Fibonacci series.")

    for looper in range(series_size):
        if looper % 5:
            print(f", {fib(looper):8d}", end="")
        else:
            print(f"\n{fib(looper):8d}", end="")

    print()


if __name__ == "__main__":
    main()