from typing import List, Optional

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res
    
solution = Solution()
print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Expected: 3 
print(solution.canCompleteCircuit([2,3,4], [3,4,3]))  # Expected: -1                
print(solution.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))  # Expected: 4
print(solution.canCompleteCircuit([1,2,3,4], [2,3,4,3]))  # Expected: 0
print(solution.canCompleteCircuit([1,2,3], [2,3,4]))  # Expected: -1            
    