from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print(f"nums is {nums}")
        position = 0
        size = len(nums)
        last_elem = size - 1
        option = 0  # max index reachable so far

        while position <= option:
            print(f"At index {position}, jump = {nums[position]}")
            option = max(option, position + nums[position])
            print(f"New option (max reachable) is {option}")

            if option >= last_elem:
                return True

            position += 1

        return False


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Can reach the end
    nums1 = [2, 3, 1, 1, 4]
    print("Test case 1:", solution.canJump(nums1))  # Expected: True

    # Test case 2: Cannot reach the end
    nums2 = [3, 2, 1, 0, 4]
    print("Test case 2:", solution.canJump(nums2))  # Expected: False

    # Test case 3: Single element (already at the end)
    nums3 = [0]
    print("Test case 3:", solution.canJump(nums3))  # Expected: True

    # Test case 4: All zeros except the first
    nums4 = [1, 0, 0, 0]
    print("Test case 4:", solution.canJump(nums4))  # Expected: False

    # Test case 5: Large jump at the start
    nums5 = [5, 0, 0, 0, 0]
    print("Test case 5:", solution.canJump(nums5))  # Expected: True

    # Test case 6: Edge case, last jump is just enough
    nums6 = [2, 0, 0]
    print("Test case 6:", solution.canJump(nums6))  # Expected: True
