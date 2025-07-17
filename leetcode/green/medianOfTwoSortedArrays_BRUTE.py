from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        res = 0
        combined = []
        combined += nums1
        combined += nums2
        combined.sort()
        print(combined)
        l, r = 0, len(combined) - 1
        print(l, r)

        mid = (l + r) // 2
        print(f"mid is {mid}, l is {l}, r is {r}, {combined[l]}, {combined[r]}")
        print(mid)

        for i in combined:
            if len(combined) % 2 == 1:
                print(f"hello")
                res = combined[mid]

            else:
                print(f"{mid} is {combined[mid]}")
                res = (combined[mid] + combined[mid + 1]) / 2

        
            

        return res