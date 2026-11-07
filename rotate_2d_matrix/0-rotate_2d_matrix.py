#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to be rotated.
    """
    n=len(matrix)
    for i in range(n//2):
        for j in range(n+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            for row in matrix:
                row.reverse()
         