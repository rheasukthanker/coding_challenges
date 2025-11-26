# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        len_intervals = len(intervals)
        intervals_merged = [intervals[0]]
        for i in range(1,len_intervals):
            low, high = intervals[i]
            if intervals_merged[-1][-1]>=low and high<=intervals_merged[-1][-1]:
                continue
            if intervals_merged[-1][-1]>=low and high>intervals_merged[-1][-1]:
                intervals_merged[-1][-1] = high
            else:
                intervals_merged.append([low,high])
        return intervals_merged
