"""Demonstration of basic competency in Python coding."""


def reverse_digits(source: int) -> str:
    """Reverse the digits of a non-negative integer"""
    assert isinstance(source, int), f"Not an integer: {source}"
    assert source >= 0, f"Must be non-negative: {source}"
    return str(source)[::-1]
