import heapq
from typing import List


def rearrange_digits(arr: list, builtin_sort=False) -> list:
    if not all(isinstance(elt, int) for elt in arr):
        raise TypeError("List contains non-integer element(s).")

    if any(map(lambda elt: elt > 9, arr)):
        raise ValueError("Math domain error.")

    if builtin_sort:
        arr = sorted(arr, reverse=True)
    else:
        arr = heapsort(arr)

    return list(map(list_to_int, [arr[::2], arr[1::2]]))


def heapsort(arr: list) -> list:
    arr = arr[:]
    sorted_arr = [None] * len(arr)

    # Employ heapsort
    heapq.heapify(arr)

    for reverse_idx in reversed(range(len(arr))):
        smallest = heapq.heappop(arr)
        sorted_arr[reverse_idx] = smallest
    
    return sorted_arr


def list_to_int(arr: List[int]) -> int:
    if len(arr) == 0:
        return
    return int("".join(map(str, arr)))