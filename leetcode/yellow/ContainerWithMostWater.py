from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        size = len(height)
        i = 0
        j = size - 1
        max_area = 0

        while i < j:
            h = min(height[j], height[i])
            width = j - i
            area = h * width
            max_area = max(max_area, area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
    
if __name__ == "__main__":
    solution = Solution()
     # Test case 1
    heights1 = [1,8,6,2,5,4,8,3,7]
    print("Test case 1:", solution.maxArea(heights1))  # Expected: 49

    # Test case 2
    heights2 = [1,1]
    print("Test case 2:", solution.maxArea(heights2))  # Expected: 1

    # Test case 3
    heights3 = [4,3,2,1,4]
    print("Test case 3:", solution.maxArea(heights3))  # Expected: 16

    # Test case 4
    heights4 = [1,2,1]
    print("Test case 4:", solution.maxArea(heights4))  # Expected: 2

    # Test case 5 (edge case: only one line)
    heights5 = [5]
    print("Test case 5:", solution.maxArea(heights5))  # Expected: 0
    