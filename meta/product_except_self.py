# TC: O(n), SC: O(1)
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] 
        for i in range(len(nums)-1, 0, -1):
            output.append(output[-1]*nums[i])
        output = output[::-1]
        left = 1
        for i in range(len(nums)):
            output[i] = output[i]*left
            left *= nums[i]
        return output
