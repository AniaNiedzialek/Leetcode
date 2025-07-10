from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    
    # helper function
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1

        return i

# ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Target appears multiple times
    nums1 = [5,7,7,8,8,10]
    target1 = 8
    print(solution.searchRange(nums1, target1))  # Expected: [3, 4]

    # Test case 2: Target not present
    nums2 = [5,7,7,8,8,10]
    target2 = 6
    print(solution.searchRange(nums2, target2))  # Expected: [-1, -1]

    # Test case 3: Target is the only element
    nums3 = [2,2,2,2,2]
    target3 = 2
    print(solution.searchRange(nums3, target3))  # Expected: [0, 4]

    # Test case 4: Empty array
    nums4 = []
    target4 = 0
    print(solution.searchRange(nums4, target4))  # Expected: [-1, -1]

    # Test case 5: Target at the beginning
    nums5 = [1,2,3,4,5]
    target5 = 1
    print(solution.searchRange(nums5, target5))  # Expected: [0, 0]

    # Test case 6: Target at the end
    nums6 = [1,2,3,4,5]
    target6 = 5
    print(solution.searchRange(nums6, target6))  # Expected: [4, 4]