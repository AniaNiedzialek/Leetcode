from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)

        half = total // 2
        # only run binary serach on one of them - the smaller one

        if len(B) < len(A):
            A, B = B, A
      

        l, r = 0, len(A) - 1
         # half - total elements in left partition
         
        while True:
            # mid pointer for A
            i = (l + r) // 2

            # pointer for B
            j = half - i - 2 # arrayss are indexed at 0, j starts at 0 and i too so we need -2

            # if statmenets to avoid edge cases
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")


            if Aleft <= Bright and Bleft <= Aright:
                # left partition is correct
                # odd number of elements
                if total % 2:
                    #compute median
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                # edge case 2
            elif Aleft > Bright:
                # too many elements from A
                r = i - 1
                # reduce the size of L partiion
            else:
                l = i + 1
            


  