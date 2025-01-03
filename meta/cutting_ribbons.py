'''You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your task is to determine the maximum length of ribbon, x, that allows you to cut at least k ribbons, each of length x. You can discard any leftover ribbon from the cuts. If it is impossible to cut k ribbons of the same length, return 0.'''
# Idea naive: We want to traverse through all possible lengths of ribbions from 0 to max(ribbons), and return the largest ribbon length after which cutting ribbons into larger pieces does not lead to k pieces. Larger length corresponds to fewer pieces and smaller length corresponds to more pieces. This is a monotonic function hence an ideal candidate for binary search
# Idea advanced: Use binary search to reduce the O(m) (m= max ribbon length) to O(logm) by using binary search, Within each binary search iteration we use O(n) to check if a cut length is valid. A cut length l, is valid if total pieces of length l after cutting are equal to or exceed k. 
# TC: O(nlogm)
# SC: O(1)
# https://leetcode.com/problems/cutting-ribbons/
class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        right = max(ribbons)
        left = 0
        while left < right:
            mid = (right + left + 1) // 2
            total_ribbons = 0
            for r in ribbons:
                total_ribbons += r // mid  # Fix accumulation
            if total_ribbons >= k:
                left = mid   # Adjust to progress loop
            else:
                right = mid - 1
        return left  # Return the largest valid mid

class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        # Binary search bounds
        left = 0
        right = max(ribbons)

        # Perform binary search on the ribbon length
        while left < right:
            middle = (
                left + right + 1
            ) // 2  # Use upper mid to prevent infinite loops
            if self._is_possible(middle, ribbons, k):
                # If it's possible to make `k` pieces of length `middle`, search the higher range
                left = middle
            else:
                # Otherwise, search the lower range
                right = middle - 1

        return left

    def _is_possible(self, x: int, ribbons: list[int], k: int) -> bool:
        total_ribbons = 0
        for ribbon in ribbons:
            # Number of pieces the current ribbon can contribute
            total_ribbons += ribbon // x
            # If the total reaches or exceeds `k`, we can stop early
            if total_ribbons >= k:
                return True
        # It's not possible to make the cut
        return False
