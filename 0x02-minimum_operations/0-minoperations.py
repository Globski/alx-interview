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

    if n <= 1:
        return 0
    
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
    return operations
