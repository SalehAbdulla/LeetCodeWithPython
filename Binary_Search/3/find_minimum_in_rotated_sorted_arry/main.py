from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        boundry_index = -1

        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                boundry_index = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return nums[boundry_index]
        

nums = [4,5,6,7,0,1,2]
expected = 0

res = Solution().findMin(nums)
if (res != expected):
    print("error")
else:
    print("success")

