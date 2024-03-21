class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        cur = 0
        prev = 0
        curchar = None
        for c in s:
            if curchar != c:
                prev = cur
                curchar = c
                cur = 1
            else:
                cur += 1
            if cur <= prev: ans += 1
        return ans
