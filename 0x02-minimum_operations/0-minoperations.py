#!/usr/bin/python3
"""
This script calculates the minimum number of operations required
to achieve exactly n 'H' characters in a text editor using
only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to reach n 'H' characters.

    The function uses the operations "Copy All" and "Paste" to build up to
    exactly n characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum number of operations to achieve exactly n 'H' characters.
             Returns 0 if n is impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor  # Reduce n
        factor += 1

    return operations
