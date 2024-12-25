'''Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.'''
# TC: O(logn) SC: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            # arr[pivot] - pivot - 1 represents number of missing elements at an index
            # [2,4,6,10] -> orig array
            # [1,2,3,4] -> no missing array
            # [1,2,3,6] -> num missing at index = arr[i]-1-1
            # Find 5th missing 
            # after search return 2+5+1 = 8
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return k+right+1
