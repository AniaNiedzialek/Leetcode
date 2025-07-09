from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def back(start, path, target):
            # base cases:
            if target == 0:
                res.append(path.copy())
            if target < 0:
                return

            # otherwise
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                back(i, path, target - candidates[i])
                path.pop()




        back(0, [], target)
        return res
    
# test cases
sol = Solution()
target = 7
candidates = [2,3,6,7]
print(f"Test Case 1: ", sol.combinationSum(candidates, target))