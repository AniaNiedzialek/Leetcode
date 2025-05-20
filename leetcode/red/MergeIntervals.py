from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort the input
        # new list
        merged = []
      

        # sort by the starting point with key
        # lambda function tells how to sort, sorting the intervals by the first point ascending
        intervals.sort(key = lambda interval: interval[0])
     
        
        for interval in intervals:
            # if we haven't merged any or the intervals does not overlap (if we end before the next one start)
            if not merged or merged[-1][1] < interval [0]:
                # add the interval
                merged.append(interval)
            else:
                # we have overlap - modify the overlap that starts at the same spot, and the end point is the max 
                # of what we currently have
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged
            
        # time: O (n log n)
        # space: O(n)
        
# test cases:
solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution.merge(intervals))
intervals = [[1,3],[0,6],[8,10],[5,18]]
print(solution.merge(intervals))
intervals = [[1,4],[4,5]]
print(solution.merge(intervals))
intervals = [[1,4],[0,0]]
print(solution.merge(intervals))
intervals = [[1,3], [2,6] ,[8,10] ,[8,9], [9,11],[15,18], [2,4] ,[16,17]]
print(solution.merge(intervals))