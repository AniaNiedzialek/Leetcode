from typing import List

class Solution:
    def maxSubarry(self, nums: List[str]) -> List[str]:
        max_sum = flaot("-inf")
        cur_sum = 0

        for n in nums:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(max_sum, cur_sum)

        return max_sum