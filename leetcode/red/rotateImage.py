from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l): # l, r - 1
                top, bottom = l, r
                
                # save the topleft - in temp variable
                topLeft = matrix[top][l + i]

                # move the bottom left to the top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right to bottom left - reverse order
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left to top right
                matrix[top + i][r] = topLeft

                
            r -= 1
            l += 1

            