'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.'''
class Solution:
    def isHappy(self, n: int) -> bool:
        sum_squares = 0
        iters = 0
        while sum_squares!=1:
            iters = iters+1
            li = list(str(n))
            sum_squares = 0
            for l in li:
                sum_squares +=int(l)**2
            n = sum_squares
            if sum_squares == 1:
                return True
            if iters == 100:
                break
        return False
