'''Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Complexity
Time complexity:
O(k * log(min(n1, n2))), where n1 and n2 are the lengths of nums1 and nums2. The loop runs k times, and each iteration involves heap operations, which take log(min(n1, n2)) time.

Space complexity:
O(min(k, n1 * n2)) for the heap and the result list.

'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k_smallest = []
        n1, n2 = len(nums1), len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]
        for _ in range(k):
            _, i, j = heapq.heappop(heap)
            k_smallest.append([nums1[i], nums2[j]])

            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
            if j == 0 and i + 1 < n1:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
        
        return k_smallest

