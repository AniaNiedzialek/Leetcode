from typing import List

class Solution:
    def maxSubarry(self, nums: List[str]) -> List[str]:
        max_sum = float("-inf")
        cur_sum = 0

        for n in nums:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(max_sum, cur_sum)

        return max_sum
    
    
    
# test cases
solution = Solution()
num1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Test Case 1: ", solution.maxSubarry(num1))  # expected: 6

 # 2
num2 = [0]
print(f"Test Case 2: ", solution.maxSubarry(num2)) #expected: 0

# 3
num3 = [1, -2, -4, -3, -9, 0, 1] 
print(f"Test Case 3: ", solution.maxSubarry(num3)) # expected 1