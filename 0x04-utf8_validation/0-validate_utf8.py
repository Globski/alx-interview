#!/usr/bin/python3
"""
Module for UTF-8 Validation.

This module contains a function to validate whether a given dataset
represents a valid UTF-8 encoding. The function checks whether the
provided list of integers (representing bytes) adheres to the UTF-8
encoding rules, which allow characters to be represented using one
to four bytes.

Function:
    validUTF8(data): Determines if the input list represents valid UTF-8 encoding.

Usage:
    To use the `validUTF8` function, import it in your Python script
    and pass a list of integers (each between 0 and 255) to check for
    valid UTF-8 encoding.

Example:
    data = [65]
    print(validUTF8(data))
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    A character in UTF-8 can be 1 to 4 bytes long. This function checks 
    whether the provided list of integers represents valid UTF-8 bytes.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF
        
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
