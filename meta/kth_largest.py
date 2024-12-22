'''Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?'''

# min heap
'''Initialize a min-heap heap.
Iterate over the input. For each num:
Push num onto the heap.
If the size of heap exceeds k, pop from heap.
Return the top of the heap.'''
# TC: O(nlogk) SC: O(k)
class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

# Quickselect, also known as Hoare's selection algorithm, is an algorithm for finding the k th smallest element in an unordered list. It is significant because it has an average runtime of O(n).
'''Define a quickSelect function that takes arguments nums and k. This function will return the k th greatest element in nums (the nums and k given to it as input, not the original nums and k). Select a random element as the pivot. Create left, mid, and right as described above. If k <= left.length, return quickSelect(left, k). If left.length + mid.length < k, return quickSelect(right, k - left.length - mid.length). Otherwise, return pivot. Call quickSelect with the original nums and k, and return the answer.'''
# TC(avg) : O(n), TC(worst): O(n**2), SC: O(n)
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)
