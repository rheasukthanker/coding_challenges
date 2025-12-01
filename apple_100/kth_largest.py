#https://leetcode.com/problems/kth-largest-element-in-an-array/
# quickselect O(n) avg case
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(arr,k):
            pivot = random.choice(arr)
            mid=[]
            left=[]
            right=[]
            for n in arr:
                if n>pivot:
                    left.append(n)
                elif n<pivot:
                    right.append(n)
                else:
                    mid.append(n)
            if k<=len(left):
                return quick_select(left,k)
            elif len(left)+len(mid)<k:
                return quick_select(right,k-len(left)-len(mid))
            return pivot      
        return quick_select(nums, k)