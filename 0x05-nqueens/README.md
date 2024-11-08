# Alx Interview - N Queens

## Description
The project involves solving the **N-Queens** problem using a backtracking algorithm in Python, where the goal is to place **N** queens on a **N×N** chessboard such that no two queens threaten each other.  A queen can attack another queen if they are positioned in the same row, column, or diagonal. The goal is to find all possible solutions where no two queens are in the same row, column, or diagonal.

## Project Structure

| **Task**               | **Description**                                                                                                                                                                                                                                                                     | Source Code |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| **0**    | The **N Queens Puzzle** is the challenge of placing **N** non-attacking queens on an **N×N** chessboard. Write a program to solve the N-Queens problem. The program should output all possible solutions. Each solution should be in the form of a list of lists. Each sublist represents the position of a queen (row, column). <br> You are only allowed to import the `sys` module. <br> The solutions do not need to be printed in any specific order. The N Queens problem is a classic problem in computer science and artificial intelligence. <br> It involves placing N queens on an N×N chessboard such that no two queens threaten each other. |   [0-nqueens.py](/0x05-nqueens./0-nqueens.py) |                                                                                                                                                                                                                                                           |


## Environment
 - **Python Version**: Python 3.x
 - **OS**: Ubuntu 20.04 LTS
 - **Interpreter**: Python 3 interpreter   

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable

## Learning Objectives

- Practice **backtracking algorithms** and **recursion**.
- Learn to handle **command-line arguments** in Python.
- Understand the **backtracking approach** to solving constraint satisfaction problems like N-Queens.         

## Prototype Table

| **Prototype**             | **Function/Method Description**                                                                                         | **Parameters**                                   | **Returns**                              |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|------------------------------------------|
| **`is_valid(board, row, col)`**  | Checks if placing a queen at (row, col) does not conflict with already placed queens.                                  | `board` (list), `row` (int), `col` (int)       | `True` or `False` based on validity      |
| **`solve_nqueens(board, row, n, solutions)`**  | Attempts to solve the N Queens problem using backtracking. Recursively places queens row by row.                    | `board` (list), `row` (int), `n` (int), `solutions` (list) | Updates `solutions` list with valid configurations |
| **`print_solution(board)`**  | Prints the board configuration in a human-readable format with queens represented by "Q" and empty spaces by ".".    | `board` (list)                                 | `None` (Prints the board to the terminal) |
| **`main()`**  | Main function that handles the user input and invokes the backtracking solver.  | No parameters                                  | `None` (Exits with printed solutions or error messages) |

## How to Use

```bash
$ ./0-nqueens.py N
```
### Example

- Run the script with a command like:
  ```bash
  ./nqueens 8
  ```
  This will solve the 8-Queens problem and print all possible solutions.

- The N-Queens problem is only solvable for N >= 4.

- Where `N` is the size of the chessboard and must be an integer greater than or equal to 4.

###### The program will behave as follows:

- If the user provides the wrong number of arguments, it will print the message:
  ```
  Usage: nqueens N
  ```
  and exit with status 1.

- If `N` is not an integer, the program will print:
  ```
  N must be a number
  ```
  and exit with status 1.

- If `N` is smaller than 4, the program will print:
  ```
  N must be at least 4
  ```
  and exit with status 1.
   
### Example

#### Running the program with `N = 4`:

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

#### Running the program with `N = 6`:

```bash
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

---

## Additional Notes

### How the Solution Works:

The problem can be solved using a **backtracking algorithm**. The backtracking approach works by placing a queen in a row, then recursively trying to place queens in the subsequent rows, ensuring that no two queens threaten each other. If a valid placement is found, it is saved as a solution. If placing a queen leads to an invalid configuration (where queens threaten each other), the algorithm backtracks and tries a different position.

### Step-by-Step Process:

1. **Start with the first row**: The algorithm tries to place a queen in each column of the first row.
2. **Move to the next row**: After placing a queen in a row, the algorithm moves to the next row and attempts to place a queen in each column of that row, while ensuring that no two queens threaten each other.
3. **Check for conflicts**: For each new placement, the algorithm checks whether placing a queen in that column would cause a conflict in the same column or on any of the diagonals.
4. **Backtrack if needed**: If a queen cannot be placed without causing a conflict, the algorithm "backtracks" by removing the queen and trying a different position in the current row, or moving back to previous rows if needed.
5. **Print valid solutions**: When all queens are placed successfully, a valid solution is found, and it is printed.

### Key Constraints:
- **No two queens in the same row**: This is naturally satisfied because the algorithm places exactly one queen in each row.
- **No two queens in the same column**: The algorithm ensures that each column is used only once by keeping track of columns where queens are already placed.
- **No two queens on the same diagonal**: The algorithm checks the diagonals by comparing the row and column positions of placed queens. The two types of diagonals (main and anti-diagonal) are checked using mathematical conditions.

The solution is stored and printed when a valid configuration is found, ensuring that all possible configurations are explored.

Each solution is a list of lists, where each sublist represents the position of a queen. The first element in each sublist represents the row, and the second element represents the column of the queen.

For example:
- `[[0, 1], [1, 3], [2, 0], [3, 2]]` means that:
  - The first queen is placed at row 0, column 1.
  - The second queen is placed at row 1, column 3.
  - The third queen is placed at row 2, column 0.
  - The fourth queen is placed at row 3, column 2.

**Backtracking Algorithms**:
   - Backtracking is a problem-solving technique used for solving constraint satisfaction problems. It builds solutions incrementally, and if a solution path leads to an invalid state, the algorithm "backtracks" to a previous step and tries a different path.
   - In problems like N-Queens, it involves placing queens one by one in a row and backtracking when a conflict occurs (such as two queens attacking each other).

**Recursion**:
   - Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem. In the case of N-Queens, recursion is used to place queens in successive rows, exploring all possible positions and backtracking when necessary.

**Handling Command-Line Arguments in Python**:
   - Command-line arguments allow you to pass inputs to a Python program from the command line when running it. In Python, you can handle these arguments using the `sys.argv` list (from the `sys` module). This allows you to provide an input value (like the size of the board) when you run the program, making it more flexible.

**Backtracking Approach to N-Queens**:
   - The N-Queens problem can be solved using backtracking by placing one queen per row while ensuring no two queens share the same column or diagonal. The backtracking approach tries all possible placements and backtracks whenever a conflict is detected, ensuring all valid configurations are explored.

#### 1. **Backtracking Algorithm**
Backtracking is a general algorithmic technique for finding solutions to problems by incrementally building a solution and abandoning (or "backtracking") as soon as you determine that the solution cannot be completed.

In the case of the N-Queens problem:
- You incrementally place queens on the chessboard, one by one.
- At each step, you check if placing a queen is valid (no conflicts).
- If placing the queen leads to a conflict at a later step, you "backtrack" and move the queen to the next possible position.

#### 2. **Recursive Function**
Backtracking often involves recursion. Here, you will recursively attempt to place queens row by row:
- If placing a queen in a particular position is valid, recursively try to place the next queen.
- If it’s not valid, backtrack to the previous row and try another position.

#### 3. **List Manipulations**
You will need to manipulate lists to represent the chessboard and keep track of where the queens are placed:
- A list (or array) will represent the positions of queens.
- For example, `board[i] = j` means placing a queen in the **i-th** row and **j-th** column.
- You will also need to check for conflicts between queens on diagonals.

#### 4. **Command-Line Arguments**
You’ll need to handle the input for the size of the chessboard (i.e., the value of **N**) via command-line arguments. This can be done using Python’s `sys.argv` or `argparse`.

### Solution Approach

1. **Set Up the Chessboard**
   - Use a list to represent the board. For an N×N chessboard, create a list where the index represents the row, and the value at each index represents the column where the queen is placed.
   
2. **Backtracking Function**
   - The backtracking function should attempt to place a queen in a valid position, starting from the first row. If a queen cannot be placed in a row, backtrack and move the previously placed queen.

3. **Validating the Position**
   - For each position (i, j) on the board, ensure no other queens are on the same column or diagonal.

4. **Generate the Solution**
   - Once a solution is found, store the current arrangement of queens (i.e., the list of their positions).

5. **Return the Results**
   - The result should be all valid solutions, or just one solution, depending on the specification of the problem.

## Tasks

#### 0. N Queens

**Chess grandmaster [Judit Polgár](https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r), the strongest female chess player of all time**

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

### Usage: 
`nqueens N`

- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1.
- Where N must be an integer greater or equal to 4.
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1.
- If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1.
- The program should print every possible solution to the problem.
- One solution per line.
- Format: see example.
- You don’t have to print the solutions in a specific order.
- You are only allowed to import the sys module.
Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
---

**Example:**

```bash
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```bash
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

---

**Repo:**

- GitHub repository: alx-interview
- Directory: 0x05-nqueens
- File: 0-nqueens.py
