from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        hashMap: dict[str, int] = defaultdict(int)
        
        for right in range(len(s)):
            hashMap[s[right]] += 1
            while (hashMap[s[right]] > 1):
                hashMap[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest
