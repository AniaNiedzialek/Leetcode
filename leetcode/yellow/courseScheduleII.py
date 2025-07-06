from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # step 1 - create a graph
        preMap = {i:[] for i in range(numCourses)}
        print(preMap)

        # step 0 - result
        result = []
        # step 2 - input the values into the grap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)

        # step 3 - set to mark current values to detect cycyles
        visited = set()

        # step 4 - dfs
        def dfs(crs):
            # base case 1 - if there's a cycle
            if crs in visited:
                return []
            # bse case 2 - if the prereq is empty - append courses that dont have the prerequisties
            if preMap[crs] == []:
                if crs not in result:
                    result.append(crs)
                return result
            # otherwise - add to the set since it was visited
            visited.add(crs)
            # check the rest
            for pre in preMap[crs]:
                if not dfs(pre):
                    return []
            result.append(crs)
            visited.remove(crs)
            preMap[crs] = []
            
            return result
        
        # step 5 - call dfs on the rest of the courses
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result