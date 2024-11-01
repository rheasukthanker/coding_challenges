'''Given a positive integer n, write a function that returns the number of  set bits in its binary representation (also known as the Hamming weight).'''
 
 class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n!=0:
            cnt += (n % 2)
            n >>= 1
        return cnt
