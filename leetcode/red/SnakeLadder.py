from typing import List
import collections
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        # reverse the board
        board.reverse()

        def intToPosition(square):
            # TODO
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c

            return [r,c]
        
        q = deque() # [square, moves]
        q.append([1, 0])
        # hashset
        visit = set()

        while q:
            square, moves = q.popleft()

            # rolling a dice - not inclusive with 7
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPosition(nextSquare)
                if board[r][c] != -1:
                    # check the value since it is a special case
                    nextSquare = board[r][c]

                # check if solition
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1

# ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from LeetCode
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print("Test case 1:", solution.snakesAndLadders(board1))  # Expected: 4

    # Test case 2: No snakes or ladders, 2x2 board
    board2 = [
        [-1, -1],
        [-1, -1]
    ]
    print("Test case 2:", solution.snakesAndLadders(board2))  # Expected: 1

    # Test case 3: Impossible to reach the end
    board3 = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, 9, -1]
    ]
    print("Test case 3:", solution.snakesAndLadders(board3))  # Expected: 1

    # Test case 4: Only one cell
    board4 = [[-1]]
    print("Test case 4:", solution.snakesAndLadders(board4))  # Expected: 0