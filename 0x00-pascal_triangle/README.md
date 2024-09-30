# Alx Interview - Pascal's Triangle

## Descriotion
This project involves creating a function to generate Pascal's Triangle using Python and returning it as a list of lists Each element in the triangle is the sum of the two elements above it, with edges set to 1. Pascal's Triangle is a triangular array where each element is the sum of the two directly above it. This project will help solidify your understanding of lists, functions, loops, and basic arithmetic operations in Python.

## Project Structure
| Task | Description | Source Code |
|------|-------------|-------------|
| 0    | Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`. | [0-pascal_triangle.py](0-pascal_triangle.py) |

## Environment
- Python 3.x

## Requirements

- Basic understanding of Python lists, loops, and functions.
- **Edge Cases**: Handle inputs such as `n = 0` gracefully, returning an empty list.
- It is assumed that `n` will always be an integer.

## Learning Objectives

- Understand the construction of Pascal's Triangle.
- Practice using nested loops and list comprehensions in Python.
- Gain experience in handling edge cases and implementing basic algorithmic logic.

## Function Prototypes

| Function Name          | Parameters           | Return Type        | Description                                          |
|-----------------------|----------------------|---------------------|------------------------------------------------------|
| `pascal_triangle`     | `n: int`             | `List[List[int]]`   | Returns a list of lists representing Pascal's Triangle with `n` rows. |

## Function Details

- **`pascal_triangle(n)`**:
  - **Parameters**:
    - `n`: An integer representing the number of rows of Pascal's Triangle to generate.
  - **Return**:
    - A list of lists where each inner list represents a row of Pascal's Triangle. Returns an empty list if `n <= 0`.

## How to Use

1. Import the `pascal_triangle` function from the module.
2. Call the function with a non-negative integer to generate Pascal's Triangle.
3. Use the provided test script to print the triangle.

### Example Usage

- **File**: `0-pascal_triangle.py` (contains the `pascal_triangle` function)
- **File**: `0-main.py` (contains the test code)

## Function Specification

### Function Name

```python
def pascal_triangle(n):
```

### Parameters

- **n** (int): The number of rows to generate for Pascal's Triangle.

### Returns

- A list of lists representing Pascal's Triangle if `n > 0`.
- An empty list if `n <= 0`.

## Example

## Testing the Function

To test the function, use the following script:

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

### Expected Input/Output

Running the test script `n = 5`, the function should return:

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

For `n = 0`, the function should return:

```python
[]
```
The function should return an empty list for any input `n <= 0`.

## Tasks

0. **Pascal's Triangle**
   - Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`.
   - Returns an empty list if `n <= 0`.
   - You can assume `n` will be always an integer.

### Example Usage

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

### Expected Output

When running the above script, the output should be:

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Additional Info

- Ensure to test the function with various inputs, including edge cases like `n = 0` and negative values.
- Explore the mathematical properties of Pascal's Triangle for deeper understanding.
- Consider the time complexity of your solution.
- Optimize where necessary for larger values of `n`.
- Feel free to explore recursive approaches, though they are not required.
