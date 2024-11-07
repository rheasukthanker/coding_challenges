'''A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr=float('inf')
        mins=float('inf')
        curr1=float('-inf')
        maxs1=float('-inf')
        total=0
        for i in nums:
            curr1=max(curr1+i,i)
            maxs1=max(maxs1,curr1)
            total+=i
            curr=min(curr+i,i)
            mins=min(mins,curr)
        if (mins==total) :
            return maxs1
        return max(maxs1,total-mins)
