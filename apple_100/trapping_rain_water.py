#https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        right_max, left_max = 0,0
        area = 0
        while left<right:
            if height[left]<height[right]:
                left_max = max(left_max,height[left])
                area = area + left_max - height[left]
                left = left+1
            else:
                right_max = max(right_max,height[right])
                area = area + right_max - height[right]
                right = right-1

        return area