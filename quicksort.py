def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quicksort(left_side) + [pivot] + quicksort(right_side)

test_arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quicksort(test_arr))