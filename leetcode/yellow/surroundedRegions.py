from typing import List
import collections


class Solution():
    def solve(self, board: List[List[str]]) -> None:
        
        # test case
        if not board:
            board = [[""]]
            
        
        rows, cols = len(board), len(board[0])
        seen = set()
        
        
        # bfs
        def bfs(r, c):
            q = collections.deque()
            
            seen.add((r,c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [(0,1), (1,0), (-1, 0), (0,-1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in seen):
                        board[nr][nc] = "X"
                        q.append((nr,nc))
                        seen.add((nr, nc))
        
        
        # iterate through the board
        # step 1: check top and bottom
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in seen:
                    bfs(r,c)
                                        
        # step 2 - check left and right
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == "O" and (r, c) not in seen:
                    bfs(r, c)
        
        # step 3 - check the rest of the board
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O" and (r, c) not in seen:
                    bfs(r, c)
                    # replace the node if its connected
                    board[r][c] = "X"
                    
            
# test cases
solution = Solution()
board1 = [["X"]]
solution.solve(board1) # Expected: [X]
print(board1)

