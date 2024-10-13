'''Given an array of positive integers nums and a positive integer target, return the minimal length of a  subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''
'''Time complexity: O(n).You may be thinking: there is an inner while loop inside another for loop, isn't the time complexity O(n**2))? The reason it is still O(n) is because the right pointer right can move n times and the left pointer left can move also n times in total. The inner loop is not running n times for each iteration of the outer loop. A sliding window guarantees a maximum of 2n window iterations. This is what is referred to as amortized analysis - even though the worst case for an iteration inside the for loop is O(n), it averages out to O(1) when you consider the entire runtime of the algorithm.'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0
