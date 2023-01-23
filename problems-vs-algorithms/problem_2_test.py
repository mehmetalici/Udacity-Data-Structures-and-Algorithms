"""
Test module for Problem 2. 
TODO: Use a framework for testing
"""

from problem_2 import rotated_array_search
import random


def test_huge_inputs():
    print("Testing huge inputs...")
    huge_input_1 = list(range(10 ** 5, 10 ** 8, 75)) + list(range(0, 10 ** 4, 10))
    huge_input_2 = list(range(235, 10 ** 4, 24)) + list(range(-10 ** 4, 0, 125))

    _test_valid((huge_input_1, 10**5))
    _test_valid((huge_input_2, -10**4))


def test_regular_inputs():
    print("Testing regular inputs...")
    _test_valid([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    _test_valid([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    _test_valid([[6, 7, 8, 1, 2, 3, 4], 8])
    _test_valid([[6, 7, 8, 1, 2, 3, 4], 1])
    _test_valid([[6, 7, 8, 1, 2, 3, 4], 10])


def test_invalid_inputs():
    print("Testing invalid values...")
    identical_values = [1] * 100
    sorted_array = sorted(random.choices(range(100), k=100))
    _test_invalid(identical_values, identical_values[0], exception=ValueError)
    _test_invalid(sorted_array, sorted_array[0], exception=ValueError)


def _linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
        

def _test_valid(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if _linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def _test_invalid(input_list, number, exception):
    try:
        rotated_array_search(input_list, number)
    except exception:
        print("Pass")
        return

    print("Fail")


if __name__ == "__main__":
    test_huge_inputs()  # Expected: Pass 2x
    test_invalid_inputs()  # Expected: Pass 2x
    test_regular_inputs()  # Expected: Pass 5x

