from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 2 heap problem
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]

        heapq.heapify(minCapital) # min heap
        
        for i in range(k):

            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p) # to make a max heap
            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)
        return w