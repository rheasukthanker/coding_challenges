# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_all = []
        start_1 = 0
        start_2 = 0
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        while start_1<len_nums1 or start_2<len_nums2:
              if start_1==len_nums1:
                while start_2<len_nums2:
                    nums_all.append(nums2[start_2])
                    start_2 = start_2 + 1
                continue
              if start_2==len_nums2:
                while start_1<len_nums1:
                    nums_all.append(nums1[start_1])
                    start_1 = start_1 + 1
                continue
              if nums1[start_1]<nums2[start_2]:
                nums_all.append(nums1[start_1])
                start_1 = start_1+1
              else:
                nums_all.append(nums2[start_2])
                start_2 = start_2+1
        len_nums_all = len_nums1 + len_nums2
        if len_nums_all%2==1:
            return nums_all[len_nums_all//2]
        else:
            return (nums_all[(len_nums_all-1)//2] + nums_all[(len_nums_all)//2])/2
