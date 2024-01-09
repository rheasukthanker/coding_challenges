#https://leetcode.com/problems/combination-sum-ii/, subarrays which sum to target with no duplication
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        helper = []
        self.findAns(0, target, candidates, ans, helper)
        return ans
    
    def findAns(self, index, target, arr, ans, helper):
        if target == 0:
            ans.append(helper[:])
            return
        
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue
            if arr[i] > target:
                break
            helper.append(arr[i])
            self.findAns(i + 1, target - arr[i], arr, ans, helper)
            helper.pop()
