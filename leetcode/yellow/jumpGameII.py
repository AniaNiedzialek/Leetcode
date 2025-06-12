from typing import List

class Solution:
    
    def jump(self, nums: List[int]) -> int:
        smallest = 0
        end, far = 0, 0

        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])

            if i == end:
                smallest += 1
                end = far

        return smallest

solution = Solution()

print(solution.jump([2,3,1,1,4]))  # Expected: 2
print(solution.jump([1]))  # Expected: 2