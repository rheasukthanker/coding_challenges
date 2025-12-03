#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(n) time and O(1) space
        '''start_index = -1
        end_index = -1
        for i,n in enumerate(nums):
            if n==target and start_index==-1:
                start_index = i
            if n==target and start_index!=-1:
                end_index = i
        return [start_index,end_index]'''
        # O(log(n)) time and O(1) space
        start_index = -1
        end_index = -1
        start = 0
        end = len(nums)-1
        # first search find start index
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                if mid==start or nums[mid-1]<target:
                    start_index=mid
                    break
                else:
                    end = mid -1
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
        if start_index==-1:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                if mid==end or nums[mid+1]>target:
                    end_index=mid
                    break
                else:
                    start = mid+1
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
        return [start_index,end_index]