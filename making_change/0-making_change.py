#!/usr/bin/python3
"""Making change: fewest coins needed to reach a total."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Dynamic programming: dp[a] holds the fewest coins that sum to a.
    Return 0 if total <= 0, and -1 if total cannot be reached.
    """
    if total <= 0:
        return 0

    impossible = total + 1
    dp = [0] + [impossible] * total

    for coin in coins:
        for amount in range(coin, total + 1):
            candidate = dp[amount - coin] + 1
            if candidate < dp[amount]:
                dp[amount] = candidate

    return dp[total] if dp[total] != impossible else -1
