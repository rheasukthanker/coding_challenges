'''You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        start = nums[0]
        end = nums[0]
        res =[]
        for i in range(1,len(nums),1):
            print(i)
            if nums[i] != nums[i-1] +1:
                if start == end:
                    res.append(f'{start}')
                else:
                    res.append(f'{start}->{end}')
                start=nums[i]
                end=nums[i]
            else:
                end = nums[i]
                
        if start!=end and f'{start}->{end}' not in res:
            res.append(f'{start}->{end}')
        elif f'{end}' not in res:
            res.append(f'{end}')
        return res
