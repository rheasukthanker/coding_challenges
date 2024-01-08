class Solution:
    def findKthLargest(self, nums, k):
        return self.quick_select(nums, k)

    def quick_select(self, nums, k):
        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)
        
        if k <= len(left):  # kth is in the left side
            return self.quick_select(left, k)

        if k <= len(left) + len(mid):  # kth is in the middle
            return pivot

        return self.quick_select(right, k - len(left) - len(mid))
