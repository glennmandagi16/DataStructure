def gcd(a, b):
    # Check if b is 0
    if b == 0:
        return a

    # Check if a is 0
    if a == 0:
        return b

    # Recursive call using the Euclidean algorithm
    return gcd(b, a % b)


# Main program
if __name__ == "__main__":
    a = 48
    b = 18

    result = gcd(a, b)

    print("GCD of", a, "and", b, "is:", result)