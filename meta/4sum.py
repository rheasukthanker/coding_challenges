# TC: O(n**2), SC: O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dupsi = set()
        results = set()
        seen = {}
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] not in dupsi:
                dupsi.add(nums[i])
            else:
                continue
            for j in range(i+1,len_nums):
                for k in range(j+1,len_nums):
                    complement = target-nums[i]-nums[j]-nums[k]
                    if complement in seen and seen[complement][0] == i and seen[complement][1] == j:
                        pair = sorted((nums[i],nums[j],nums[k],complement))
                        results.add(tuple(pair))
                    else:
                        seen[nums[k]] = [i,j]
        return list(results)
 # TC: O(n**2), SC: O(1)               
'''class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []

        for i in range(n):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Two-pointer approach for remaining two numbers
                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Skip duplicates for the third and fourth numbers
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return results'''
