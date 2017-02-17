# fast inversions

def fast_inversions(arr):
    return sort_and_count(arr)[1]

def sort_and_count(arr):
    if len(arr) == 1:
        return (arr, 0)
    else:
        mid = int(len(arr) / 2)
        left, left_count = sort_and_count(arr[:mid])
        right, right_count = sort_and_count(arr[mid:])
        sorted_arr, split_count = merge_and_count_split(left, right)
        return (sorted_arr, left_count + right_count + split_count)

def merge_and_count_split(left, right):
    merged = []
    splits = 0
    while (len(left) > 0 and len(right) > 0):
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            splits += len(left)
            merged.append(right.pop(0))
    return (merged + left + right, splits)
