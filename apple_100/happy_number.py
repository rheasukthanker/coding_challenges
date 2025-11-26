#https://leetcode.com/problems/happy-number/
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