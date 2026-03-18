
arr = [False, False, False, True, True]

target = False

# Out intention is to find the first False in the array


def monotonic_binary_search(arr, target) -> int:

    left, right = 0, len(arr) - 1
    first_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first_idx = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return first_idx



res = monotonic_binary_search(arr=arr, target=target)

print(res)

print("------------------------------------------")

arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

target2 = 8


def binary_search(arr, target) -> int:
    
    left, right = 0, len(arr) - 1


    while (left <= right):
        mid = (right + left) // 2

        if (arr[mid] == target):
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    

    return -1



res2 = binary_search(arr=arr2, target=target2)

print(res2)


print(arr2[8])

