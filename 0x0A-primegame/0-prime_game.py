#!/usr/bin/python3"""


def isWinner(x, nums):
    """Identify winner in a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # Sieve algorithym to generate prime
    n = max(nums)
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # Sieve numbers primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
