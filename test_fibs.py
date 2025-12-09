import unittest
from fib1 import fib_1, fib_2, fib_3, fib_4


class TestFibonacci(unittest.TestCase):
    """Perform tests on various Fibonacci implementations.
    
    Test the recurrence relation first."""

    results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    def test_1(self) -> None:
        """Test the recurrence relation."""
        for n in range(5, 12):
            self.assertEqual(self.results[n], fib_1(n))

    def test_binet(self) -> None:
        """Test the Binet formula."""
        for n in range(5, 12):
            self.assertEqual(self.results[n], fib_2(n))

    def test_memo(self) -> None:
        """Test the memoized recurrence relation."""
        for n in range(5, 12):
            self.assertEqual(self.results[n], fib_3(n))

    def test_iterative(self) -> None:
        """Test the iterative linear form."""
        for n in range(5, 12):
            self.assertEqual(self.results[n], fib_4(n))
            