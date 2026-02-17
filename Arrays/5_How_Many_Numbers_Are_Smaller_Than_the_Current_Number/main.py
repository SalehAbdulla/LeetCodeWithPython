class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # [4, 5, 6, 8]
        numsSorted = sorted(nums)
        #print(numsSorted)
        
        # {4:0, 5:1, 6:2, 8:3}
        hashMap = {}

        for i, v in enumerate(numsSorted):
            if v not in hashMap:
                hashMap[v] = i
        
        #print(hashMap)
        
        res = []

        for i, v in enumerate(nums):
            res.append(hashMap[v])

        return res

        