def linear_search(arr, target):
    # Your code here
    for x in range(len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high + low) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1  # not found
