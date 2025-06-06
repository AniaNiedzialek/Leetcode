from typing import Optional, List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(nums)  
    # step 1 - sort in order
    # step 2 - traverse the new array 
        # step 3 - return the vale at index k
        # new_list = [0] * len(nums)

        def heapsort(nums):
            nums = [-x for x in nums]

            heapq.heapify(nums)
            new_list = [0] * len(nums)

            for i in range(len(nums)):
                
                new_list[i] = -  heapq.heappop(nums)
            # print(new_list)
            # print(new_list)

            return (new_list)
        sorted_list = heapsort(nums)
        return sorted_list[k - 1]
        # def reverse(nums):
        
        