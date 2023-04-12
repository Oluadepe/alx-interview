def makeChange(coins, total):
    """
    Logic to find the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    remain = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num = len(coins)
    while remain > 0:
        if coin_index >= num:
            return -1
        if remain - sorted_coins[coin_index] >= 0:
            remain -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1
    return coins_count

