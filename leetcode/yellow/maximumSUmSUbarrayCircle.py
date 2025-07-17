from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        cur_max = cur_min = max_sum = min_sum = nums[0]
        for n in nums[1:]:
            cur_max = max(n, cur_max + n)
            max_sum = max(max_sum, cur_max)

            cur_min = min(n, cur_min + n)
            min_sum = min( cur_min, min_sum)

            total += n
        total += nums[0]

        if max_sum < 0:
            return max_sum
        else:
            return max(max_sum, total - min_sum)


# test cases
solution = Solution()
nusm1 = [-3, -5, -3]
print(f"Test Case 1: ", solution.maxSubarraySumCircular(nusm1)) # expected: -3
        