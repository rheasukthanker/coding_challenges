#https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
# 
from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        ans = 0 
        for k, v in freq.items(): 
            if target.startswith(k): 
                suffix = target[len(k):]
                ans += v * freq[suffix]
                if k == suffix: ans -= freq[suffix]
        return ans 