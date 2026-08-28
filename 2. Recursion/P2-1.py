def gcd(a, b):
    """
    Calculates greatest common divisor using
    the Euclidean algorithm.

    Pre:
        a and b are positive integers greater than 0

    Post:
        Greatest common divisor is returned
    """

    if b == 0:
        return a

    if a == 0:
        return b

    return gcd(b, a % b)


def main():
    # Test GCD Algorithm
    print("Test GCD Algorithm")

    gcd_result = gcd(10, 25)

    print("GCD of 10 & 25 is", gcd_result)

    print("End of Test")


if __name__ == "__main__":
    main()