def iterative_factorial(n):
    # Set i to 1
    i = 1

    # Set factN to 1
    fact_n = 1

    # Loop while i <= n
    while i <= n:
        # factN = factN * i
        fact_n = fact_n * i

        # Increment i
        i += 1

    # Return factorial
    return fact_n


# Main program
if __name__ == "__main__":
    n = 5

    result = iterative_factorial(n)

    print("Factorial of", n, "is:", result)