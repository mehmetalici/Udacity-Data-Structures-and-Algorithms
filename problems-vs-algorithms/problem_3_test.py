from problem_3 import rearrange_digits
import random


def test_huge_inputs():
    huge_arr = random.choices(range(10), k=10**6)
    _test_valid(huge_arr)


def test_invalid_inputs():
    not_int_arr = [1, 2.5, 3, "just_a_string"]
    out_of_bounds_arr = [100, 200]
    _test_invalid(not_int_arr, expected_exception=TypeError)
    _test_invalid(out_of_bounds_arr, expected_exception=ValueError)


def test_regular_inputs():
    regular_input1 = [1, 2, 3, 4, 5]
    regular_input2 = [4, 6, 2, 5, 9, 8]
    test_valid(regular_input1, regular_input2)


def _test_invalid(numbers, expected_exception):
    try:
        rearrange_digits(numbers)
    except expected_exception:
        print("Pass")
        return
    print("Fail")


def _test_valid(numbers):
    output = rearrange_digits(numbers)
    solution = rearrange_digits(numbers, builtin_sort=True)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_huge_inputs()
    test_invalid_inputs()
    test_regular_inputs()