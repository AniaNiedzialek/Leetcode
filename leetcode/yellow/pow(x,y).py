class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = 1 
        # base case if n is negative
        # 
        if n < 0:
            x = 1 / x
            n = -n
    
        # otherwise, we can use the same logic
        while n > 0:
            if n % 2 == 1:
                result *= x 
            x *= x     
            n //= 2
    
        return result
    
# test cases
solution = Solution()
print(solution.myPow(2.00000, 10))  # Expected: 1024.00000
print(solution.myPow(2.10000, 3))   # Expected: 9.26100
print(solution.myPow(2.00000, -2))  # Expected: 0.25000
print(solution.myPow(2.0, 3))  # Expected: 8.0 