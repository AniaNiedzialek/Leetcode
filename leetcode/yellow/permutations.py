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
    
# test cases
sol = Solution()
nums = [1,2,3]
print("Test Case 1: ", sol.permute(nums))
    
    