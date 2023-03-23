def makeChange(coins, total):
    # Initialize the dynamic programming array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Compute the minimum number of coins needed for each total amount
    for t in range(1, total + 1):
        for coin in coins:
            if t - coin >= 0:
                dp[t] = min(dp[t], dp[t - coin] + 1)

    # Return the result
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

