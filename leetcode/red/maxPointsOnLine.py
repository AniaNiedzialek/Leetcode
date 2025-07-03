from typing import List
import collections  


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1

        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                res = max(res, count[slope] + 1)

        return res


# test cases
solution = Solution()
print(solution.maxPoints([[1, 1], [2, 2], [3, 3]]))  # Expected: 3
print(solution.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [     2, 3], [1, 4]]))  # Expected: 4 