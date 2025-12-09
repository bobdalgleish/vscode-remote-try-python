"""Generate the Fibonacci value for a given 'n'"""

from math import sqrt
from typing import List


def fib_1(n: int) -> int:
    """Use the recurrence relation."""
    if n <= 1:
        return n
    return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n: int) -> int:
    """Use the Binet formula."""
    if n <= 1:
        return n
    root_5: float = sqrt(5)
    phi: float = (1 + root_5) / 2
    psi: float = (1 - root_5) / 2
    return int((phi ** n - psi ** n) / root_5)


def fib_3(n: int) -> int:
    """Use the linear (memoized) recurrence relation."""
    memo: List[int] = [0, 1]
    if n <= 1:
        return n
    for i in range(len(memo), n + 1):
        memo += [memo[i - 1] + memo[i - 2]]
    return memo[n]


def fib_4(n: int) -> int:
    """Use the iterative linear form"""
    if n <= 1:
        return n
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = a + b, a
    return b
