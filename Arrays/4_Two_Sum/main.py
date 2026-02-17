class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}

        for i, v in enumerate(nums):
            complement = target - v
            if complement in hashMap:
                return [hashMap[complement], i]
            
            hashMap[v] = i
        
        return [-1, -1]
