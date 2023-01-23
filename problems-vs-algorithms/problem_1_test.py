import problem_1
import math


def _test_valid(number):
    actual = problem_1.sqrt(number)
    expected = math.floor(math.sqrt(number))
    print("Pass" if  (expected == actual) else "Fail")


def _test_invalid(number, exception):
    try:
        problem_1.sqrt(number)
    except exception:
        try:
            math.sqrt(number)
        except exception:
            print("Pass")
            return
    
    print("Fail")


def test_big_inputs():
    print("Testing big inputs...")
    number = 10 ** 6
    _test_valid(number)


def test_invalid_inputs():
    print("Testing invalid inputs...")
    math_invalid_input = -5
    type_invalid_input = "varien"
    _test_invalid(math_invalid_input, ValueError)
    _test_invalid(type_invalid_input, TypeError)


def test_regular_inputs():
    print("Testing regular inputs...")
    candidates = [0, 1, 9, 16, 27]
    for candidate in candidates:
        _test_valid(candidate)


if __name__ == "__main__":
    test_big_inputs()  # Expected: 1x Pass
    test_invalid_inputs()  # Expected: 2x Pass
    test_regular_inputs()  # Expected: 5x Pass