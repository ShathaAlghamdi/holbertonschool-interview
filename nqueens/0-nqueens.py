#!/usr/bin/python3
"""
Module to solve the N queens puzzle using backtracking.
"""
import sys


def solve_nqueens(n: int) -> None:
    """
    Solves the N queens problem and prints all possible solutions.

    Args:
        n (int): The size of the chessboard and number of queens.
    """
    def backtrack(row: int, current_solution: list) -> None:
        """
        Recursive backtracking function to find valid positions for queens.
        """
        if row == n:
            print(current_solution)
            return

        for col in range(n):
            conflict = False
            for r, c in current_solution:
                if c == col or abs(row - r) == abs(col - c):
                    conflict = True
                    break
            if not conflict:
                current_solution.append([row, col])
                backtrack(row + 1, current_solution)
                current_solution.pop()

    backtrack(0, [])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n_val = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n_val < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n_val)
    