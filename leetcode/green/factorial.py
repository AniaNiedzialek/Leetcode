class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        limit = 5
        
        while  n // limit > 0:
            count += n // limit
            limit *= 5
        return count
    