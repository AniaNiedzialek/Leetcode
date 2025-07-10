from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            new_row = matrix[r]
            for c in range(col):
            
                left = 0
                right = len(new_row) - 1
                
               
                while left <= right:
                    middle = (left + right) // 2
                    if target == new_row[middle]:
                        return True
                    elif target < new_row[middle]:
                        right = middle - 1
                    else:
                        left = middle + 1
             
        return False