from typing import List

class Solution:
    def permute(self, nums: List[str]) -> List[str]:
        
        # result
        res = []
        
        # function backtracking
        def back(path, used):
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return
           
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                back(path, used)
                path.pop()
                
                used[i] = False
            
            
        back([], [False] * len(nums))
        return res
    
    