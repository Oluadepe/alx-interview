def makeChange(coin_values, total_amount):
    """
    Logic to find the fewest number of coins needed to meet a given amount total.
    """
    if total_amount <= 0:
        return 0
    remaining_amount = total_amount
    coin_count = 0
    coin_index = 0
    sorted_coin_values = sorted(coin_values, reverse=True)
    num_coins = len(coin_values)
    while remaining_amount > 0:
        if coin_index >= num_coins:
            return -1
        if remaining_amount - sorted_coin_values[coin_index] >= 0:
            remaining_amount -= sorted_coin_values[coin_index]
            coin_count += 1
        else:
            coin_index += 1
    return coin_count

