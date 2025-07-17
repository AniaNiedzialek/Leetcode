from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        res = 0
        combined = []
        combined += nums1
        combined += nums2
        combined.sort()
        l, r = 0, len(combined) - 1

        mid = (l + r) // 2

        for i in combined:
            if len(combined) % 2 == 1:
           
                res = combined[mid]

            else:
                res = (combined[mid] + combined[mid + 1]) / 2

        
            

        return res
    
# test case
solutuion = Solution()
nums1 = [1, 3]
nusm2 = [2]
print(f"Test Case 1: ", solutuion.findMedianSortedArrays(nums1, nusm2))  # expected: 2.0