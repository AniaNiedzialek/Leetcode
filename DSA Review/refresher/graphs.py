# array of edges (directed))
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4,], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

print(A)

# convert array of edged to adjacency matrix

M = []
for i in range(n):
    M.append([0] * n)
    
# print(M)

for u, v in A:
    # for directed graph
    M[u][v] = 1
    # for undirected graph
    # M[v][u] = 1
# print(M)

# convert array of edges to adjacency list
from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    
    # D[u].append(v)

print(D)

print(D[3])
print(M[3])

# DFS with recursion  - O(V + E) where V is numbers of nodes and E is number oF edges

def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

source = 0
seen = set()
seen.add(source)
dfs_recursive(source)


# dfs with stack
source = 0
seen = set()
seen.add(source)
stack = [source] 

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)
            
            
# BFS  with queue

source = 0

from collections import deque
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)

# class
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # fixed typo: was 'neighors'
    
    def __str__(self):
        return f'Node({self.value})'  # fixed typo: was 'valeue'

    def display(self):
        connections = [node.value for node in self.neighbors]
        return f'{self.value} is connected to {connections}'

A = Node('A')
B = Node('B')
C = Node('C')       
D = Node('D')

A.neighbors.append(B)  # fixed typo: was 'neighors'
B.neighbors.append(D)
C.neighbors.append(D) 
D.neighbors.append(C)

print(A.display())  # Output: A is connected to ['B']
