# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        num_bits = 0
        while n!=0:
            bit = n%2
            n = n//2
            if bit==1:
                num_bits = num_bits +1
        return num_bits