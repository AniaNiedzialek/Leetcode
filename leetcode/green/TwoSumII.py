from typing import List  
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        print(f"left: {l}, right {r}")
        print(f"sum is {numbers[l] + numbers[r]}" )
        while l < r:
            if numbers[l] + numbers[r]== target:
                return [l + 1, r + 1]
            elif numbers[l] +  numbers[r] < target:
                l += 1
            else:
                r -= 1