from typing import List

class Solution: 
    def combine(self, n: int, k : int) -> List[str]:
        
        
        # declare the result list
        res = []
        
        # backtracking function(start point, current combination)
        def back(start, comb):
            # base case - when to stop
            if len(comb) == k:
                res.append(comb.copy())
                
            # otherwise
            for i in range(start, n + 1):
                comb.append(i)
                back(i + 1, comb)
                comb.pop()
                
        back(1, [])
        return res