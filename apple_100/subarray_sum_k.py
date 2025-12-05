# https://leetcode.com/problems/subarray-sum-equals-k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        arrsum = 0
        hashmap[0]=1
        # [1,2,3] {0:1} k=3
        # arrsum = 1, {0:1,1:1}
        # arrsum = 3, count = 1, {0:1,1:1,3:1}
        # arrsum = 6, count = 2, {0:1,1:1,6:1} 
        for i, n in enumerate(nums):
            arrsum = arrsum + n
            if arrsum-k in hashmap:
               count = count +  hashmap[arrsum-k]
            hashmap[arrsum] = hashmap.get(arrsum,0) + 1
        return count