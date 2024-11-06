'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # Find first instance of target (a)
        a = 0
        b = n - 1
        while a <= b:
            mid = ((b - a) // 2) + a
            if nums[mid] < target:
                a = mid + 1
            else:
                b = mid - 1

        # No instance of target at all
        if a == n or nums[a] != target:
            return [-1, -1]

        # Find last instance of target (d)
        c = a
        d = n - 1
        while c <= d:
            mid = ((d - c) // 2) + c
            if nums[mid] <= target:
                c = mid + 1
            else:
                d = mid - 1

        return [a, d]
