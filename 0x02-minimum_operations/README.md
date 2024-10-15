# Alx Interview - Minimum Operations

## Description

This project focuses on implementing a method to calculate the minimum number of operations required to achieve exactly `n` characters of "H" in a text file, starting with a single "H". The only operations permitted are `Copy All` and `Paste`. The goal is to determine the fewest operations needed to produce a specified number of "H" characters using these two methods.

## Features
1. **Prime Factorization**: Write a function to calculate the prime factors of `n`.
2. **Calculate Operations**: Sum the prime factors to get the total number of operations.
3. The implementation assumes that `n` is a positive integer.
4. The `minOperations` function calculates the required operations based on the prime factorization of `n`.

## Project Structure

| Task Description | Source Code |
|------------------|-------------|
| In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file. | [0-minoperations.py](0-minoperations.py) |

## Environment
- Python 3.4.3 or later
- Ubuntu 20.04 LTS

## Requirements
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Learning Objectives
For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only `Copy All` and `Paste` operations. 
- Understand the use of prime factorization to optimize operation counts.
- Gain proficiency in dynamic programming concepts and implementation.
- Develop skills in code optimization to improve solution efficiency.
- Learn to apply greedy algorithms to make optimal choices at each step.
- Enhance basic Python programming skills, including loops, conditionals, and functions.

## Prototype Used in the Project
| Function Name     | Prototype                             |
|-------------------|---------------------------------------|
| Minimum Operations | `def minOperations(n: int) -> int`   |

## Function Prototype
```python
def minOperations(n)
```

### Parameters
- `n` (int): The target number of "H" characters.

### Returns
- Returns an integer representing the minimum number of operations needed to achieve `n` characters. If it is impossible to achieve, the function returns `0`.

## How to Use
1. Ensure you have Python 3 installed.
2. Place the `0-minoperations.py` and a test file (e.g., `0-main.py`) in the same directory.
3. Run the test script using Python 3:
```bash
python3 0-main.py
```

## Example Usage
To test the function, you can use the following script:

```python
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
```

### Example Output
```
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```

- Run the script and input the desired number of characters. The program will output the minimum number of operations needed.
- Test your solution with various inputs to ensure accuracy.
- Ensure that both files are in the correct directory
- Ensure the Python file has executable permissions.

## Additional Notes

1. **Copy All**: Copies all characters currently present.
2. **Paste**: Pastes the copied characters.

#### Goal
Starting from 1 character (i.e., "A"), we want to reach `n` characters using the least number of operations.

#### Insight
The optimal strategy revolves around prime factorization. The number of operations corresponds to the sum of the prime factors of `n`. Each prime factor `p` indicates a "Copy All" followed by `p-1` "Paste" operations.

For instance:
- If `n = 12`, its prime factorization is `2^2 * 3^1`. The operations to achieve 12 can be:
  - Copy (2 characters), Paste (1 time) to get 4.
  - Copy (4 characters), Paste (2 times) to get 12.
  - Total operations = 1 (for the first copy) + 1 (for the first paste) + 1 (for the second copy) + 2 (for pastes) = 5.

## Tasks

#### Task 0. Minimum Operations

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

### Prototype:
```python
def minOperations(n)
```

### Returns:
- An integer.
- If n is impossible to achieve, return 0.

### Example:
```plaintext
n = 9

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```

### Testing:
```python
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
```

### Expected Output:
```plaintext
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```

- GitHub repository: alx-interview
- Directory: 0x02-minimum_operations
- File: 0-minoperations.py

