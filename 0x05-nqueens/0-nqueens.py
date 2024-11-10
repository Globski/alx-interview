#!/usr/bin/python3
"""
N-Queens Solver

This script solves the N-Queens problem, which involves placing N non-attacking
queens on an N×N chessboard. The script uses the backtracking algorithm to find
all possible solutions to the problem. It is designed to be executed from
the command line with one argument, the size of the chessboard (N).

Usage:
    ./0-nqueens.py N
        Where N is the size of the board and the number of queens to be placed.
        The program will print all possible solutions to the N-Queens puzzle.

        If N is not provided or is less than 4, the program will print an error
        message and exit with status 1. If N is not a valid integer, an error
        message will also be printed, and the program will exit.

Exit Status:
    0  - If the program runs successfully and outputs the solutions.
    1  - If there is an error in the input or execution.

    Example:
    $ ./0-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

    $ ./0-nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the given position (row, col)
    on the board.

    The function checks three conditions:
    1. No other queen in the same column.
    2. No other queen in the same diagonal (top-left to bottom-right).
    3. No other queen in the same diagonal (top-right to bottom-left).

    Args:
        board (list): The list of positions of previously placed queens.
        row (int): The current row where the queen is to be placed.
        col (int): The current column where the queen is to be placed.
     
    Returns:
        bool: True if it's safe to place the queen at (row, col), False otherwise.
    """
    for r, c in board:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N-Queens problem using backtracking.

    The function uses the helper function `backtrack()` to explore all possible
    placements of queens on the board. It stores the valid solutions in a list
    and returns it once all solutions are found.

    Args:
        N (int): The size of the chessboard and the number of queens to place.

    Returns:
        list: A list of lists, each representing a valid solution
        to the N-Queens puzzle.
    """

    def backtrack(row, board):
        """
        Try to place queens in rows starting from the given `row`.

        If a valid configuration is found (all rows are filled), the solution
        is added to the list of solutions.

        Args:
            row (int): The current row to attempt placing a queen.
            board (list): The current list of queens placed on the board (row, col) pairs.
        """
        if row == N:
            solutions.append(board.copy())
            return
        for col in range(N):
            if is_safe(board, row, col):
                board.append([row, col])
                backtrack(row + 1, board)
                board.pop()

    solutions = []
    backtrack(0, [])
    return solutions


def main():
    """
    Main function to handle input and execute the N-Queens solver.

    This function parses the command-line arguments, validates the input,
    and calls the `solve_nqueens()` function to find all solutions.
    It then prints each solution to the console.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
