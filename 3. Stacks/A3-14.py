def power(base, exp):
    """
    ===================== power =====================
    Computes the value of base raised to the power
    of exponent exp.

    Pre:
        base is the number to be raised.
        exp is the exponent.

    Post:
        The value of base raised to exp is returned.

    Return:
        base ** exp
    """

    # Base case
    if exp == 0:
        return 1

    # Recursive case
    else:
        return base * power(base, exp - 1)