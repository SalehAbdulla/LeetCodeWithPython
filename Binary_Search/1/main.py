from typing import List


arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109,110]


def binary_search(arr: List[int], target: int) -> int:

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


    return -1


res = binary_search(arr, 106)
print(res)

