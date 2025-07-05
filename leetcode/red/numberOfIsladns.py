from typing import List
import collections 
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # get dimensions
        rows, cols = len(grid), len(grid[0])
        # print(rows)
        # print(cols)

        visit = set()
        # we could use 2D grid or sets
        islands = 0

        # bfs - queue, iterative not recursive
        # we need data structure for memory
        def bfs(r, c):
            q = collections.deque()
            # mark as visited
            visit.add((r, c))
            # add to the queue
            q.append((r,c))

            while q:
                # expand the island
                row, col = q.popleft()
                # for dfs
                # row, col = q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # check if in bounds
                    if (r in range(rows) and c in range (cols) and grid[r][c] == "1" and (r, c ) not in visit):
                        q.append((r , c))
                        visit.add((r , c))




        # visit every position in grid interate through rows and column
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    # BFS on col
                    bfs(r,c)
                    # if islands was not visited
                    islands += 1
        return islands
        
# test cases
solution = Solution()   
print(solution.numIslands([["1", "1", "0", "0", "0"]]))    # Expected: 1
print(solution.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))  # Expected: 3
print(solution.numIslands([["1", "1", "1", "1", "0"], ["1", "0", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"], ["0", "1", "1", "1", "1"]]))  # Expected: 2







