# Alx Interview - UTF-8 Validation

## Description

This project implements a function to validate whether a given dataset represents valid UTF-8 encoding. UTF-8 is a character encoding that can represent characters using 1 to 4 bytes long. Each byte in this encoding has specific rules that determine how it can be used. In this project, the data is represented as a list of integers. Each integer corresponds to a byte of data. 
The function checks if the provided list of integers follows the rules of UTF-8 encoding. It ensures that the bytes in the list correctly represent valid UTF-8 characters.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0    | Write a method that determines if a given data set represents a valid UTF-8 encoding. | [0-validate_utf8.py](0-validate_utf8.py) |
|      | Prototype: `def validUTF8(data)` | |
|      | Return: True if data is a valid UTF-8 encoding, else return False | |
|      | A character in UTF-8 can be 1 to 4 bytes long | |
|      | The data set can contain multiple characters | |
|      | The data will be represented by a list of integers | |
|      | Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer | |

## Environment
- Python 3.4.3 or higher
- Ubuntu 20.04 LTS for execution

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Learning Objectives
- Understand and implement the UTF-8 encoding scheme.
- Apply bitwise operations to manipulate and analyze byte data.
- Improve skills in Python programming and data validation.

## Prototype Table

| Prototype | Description |
|-----------|-------------|
| `def validUTF8(data)` | Validates if the given data set is a valid UTF-8 encoding. |

## How to Use
1. To use the `validUTF8` function, import it from the module and provide a list of integers.
2. Provide a list of integers as input to check for valid UTF-8 encoding.
3. Ensure your Python script is executable. You can do this by running `chmod +x 0-validate_utf8.py` in your terminal.
4. Test your implementation using the provided `0-main.py` script. Make sure to create this file with test cases to verify the functionality of your implementation.

## Additional Notes

#### UTF-8 Encoding Rules

1. **Single-byte (ASCII)**: `0xxxxxxx` (0-127)
2. **Two-byte**: `110xxxxx 10xxxxxx` (128-2047)
3. **Three-byte**: `1110xxxx 10xxxxxx 10xxxxxx` (2048-65535)
4. **Four-byte**: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` (65536-1114111)

### Steps for the Algorithm

1. Read the bytes of the input data.
2. Determine the number of bytes the first byte indicates.
3. Validate the following bytes based on the expected number of continuation bytes.
4. Ensure each continuation byte starts with `10`.

- **Understand and Implement UTF-8:** Learn how the UTF-8 encoding scheme works, which represents characters using 1 to 4 bytes.

- **Bitwise Operations:** Use bitwise operations to manipulate and analyze byte data effectively.

- **Enhance Python Skills:** Improve your Python programming abilities, particularly in the area of data validation.

## Tasks

0. **UTF-8 Validation**
   - Mandatory
   - Write a method that determines if a given data set represents a valid UTF-8 encoding.
   - Prototype: `def validUTF8(data)`
   - Return: True if data is a valid UTF-8 encoding, else return False
   - A character in UTF-8 can be 1 to 4 bytes long
   - The data set can contain multiple characters
   - The data will be represented by a list of integers
   - Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

## Function Prototype
```python
def validUTF8(data)
```

## Parameters
- `data`: A list of integers representing the bytes of the data to be validated.

## Return Value
- Returns `True` if the data is a valid UTF-8 encoding, otherwise returns `False`.

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```
```python
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```
