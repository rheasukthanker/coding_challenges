'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.'''
# https://leetcode.com/problems/trapping-rain-water/
# TC O(n) SC: O(1)
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if left_max - height[left]>0:
                    ans += left_max - height[left]
                left_max = max(left_max, height[left])
                left += 1
            else:
                if right_max - height[right]>0:
                   ans += right_max - height[right]
                right_max = max(right_max, height[right])
                right -= 1
        return ans
