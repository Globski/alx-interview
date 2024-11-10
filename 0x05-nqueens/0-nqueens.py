#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """
    Check if a queen can be placed at position (row, col).
    A queen can only be placed if no other queens are attacking it.
    We check for attacks in the column and diagonals.
    """
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == row - i:
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    """
    Solve the N-Queens problem using backtracking.
    We recursively try to place queens row by row, ensuring no two queens
    threaten each other.
    """
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1

def print_solution(board):
    """
    Print the board configuration.
    Each queen is represented by 'Q' and empty spaces by '.'.
    """
    for row in board:
        print("." * row + "Q" + "." * (len(board) - row - 1))

def main():
    """
    Main function to handle input and invoke the solver.
    It reads the input size (N) from command-line arguments and
    prints all possible solutions for the N-Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()
