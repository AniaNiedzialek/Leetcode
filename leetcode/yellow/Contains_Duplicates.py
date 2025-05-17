# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

from typing import List

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         print(f"nums is : {nums}")

#         size = len(nums)
#         i = 0
#         # j = i + 1

#         for i  in range(size):
#             for j in range(i + 1, size):
#                 print(f"i is {i}, nums[i] is {nums[i]} || j is {j}, nums[j]: {nums[j]}")

#                 if nums[i] == nums[j]:
#                     print(f"i is {i}, j is {j}")
#                     print(f"nums[i]: {nums[i]}, nums[j]: {nums[j]}")
#                     return True
#                 # else:
#                 #     i += 1
    
#         return False

# MORE EFFICIENT SOLUTION - O(n):
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True  
            seen.add(nums[i])  

        return False

    
solution = Solution()
nums = [1, 2, 3, 3]
print(solution.hasDuplicate(nums))  # Output: True
