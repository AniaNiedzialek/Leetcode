from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every value in the top row
            for i in range(left, right):
                # right is out of bounds so it can iterate including the actual right
                res.append(matrix[top][i])
            top += 1

            # get every item in the right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1]) #right ou of bounds
            right -= 1
        
            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1): #from right to left in reverse order - use -1
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res



