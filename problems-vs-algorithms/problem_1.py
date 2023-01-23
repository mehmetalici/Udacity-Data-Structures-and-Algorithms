"""
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

Examples:
Given number: 16, Answer: 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
"""

from typing import Type


def sqrt(number):
    if number < 0:
        raise ValueError("Math domain error.")
    if not isinstance(number, (int, float)):
        raise TypeError(f"Must be real number, not {type(number)}")
    return _sqrt(number, 0, number)


def _sqrt(number, start, end):
    if end in [0, 1]:
        return end

    mid = (start + end) // 2

    if mid ** 2 <= number < (mid + 1) ** 2:
        return mid
    elif mid ** 2 < number:
        return _sqrt(number, mid, end)
    else:
        return _sqrt(number, start, mid)

