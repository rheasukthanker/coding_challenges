"You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.Merge nums1 and nums2 into a single array sorted in non-decreasing order.The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer_1 = 0
        pointer_2 = 0
        merged_array = []
        while not (pointer_1==m and pointer_2==n):
            if pointer_1<m:
               a = nums1[pointer_1]
            else:
               a = 1e6
            if pointer_2<n:
               b = nums2[pointer_2]
            else:
               b = 1e6
            if a<b:
                merged_array.append(a)
                pointer_1 = pointer_1+1
            else:
                merged_array.append(b)
                pointer_2 = pointer_2+1
        for i in range(len(nums1)):
            nums1[i] = merged_array[i]
