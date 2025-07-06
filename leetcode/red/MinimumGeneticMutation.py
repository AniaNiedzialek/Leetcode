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
