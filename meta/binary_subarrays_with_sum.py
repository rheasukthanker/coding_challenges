'''Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.'''

# prefixsum
# TC:O(n) SC: O(n)
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0: 1}  # Initialize prefix sum count with 0
        prefix_sum = 0
        num_arrs = 0
        
        for n in nums:
            prefix_sum += n
            # Check if prefix_sum - goal exists in d
            if prefix_sum - goal in d:
                num_arrs += d[prefix_sum - goal]
            
            # Update the prefix sum count in the dictionary
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1
        
        return num_arrs
        
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        # {prefix: number of occurrence}
        freq = {}  # To store the frequency of prefix sums

        for num in nums:
            current_sum += num
            if current_sum == goal:
                total_count += 1

            # Check if there is any prefix sum that can be subtracted from the current sum to get the desired goal
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return total_count
#sliding window one pass
# TC: O(n), SC: O(1)
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start = 0
        prefix_zeros=0
        current_sum = 0
        total_arrs = 0
        for end,n in enumerate(nums):
            current_sum = current_sum+n
            while start<end and (nums[start]==0 or current_sum>goal):
                if nums[start]==1:
                    prefix_zeros=0
                else:
                    prefix_zeros=prefix_zeros+1
                current_sum = current_sum-nums[start]
                start=start+1
            if current_sum==goal:
                total_arrs=total_arrs+1+prefix_zeros
        return total_arrs
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start = 0
        prefix_zeros = 0
        current_sum = 0
        total_count = 0
        
        # Loop through the array using end pointer
        for end, num in enumerate(nums):
            # Add current element to the sum
            current_sum += num
            
            # Slide the window while condition is met
            while start < end and (nums[start] == 0 or current_sum > goal):
                if nums[start] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1
                
                current_sum -= nums[start]
                start += 1
                
            # Count subarrays when window sum matches the goal
            if current_sum == goal:
                total_count += 1 + prefix_zeros  
                
        return total_count
