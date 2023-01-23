import random
from problem_6 import get_min_max


def test_regular_inputs():
    print("Testing regular inputs...")
    for _ in range(5):
        nums = random.choices(range(10), k=10)
        _test_valid(nums)


def test_huge_inputs():
    print("Testing huge inputs...")
    for _ in range(5):
        huge_nums = random.choices(range(10), k=10**6)
        _test_valid(huge_nums)


def test_edge_inputs():
    print("Testing edge inputs...")

    invalid_arr = list("Varien") + [1.5, 2.5, set()]
    empty_arr = []
    for arr in [invalid_arr, empty_arr]:
        _test_invalid(arr, ValueError)


def _test_invalid(arr, expected_exception=Exception):
    actual_exception = None
    try:
        get_min_max(arr)
    except expected_exception:
        print("Pass")
        return
    except Exception as e:
        actual_exception = e
    print(f"Fail: Expected: {expected_exception}, Actual: {actual_exception}")
    

def _test_valid(arr):
    expected = (min(arr), max(arr))
    actual = get_min_max(arr)
    if expected == actual:
        print("Pass")
    else:
        print(f"Fail: Expected: {expected}, Actual: {actual}")


if __name__ == "__main__":
    test_regular_inputs()
    test_edge_inputs()
    test_huge_inputs()