from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res # xor
        return res
    
# ...existing code...

if __name__ == "__main__":
    solution = Solution()
    # Test case 1: Only one unique number
    print(solution.singleNumber([2,2,1]))  # Expected: 1

    # Test case 2: Unique number at the end
    print(solution.singleNumber([4,1,2,1,2]))  # Expected: 4

    # Test case 3: Only one element
    print(solution.singleNumber([1]))  # Expected: 1

    # Test case 4: Negative numbers
    print(solution.singleNumber([-1, -1, -2]))  # Expected: -2

    # Test case 5: Larger array
    print(solution.singleNumber([10, 10, 20, 30, 20]))  # Expected: 30