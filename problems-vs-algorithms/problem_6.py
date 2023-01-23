from typing import List


def _contains_nonint(arr: list) -> bool:
    if not all(isinstance(elt, int) for elt in arr):
        return True
    return False


def get_min_max(nums: List[int]) -> tuple:
    if _contains_nonint(nums):
        raise ValueError("nums contains non-ints.")
    if len(nums) == 0:
        raise ValueError("nums is an empty sequence.")

    num_min = nums[0]
    num_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > num_max:
            num_max = nums[i]
        if nums[i] < num_min:
            num_min = nums[i]
    
    return (num_min, num_max)

