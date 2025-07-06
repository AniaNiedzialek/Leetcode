from typing import List

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