from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort the input
        # new list
        merged = []
      

        # sort by the starting point with key
        intervals.sort(key = lambda interval: interval[0])
     
        for interval in intervals:
            if not merged or merged[-1][1] < interval [0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged
            
        # time: O (n log n)
        # space: O(n)
        
# test cases:
solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution.merge(intervals))