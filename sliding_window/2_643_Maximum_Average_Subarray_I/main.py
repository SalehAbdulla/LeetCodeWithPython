from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg_window = sum(nums[:k])
        max_avg_window = avg_window

        for left in range(k, len(nums)):
            avg_window -= nums[left-k]
            avg_window += nums[left]
            max_avg_window = max(max_avg_window, avg_window)

        return max_avg_window / k
