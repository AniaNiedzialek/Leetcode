from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        arr = [0] * len(nums) # additional memory
        last_elem = len(nums) - 1
        j = 1

        if len(nums) == 0:
            return
        #  to normalize k for rotation
        k = k % len(nums)
        # i need to have this as a shifting value
        for i in range(1, k + 1):
            temp = nums[len(nums) - i]
            if j <= k:
                arr[k-j] = temp
                j += 1
        else:
            for z in range(0, len(nums) - k):
                arr[j - 1] = nums[z]
                j += 1
        nums[:] = arr

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Before rotation:", nums)
    solution.rotate(nums, k)
    print("After rotation:", nums)



