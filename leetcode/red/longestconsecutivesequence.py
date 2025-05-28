
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # step 1 - declarations
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest