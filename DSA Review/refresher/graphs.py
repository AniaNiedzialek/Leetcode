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
    # D[u].append(v)
    
    D[u].append(v)

print(D)

print(D[3])
print(M[3])


# undirected graph