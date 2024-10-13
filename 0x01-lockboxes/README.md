# Alx Interview - Lockboxes

### Description

This project addresses the "Lockboxes" problem, where you must determine if all locked boxes can be opened using a set of keys contained within them. Each box is indexed from 0 to n-1, and keys inside the boxes allow access to other boxes. The first box, `boxes[0]`, is always unlocked, providing access to start the unlocking process.

**Objective**: The task is to Implement a method `canUnlockAll` that checks whether all boxes can be opened based on the keys available within them.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0    | You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes. Write a method that determines if all the boxes can be opened. | [0-lockboxes.py](0-lockboxes.py) |

## Environment
- **Python Version:** 3.4.3
- **OS:** Tested on Ubuntu 20.04 LTS

## Requirements
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Learning Objectives
- Understand how to manipulate lists in Python.
- Gain knowledge of graph traversal algorithms (DFS/BFS).
- Learn to track visited nodes using sets.
- Develop an understanding of algorithmic complexity.

## Prototype Used

| Prototype                     |
|-------------------------------|
| `def canUnlockAll(boxes)`     |

## Functionality
The `canUnlockAll` function accepts a list of lists, where each inner list contains keys to other boxes. The function returns `True` if all boxes can be opened; otherwise, it returns `False`.

## How to Use

#### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/alx-interview.git
   cd alx-interview/0x01-lockboxes
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd 0x01-lockboxes
   ```

#### Running the Main Program

1. **Open a Terminal**: Ensure a terminal is open in the project directory.

2. **Run the Test Script**:
   ```bash
   ./main_0.py
   ```

   This will execute predefined test cases and display the results of the `canUnlockAll` function.

### Test Cases Included

The `main_0.py` script includes several test cases to validate the functionality of the `canUnlockAll` function:

- **Test Case 1**:
  ```python
  boxes = [[1], [2], [3], [4], []]
  print(canUnlockAll(boxes))  # Expected Output: True
  ```
  - **Description**: Each box contains a key to the next, allowing access to all boxes.

- **Test Case 2**:
  ```python
  boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
  print(canUnlockAll(boxes))  # Expected Output: True
  ```
  - **Description**: A complex scenario with multiple keys leading to all boxes being accessible.

- **Test Case 3**:
  ```python
  boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
  print(canUnlockAll(boxes))  # Expected Output: False
  ```
  - **Description**: A case where not all boxes can be opened due to missing keys.

### Modifying Test Cases

To add or modify test cases, edit the `main_0.py` file. You can create new lists of boxes and call the `canUnlockAll` function to test different scenarios.

### Example Output

When running the test script, the output will display whether all boxes can be opened for each test case:

```
True
True
False
```

### Additional Notes

1. **Graph Theory Basics**:
   - Visualize boxes as nodes and keys as edges in a graph.
   - Implement traversal algorithms (DFS or BFS) to explore reachable boxes.

2. **Algorithmic Complexity**:
   - Analyze time and space complexity to evaluate the efficiency of your solution.

3. **Set Operations**:
   - Utilize sets to track visited boxes and keys efficiently.

### Steps to Implement the Solution

1. **Input Representation**:
   - Represent boxes as a list of lists, where each inner list contains keys to other boxes.

2. **Initialization**:
   - Create a set to track visited boxes and a queue (or list) to manage boxes to explore, starting with box 0.

3. **Traversal Algorithm**:
   - Implement a BFS or DFS approach to explore boxes:
     - For BFS, use a queue to explore each box and its keys iteratively.
     - For DFS, recursively explore each box until no new boxes can be opened.

4. **Check for Completion**:
   - After exploring, compare the size of the visited set to the total number of boxes. Return `True` if all boxes are visited, otherwise return `False`. 

## Tasks

0. **Lockboxes**
   - **Mandatory**
   - **Score:** 0.0% (Checks completed: 0.0%)
   - You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
   - Write a method that determines if all the boxes can be opened.
   - **Prototype:** `def canUnlockAll(boxes)`
   - `boxes` is a list of lists
   - A key with the same number as a box opens that box
   - You can assume all keys will be positive integers
   - There can be keys that do not have boxes
   - The first box `boxes[0]` is unlocked
   - Return `True` if all boxes can be opened, else return `False`
```python
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```

```python
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```
