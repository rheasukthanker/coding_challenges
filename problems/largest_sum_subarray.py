import sys
 # Find the largest sum of a subarray of size k 
class Solution():
    def maxSumWithK(self, a, n, k):
        sum = 0
        for i in range(k):
            sum += a[i]
        last = 0
        j = 0
        ans = -sys.maxsize - 1
        ans = max(ans, sum)
        for i in range(k, n):
            sum = sum + a[i]
            last = last + a[j]
            j += 1
            ans = max(ans, sum)
            if(last < 0):
               sum = sum-last
               ans = max(ans, sum)
               last = 0
        return ans 
