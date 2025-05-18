from typing import List 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        new_arr = sorted(citations)
        cit = list(reversed(new_arr))
        print(f"{cit}")
        h = 1

        print(f"papers {papers}, sort {new_arr}")

        if cit[0] == 0:
                return 0

        # improved logic:
        # if all(c == 0 for c in citations):
        #     return 0

        for i in range(papers - 1):
            if cit[i + 1] > i + 1:
                h += 1
            # print(f"h is {h}")
        return h
    
if __name__ == '__main__':
    solution = Solution()
    citations = [3,0,6,1,5]
    print(f"Output is: ", solution.hIndex(citations))
    
    citations2 = [1,3,1]
    print("Output is: ", solution.hIndex(citations2))