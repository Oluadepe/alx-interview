#!/usr/bin/python3
"""
Module for Prime Game
"""


def findingPrimeNumber(n):
    """
    Returns a list of primes using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): Upper limit for finding primes.

    Returns:
        list: A list of boolean values representing prime numbers up to n.

    """
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False
    sieve[0] = sieve[1] = False
    return sieve


def isWinner(x, nums):
    """
    Solves Prime Game and returns the winner.

    Args:
        x (int): Number of turns to be played.
        nums (list): List of integers representing the numbers
        to be used in the game.

    Returns:
        str or None: The winner of the game, either "Maria", "Ben",
        or None if it's a draw.

    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    sieve = findingPrimeNumber(max_num)

    primes_count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            primes_count += 1
        sieve[i] = primes_count

    player1 = sum(sieve[n] % 2 == 1 for n in nums)

    if player1 * 2 == len(nums):
        winner = None
    elif player1 * 2 > len(nums):
        winner = "Maria"
    else:
        winner = "Ben"

    return winner
