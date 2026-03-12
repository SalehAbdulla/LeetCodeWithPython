from typing import List

# make the max window
def subarray_sum_fixed(nums: List[int], k: int) -> int:
    
    window_sum = sum(nums[:k])
    max_window = window_sum

    for left in range(k, len(nums)):
        # remove_left
        window_sum -= nums[left-k]
        # add_left
        window_sum += nums[left]
        # whos that SMART MAN
        max_window = max(window_sum, max_window)


    return max_window

nums = [1, 2, 3, 7, 4, 1]
k = 3

res = subarray_sum_fixed(nums, k)
print(res)

