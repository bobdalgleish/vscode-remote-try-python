"""Demonstration of basic competency in Python coding."""
import unittest


def reverse_digits(source: int) -> str:
    """Reverse the digits of a positive integer"""
    assert isinstance(source, int), f"Not an integer: {source}"
    assert source >= 0, f"Must be non-negative: {source}"
    return str(source)[::-1]


class TestReverseDigits(unittest.TestCase):
    """Test basic functionality of reverse_digits() function"""

    def test_good_positive(self) -> None:
        """Accept positive numbers"""
        self.assertEqual('31', reverse_digits(13))

    def test_zero(self) -> None:
        """Accept 0"""
        self.assertEqual('0', reverse_digits(0))

    def test_not_an_integer(self) -> None:
        """Reject non-integral value"""
        with self.assertRaises(AssertionError):
            reverse_digits('not an integer')

    def test_negative_number(self) -> None:
        """Reject negative value"""
        with self.assertRaises(AssertionError):
            reverse_digits(-4)


if __name__ == '__main__':
    unittest.main()
