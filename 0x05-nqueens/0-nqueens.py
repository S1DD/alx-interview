#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


solutions = []
"""List of valid solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard (n x n).
"""
positions = None
"""List of all possible positions on the chessboard.
"""


def get_input():
    """Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos1, pos2):
    """Checks if two queens are attacking each other.

    Args:
        pos1 (list or tuple): Position of the first queen (row, col).
        pos2 (list or tuple): Position of the second queen (row, col).

    Returns:
        bool: True if the queens are attacking each other, else False.
    """
    same_row = pos1[0] == pos2[0]
    same_col = pos1[1] == pos2[1]
    same_diag = abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])
    return same_row or same_col or same_diag


def solution_exists(candidate_solution):
    """Checks if a candidate solution already exists.

    Args:
        candidate_solution (list of [row, col]): A potential queen placement.

    Returns:
        bool: True if the solution already exists, else False.
    """
    global solutions
    for existing_solution in solutions:
        match_count = 0
        for existing_pos in existing_solution:
            for candidate_pos in candidate_solution:
                if existing_pos[0] == candidate_pos[0] and existing_pos[1] == candidate_pos[1]:
                    match_count += 1
        if match_count == n:
            return True
    return False


def place_queens(row, current_solution):
    """Recursively places queens on the board to build valid solutions.

    Args:
        row (int): The current row to place a queen.
        current_solution (list): The current list of queen positions.
    """
    global solutions, n
    if row == n:
        solution_copy = current_solution.copy()
        if not solution_exists(solution_copy):
            solutions.append(solution_copy)
    else:
        for col in range(n):
            index = row * n + col
            potential_queen = positions[index]
            if all(not is_attacking(potential_queen, placed)
                   for placed in current_solution):
                current_solution.append(potential_queen.copy())
                place_queens(row + 1, current_solution)
                current_solution.pop()


def find_solutions():
    """Generates all valid N-Queens solutions.
    """
    global positions, n
    positions = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    place_queens(0, [])


n = get_input()
find_solutions()
for solution in solutions:
    print(solution)
