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
    
    
# test cases

 # ...existing code...

if __name__ == "__main__":
    solution = Solution()
    # Test case 1: Positive numbers
    print(solution.singleNumber([2,2,3,2]))  # Expected: 3

    # Test case 2: Negative number
    print(solution.singleNumber([0,1,0,1,0,1,-99]))  # Expected: -99

    # Test case 3: Single element
    print(solution.singleNumber([7]))  # Expected: 7

    # Test case 4: All numbers are the same except one
    print(solution.singleNumber([5,5,5,8]))  # Expected: 8

    # Test case 5: Larger array with negative unique
    print(solution.singleNumber([-2,-2,-2,-7]))  # Expected: -7