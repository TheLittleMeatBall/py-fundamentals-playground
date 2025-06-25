import pytest
from debug import is_palindrome, factorial, fizzbuzz

@pytest.mark.parametrize("word, expected", [
    ("racecar", True),
    ("level", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("ab", False),
])
def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, "1"),
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (13, "13"),
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
