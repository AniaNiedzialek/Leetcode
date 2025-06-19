from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()


        print(points)
        res = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]

            # case 1 - if overlapping
            print(curr[0])
            print(f"prev is {prev[1]}")
            if curr[0] <= prev[1]:
                print(f"hello")
                # adjust result - number of arrows
                res -= 1
                # adjust prev
                prev = [curr[0], min(curr[1], prev[1])]
                print(f"new prev is {prev}")
            # case 2 - not overlapping
            else:
                prev = curr
        return res