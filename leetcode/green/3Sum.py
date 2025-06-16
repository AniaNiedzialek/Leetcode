
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []


        for i in range(n):
            # base case 1 -  if nums[i] > 0:
            if nums[i] > 0:
                break
            # base case 2 - if i is bigger than zero but the next entry is the same
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            # lo and hi
            lo, hi =  i + 1, n - 1
            while lo < hi:
                # get the sum
                summ = nums[i] + nums[lo] + nums[hi]
                # case 1 - we found the result
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    # case 1 - if the next number for lo is the same as current
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
            





        return answer

solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([0, 1, 1]))  # Output: []
print(solution.threeSum([0, 0, 0]))  # Output: [[0, 0, 0]]
print(solution.threeSum([-2, 0, 1, 1, 2]))  # Output: [[-2, 0, 2], [-2, 1, 1]]
print(solution.threeSum([-4, -2, 1, 2, 3, 5]))  # Output: [[-4, 1, 3], [-2, -2, 4]]             