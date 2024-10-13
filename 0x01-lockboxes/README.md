# Alx Interview - Lockboxes

### Description

This project determines if all locked boxes can be opened using a set of keys contained within them. Each box is indexed from 0 to n-1, and keys within the boxes allow access to other boxes. The first box, `boxes[0]`, is always unlocked. Each box can hold keys to other boxes

**objective:**
The task is to determine if all locked boxes can be opened using a method called `canUnlockAll`. Each box may contain keys that unlock other boxes, and the first box (index 0) is always unlocked.

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
The main function, `canUnlockAll`, takes a list of lists as input, where each inner list contains keys to other boxes. The function returns `True` if all boxes can be opened, and `False` otherwise.
- The function will return `True` or `False` based on whether all boxes can be opened.

## How to use
1. Clone the repository: Ensure Python is installed.
   ```bash
   git clone https://github.com/YOUR_USERNAME/alx-interview.git
   cd alx-interview/0x01-lockboxes
   ```
2. Run the main script to test the function:
   ```bash
   ./main_0.py
   ```

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

### Additional Notes

1. **Lists and List Manipulation**:
   - Use lists to represent boxes and keys.
   - Access, iterate, and modify lists effectively.

2. **Graph Theory Basics**:
   - Visualize boxes as nodes and keys as edges in a graph.
   - Use traversal algorithms (DFS or BFS) to explore reachable boxes.

3. **Algorithmic Complexity**:
   - Analyze the efficiency of your solution in terms of time and space.

4. **Recursion**:
   - Implement recursive solutions for traversing through boxes.

5. **Queue and Stack**:
   - Use a queue for BFS or a stack for DFS when exploring boxes.

6. **Set Operations**:
   - Utilize sets to track visited boxes and available keys.

### Steps to Implement the Solution

1. **Input Representation**:
   - Represent the boxes and their keys as a list of lists.
   - For example, `boxes = [[1], [2], [3], []]` means box 0 has a key to box 1, box 1 has a key to box 2, and so on.

2. **Initialization**:
   - Create a set to track visited boxes.
   - Use a list (or queue) to manage boxes to explore, starting with box 0.

3. **Traversal Algorithm**:
   - Implement BFS or DFS:
     - For BFS, enqueue the initial box and iterate through keys.
     - For DFS, recursively explore each box.

4. **Check for Completion**:
   - After exploring, compare the size of the visited set to the total number of boxes.
   - If all boxes are visited, return `True`; otherwise, return `False`.
