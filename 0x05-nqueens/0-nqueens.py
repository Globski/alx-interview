#!/usr/bin/python3
"""
N-Queens Solver

This script solves the N-Queens problem, which involves placing N non-attacking queens 
on an N×N chessboard. The script uses the backtracking algorithm to find all possible 
solutions to the problem. It is designed to be executed from the command line with 
one argument, the size of the chessboard (N).

Usage:
    ./0-nqueens.py N
        Where N is the size of the board and the number of queens to be placed.
        The program will print all possible solutions to the N-Queens puzzle.
        
        If N is not provided or is less than 4, the program will print an error message
        and exit with status 1. If N is not a valid integer, an error message will also
        be printed, and the program will exit.

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
    """Check if it's safe to place a queen at board[row][col]."""
    for r, c in board:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True

def solve_nqueens(N):
    """Solve the N-Queens problem using backtracking."""
    def backtrack(row, board):
        """Try to place queens in rows starting from 'row'."""
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
    """Main function to handle input and call the N-Queens solver."""
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
