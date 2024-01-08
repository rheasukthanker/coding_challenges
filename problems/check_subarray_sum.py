'''Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.'''
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        d[0] = -1
        sums = 0
        for i in range(len(nums)):
            sums+=nums[i]
            if(k!=0):
                sums = sums%k
            if(sums in d):
                if(i-d[sums]>1):
                    return(True)
            else:
                d[sums] = i

        return(False)
