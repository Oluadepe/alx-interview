def isPrime(i):
    """
    Check if a number is prime.
    """
    if i < 2:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True


def findPrimes(n):
    """
    Dispatch a given set into prime numbers and non-prime numbers.
    """
    counter = 0
    target = list(n)
    for i in range(1, len(target) + 1):
        if isPrime(i):
            counter += 1
            target.remove(i)
            target = _searchMultiple(i, target)
    return counter


def isWinner(x, nums):
    players = {'Maria': 0, 'Ben': 0}
    for num in nums:
        cluster = set(range(1, num + 1))
        temp = findPrimes(cluster)
        if temp % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1
    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None

