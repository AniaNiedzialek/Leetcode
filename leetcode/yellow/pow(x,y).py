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
            n -= 1
    
        return result