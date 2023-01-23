def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    pivot_idx = _find_pivot_idx(input_list, 0, len(input_list)-1)
    if pivot_idx == -1:
        raise ValueError("Pivot index could not be detected.")

    if input_list[0] <= number <= input_list[pivot_idx]:
        return _binary_search(input_list, 0, pivot_idx, number)

    elif input_list[pivot_idx+1] <= number <= input_list[-1]:
        return _binary_search(input_list, pivot_idx+1, len(input_list)-1, number)

    return -1


def _binary_search(input_list, start, stop, number):
    if start > stop:
        return -1

    mid = (start + stop) // 2

    if number > input_list[mid]:
        return _binary_search(input_list, mid+1, stop, number)
    elif number < input_list[mid]:
        return _binary_search(input_list, start, mid-1, number)
    else:
        return mid


def _find_pivot_idx(input_list, start, stop):
    # Base case
    if start >= stop:
        return -1
    
    mid = (start + stop) // 2
    if input_list[mid] > input_list[mid+1]:
        return mid

    if input_list[start] > input_list[mid]:
        # Left is rotated
        return _find_pivot_idx(input_list, start, mid)
    elif input_list[mid+1] > input_list[stop]:
        # Right is rotated
        return _find_pivot_idx(input_list, mid+1, stop)
    
    return -1


