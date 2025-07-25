from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)
            
        return sum(arr)

solution = Solution()
print(solution.candy([1,0,2]))  # Expected: 5
print(solution.candy([1,2,2]))  # Expected: 4
print(solution.candy([1,3,2,2,1]))  # Expected: 9   