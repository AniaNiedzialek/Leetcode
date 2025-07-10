from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # leftmost
        res = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1 
            else:
                r = m - 1
        
        return res
    
    # test cases
    # ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Rotated array
    nums1 = [3,4,5,1,2]
    print(solution.findMin(nums1))  # Expected: 1

    # Test case 2: Not rotated
    nums2 = [1,2,3,4,5]
    print(solution.findMin(nums2))  # Expected: 1

    # Test case 3: Rotated at last element
    nums3 = [2,3,4,5,1]
    print(solution.findMin(nums3))  # Expected: 1

    # Test case 4: Single element
    nums4 = [10]
    print(solution.findMin(nums4))  # Expected: 10

    # Test case 5: Two elements, rotated
    nums5 = [2,1]
    print(solution.findMin(nums5))  # Expected: 1

    # Test case 6: Two elements, not rotated
    nums6 = [1,2]
    print(solution.findMin(nums6))  # Expected: 1