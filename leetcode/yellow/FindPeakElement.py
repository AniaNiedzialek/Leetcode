from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(log n) => binary search algorithm
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (( r - l) // 2) # will not overflow
            # left grater
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            # right greater
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            

            else:
                return m