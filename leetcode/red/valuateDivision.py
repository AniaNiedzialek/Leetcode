from typing import List
import collections
from collections import deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            # base case - specific to the description
            if src not in adj or target not in adj:
                return - 1
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
# bfs implementation
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, weight * w])
                        visit.add(nei)

            return -1

# list comprehension
        return [bfs(q[0], q[1]) for q in queries]




# test cases
solution = Solution()
# ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic example
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(solution.calcEquation(equations1, values1, queries1))
    # Expected: [6.0, 0.5, -1.0, 1.0, -1.0]

    # Test case 2: Disconnected variables
    equations2 = [["x", "y"], ["y", "z"]]
    values2 = [4.0, 2.0]
    queries2 = [["x", "z"], ["z", "x"], ["x", "w"], ["w", "w"]]
    print(solution.calcEquation(equations2, values2, queries2))
    # Expected: [8.0, 0.125, -1.0, -1.0]

    # Test case 3: Self division
    equations3 = [["a", "b"]]
    values3 = [5.0]
    queries3 = [["a", "a"], ["b", "b"], ["a", "b"], ["b", "a"]]
    print(solution.calcEquation(equations3, values3, queries3))
    # Expected: [1.0, 1.0, 5.0, 0.2]

    # Test case 4: No equations
    equations4 = []
    values4 = []
    queries4 = [["a", "b"], ["b", "a"]]
    print(solution.calcEquation(equations4, values4, queries4))
    # Expected: [-1.0, -1.0]