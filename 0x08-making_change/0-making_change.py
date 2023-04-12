def makeChange(coin, total):
    """
    Logic to find the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    remaining_amount = total
    coin_count = 0
    coin_index = 0
    sorted_coin = sorted(coin, reverse=True)
    num_coins = len(coin)
    while remaining_amount > 0:
        if coin_index >= num_coins:
            return -1
        if remaining_amount - sorted_coin[coin_index] >= 0:
            remaining_amount -= sorted_coin[coin_index]
            coin_count += 1
        else:
            coin_index += 1
    return coin_count

