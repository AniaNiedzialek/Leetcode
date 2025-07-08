
from typing import List


class Solution():
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        row, col = len(board), len(board[0])
        
        # dfs helper function
        def dfs(r, c, i):
            # base cases
            # 1 -  if out or range
            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            # 2 - if the element does not match
            if board[r][c] != word[i]:
                return False
            # 3 -  if the cell was already visited
            if (r, c) in seen:
                return False
            
            # 4 - if the end of the word was reached
            if i == len(word) - 1:
                return True
            # add to set
            seen.add((r, c))
            # check neighbors
            
            # make directions
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # check the dfs against the neighbor cells and the next element of the word
                if dfs(nr,nc, i + 1):
                    return True
            seen.remove((r, c))
            
            return False
                
                        
        # check the bounds of board and move to the next element of word
        for r in range(row):
            for c in range(col):
                # reset the set to start fresh
                seen = set()
                # check if dfs passes correctly, start at word[0]
                if dfs(r,c, 0):
                    return True
        return False
    
# test cases

sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(f"Test Case 1: ", sol.exist(board, word))
