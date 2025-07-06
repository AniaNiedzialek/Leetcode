from typing import List
import collections
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        print(bank)

        if endGene not in bank:
            return -1

        def bfs():
            visited = set()
            q = collections.deque()
            q.append((startGene, 0))
            visited = {startGene}
            while q:
                gene, level = q.popleft()
                if gene == endGene:
                    return level
                for i in range(len(gene)):
                    for letter in 'AGTC':
                        new_gene = gene[:i] + letter + gene[i + 1 :]
                        if new_gene not in visited and new_gene in bank:
                            q.append((new_gene, level + 1))
                            visited.add(new_gene)
            return -1
        return bfs()
# ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from LeetCode
    start1 = "AACCGGTT"
    end1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    print(solution.minMutation(start1, end1, bank1))  # Expected: 1

    # Test case 2: Two mutations needed
    start2 = "AACCGGTT"
    end2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(solution.minMutation(start2, end2, bank2))  # Expected: 2

    # Test case 3: No possible mutation
    start3 = "AAAAACCC"
    end3 = "AACCCCCC"
    bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(solution.minMutation(start3, end3, bank3))  # Expected: 3

    # Test case 4: End gene not in bank
    start4 = "AACCGGTT"
    end4 = "AAACGGTA"
    bank4 = ["AACCGGTA", "AACCGCTA"]
    print(solution.minMutation(start4, end4, bank4))  # Expected: -1

    # Test case 5: Start equals end
    start5 = "AACCGGTT"
    end5 = "AACCGGTT"
    bank5 = ["AACCGGTT"]
    print(solution.minMutation(start5, end5, bank5))  # Expected: 0