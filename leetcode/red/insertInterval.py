
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # edge cases - if the newInterval was not overlapping
            # if newInterval has smaller value than start value of intevals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # newInterval goes after the current interval but can still overlap
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # is overlapping
            else: 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res
            