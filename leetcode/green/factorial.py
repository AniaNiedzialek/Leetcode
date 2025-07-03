class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        limit = 5
        
        while  n // limit > 0:
            count += n // limit
            limit *= 5
        return count
    
    
# test cases
solution = Solution()
print(solution.trailingZeroes(3))  # Expected: 0
print(solution.trailingZeroes(5))  # Expected: 1
print(solution.trailingZeroes(10))  # Expected: 2
print(solution.trailingZeroes(25))  # Expected: 6   