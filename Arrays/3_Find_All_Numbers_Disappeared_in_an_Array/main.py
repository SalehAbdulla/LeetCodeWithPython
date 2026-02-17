class Solution(object):
    def findDisappearedNumbers(self, nums):
        numsSet = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in numsSet:
                res.append(i)
        return res
        