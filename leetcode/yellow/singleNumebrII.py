from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):  # check all 32 bits
            bit_sum = 0
            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1
            if bit_sum % 3 != 0:
                res |= (1 << i)
        
        # handle negative numbers (32-bit signed int)
        if res >= 2**31:
            res -= 2**32
        return res
 