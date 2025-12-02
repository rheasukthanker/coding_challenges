#https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        i = 0
        n = len(intervals)
        start = -1
        end = -1
        while i<n and newInterval[0]>intervals[i][1]:
            new_intervals.append(intervals[i])
            i = i+1
        while i<n and newInterval[1]>=intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i = i+1
        new_intervals.append(newInterval)
        while i<n:
            new_intervals.append(intervals[i])
            i = i+1
        return new_intervals
