#https://leetcode.com/problems/top-k-frequent-elements/
# O(Nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n,0)+1
        frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        keys = list(frequency.keys())
        top_keys = []
        for i in range(k):
            top_keys.append(keys[i])
        return top_keys
    
# Avg O(n), worst case O(n**2), quickselect algorithm
from collections import Counter
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index)->int:
            frequency_pivot = count[unique[pivot_index]]
            unique[right], unique[pivot_index] = unique[pivot_index], unique[right]
            store_index = left
            for i in range(store_index,right):
                if count[unique[i]]<frequency_pivot:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index = store_index+1
            unique[right], unique[store_index] = unique[store_index], unique[right]
            return store_index

        def quickselect(left, right, k_smallest)->int:
            # base case
            if left==right:
                return
            pivot_index = random.randint(left,right)
            pivot_index = partition(left, right, pivot_index)
            if pivot_index==k_smallest:
                return
            elif pivot_index<k_smallest:
                quickselect(pivot_index+1,right,k_smallest)
            else:
                quickselect(left,pivot_index-1,k_smallest)
        n = len(unique)
        quickselect(0,n-1,n-k)
        return unique[n-k:]

    
