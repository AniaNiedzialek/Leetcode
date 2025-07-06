from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detecting cycles in a graph
        
        # dfs algorithm to check the empty course without any prepreqs
        
        # create a graph
        # map each course to the preMap
        preMap = {i:[] for i in range(numCourses)}


        # course and prereq pair in prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # to store all the courses along the current dfs path
        visit = set()
        def dfs(crs):
            # base case
            if crs in visit:
                return False
            # base case 2 - if prereq is an empty list
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
                # remove from visit set
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        