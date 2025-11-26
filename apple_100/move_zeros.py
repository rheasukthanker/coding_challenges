# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        if set(nums)=={0}:
            return nums
        
        count=0
        while i<len(nums)-1:
            if nums[i]==0:
                nums[(i):(len(nums)-1)]=nums[i+1:]
                nums[len(nums)-1]=0
            #print(nums[i])
            if nums[i]!=0:
               i=i+1
            count=count+1
            if count==len(nums):
                break