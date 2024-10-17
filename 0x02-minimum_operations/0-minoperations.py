#!/usr/bin/python3
"""
Contains a solution to the mininum operations problem
"""


def minOperations(n: int) -> int:
    """
    Calculates the number of operations needed to
    to get `n` number of H characters in a text file.
    """
    if n <= 0:
        return 0

    primes = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n //= i
        i += 1

    if n > 1:
        primes.append(n)

    return sum(primes)
