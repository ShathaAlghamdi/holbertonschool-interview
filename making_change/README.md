# Making Change

`makeChange(coins, total)` returns the fewest number of coins needed to reach
`total`, using an unlimited supply of each coin value in `coins`.

- Returns `0` when `total` is 0 or less.
- Returns `-1` when the total cannot be reached.

The solution uses bottom-up dynamic programming: `dp[a]` is the fewest coins
that add up to `a`. For each coin, every amount from the coin's value up to
`total` is updated with `dp[a - coin] + 1` when that is smaller.
Time complexity: O(len(coins) * total). Memory: O(total).
