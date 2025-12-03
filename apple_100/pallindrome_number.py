# https://leetcode.com/problems/palindrome-number/
# Time O(log(n))
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        reverted_number=0
        x_orig = x
        while x>0:
            reverted_number = reverted_number*10+x%10
            x = x//10
        return reverted_number==x_orig 