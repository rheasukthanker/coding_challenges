# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i]=left
            left = left*nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            output[i]=output[i]*right
            right = right*nums[i]
        return output
        