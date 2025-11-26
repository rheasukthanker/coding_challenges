# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: List[int]) -> int:

        #length of height
        n=len(height) 
        l = 0
        r = n-1
        area = 0
        while l<r:
            area = max(area,(r-l)*min(height[r],height[l]))
            if height[r]>height[l]:
                l = l+1
            else:
                r = r-1
        return area