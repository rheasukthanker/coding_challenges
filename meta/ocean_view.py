'''There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.'''
# Naive: iterate over a building and all buildings after it
# Advanced: Track max element, or use stack keeeping the max element
# TC: O(n), SC: O(1)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        len_h = len(heights)
        ocean_view = []
        '''for i in range(len_h):
            count = 0
            for j in range(i+1,len_h):
                if heights[i]>heights[j]:
                    count = count+1
            if count == len_h-i-1:
                ocean_view.append(i)
        return ocean_view'''
        max_len = -1e6
        for i in range(len_h-1,-1,-1):
            if heights[i]>max_len:
                max_len = heights[i]
                ocean_view.append(i)
        return ocean_view[::-1]



