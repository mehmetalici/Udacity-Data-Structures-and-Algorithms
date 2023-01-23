import random
from problem_4 import sort_012


def test_huge_inputs():
    huge_input = random.choices([0, 1, 2], k=10**6)
    _test_valid(huge_input)


def test_regular_inputs():
    regular_input1 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    regular_input2 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    regular_input3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

    for arr in [regular_input1, regular_input2, regular_input3]:
        _test_valid(arr)


def test_garbage_inputs():
    empty_arr = []
    out_of_bounds_arr = [1, 2, 3, 4, 5]
    different_type_arr = ["livin'", "la", "vida", "loca"]
    
    for arr in [out_of_bounds_arr, different_type_arr]:
        _test_invalid(arr)
    _test_valid(empty_arr)


def _test_valid(arr):
    result = sort_012(arr)
    solution = sorted(arr)

    if result == solution:
        print("Pass")
    else:
        print("Fail")


def _test_invalid(arr, expected_exception=Exception):
    try:
        sort_012(arr)
    except expected_exception:
        print("Pass")
        return
    print("Fail")


if __name__ == "__main__":
    test_huge_inputs()
    test_regular_inputs()
    test_garbage_inputs()