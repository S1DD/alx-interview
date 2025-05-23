#!/usr/bin/python3
"""
Solves the N Queens problem using backtracking.

Usage:
    ./0-nqueens.py N

Where:
    N must be an integer >= 4
    Prints every possible solution to the N queens problem
    Each solution is a list of coordinate pairs [row, col]
"""
import sys


def can_place(positions, curr_row, curr_col):
    """Check if a queen can be placed at (curr_row, curr_col)"""
    for r, c in positions:
        if c == curr_col or abs(curr_row - r) == abs(curr_col - c):
            return False
    return True


def nqueens_solver(size, row_idx=0, positions=[]):
    """Recursively solve the N Queens problem"""
    if row_idx == size:
        print(positions)
        return

    for col_idx in range(size):
        if can_place(positions, row_idx, col_idx):
            nqueens_solver(size, row_idx + 1, positions + [[row_idx, col_idx]])


def check_and_execute():
    """Validate input and run the N Queens solver"""
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens_solver(size)


if __name__ == "__main__":
    check_and_execute()
