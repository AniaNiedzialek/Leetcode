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
    
    
# test cases
# ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Target is present
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    print(solution.searchMatrix(matrix1, 3))  # Expected: True

    # Test case 2: Target is not present
    print(solution.searchMatrix(matrix1, 13))  # Expected: False

    # Test case 3: Single row, target present
    matrix2 = [[1, 2, 3, 4, 5]]
    print(solution.searchMatrix(matrix2, 4))  # Expected: True

    # Test case 4: Single column, target not present
    matrix3 = [[1], [3], [5]]
    print(solution.searchMatrix(matrix3, 2))  # Expected: False

