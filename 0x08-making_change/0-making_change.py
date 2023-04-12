def makeChange(coins, total):
    """
    Logic to find the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    remaining_amount = total
    coins_count = 0
    coins_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)
    while remaining_amount > 0:
        if coins_index >= num_coins:
            return -1
        if remaining_amount - sorted_coins[coins_index] >= 0:
            remaining_amount -= sorted_coins[coins_index]
            coins_count += 1
        else:
            coins_index += 1
    return coins_count

