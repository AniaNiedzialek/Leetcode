from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0
    
solution = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(solution.minSubArrayLen(target, nums))
target = 4
nums = [1,4,4]
print(solution.minSubArrayLen(target, nums))
target = 11
nums = [1,1,1]
print(solution.minSubArrayLen(target, nums))