#!/usr/bin/python3
"""Module for calculating the minimum number of operations."""


def minOperations(n):
    """Return the minimum operations needed to get n H characters."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
