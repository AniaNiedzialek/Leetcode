from typing import Optional

class Node:
    def __init__(self, val =0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        


class Solution():
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # hashmap to store and retrive the nodes
        old = {}
        
        # dfs
        def dfs(node):
            # base case - if already exists
            if node in old:
                return old[node]
            
            # otherwise
            # create a copy of the node - new Node instance
            copy = Node(node.val)
            # add the copy to the hashmap before recursion
            old[node] = copy
            
            # check neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
    
def build_graph(adj_list):
    if not adj_list:
        return None
    nodes = [Node(i+1) for i in range(len(adj_list))]
    for idx, neighbors in enumerate(adj_list):
        nodes[idx].neighbors = [nodes[n-1] for n in neighbors]
    return nodes[0]

# test cases
solution = Solution()
# case1 = [[2,4],[1,3],[2,4],[1,3]]
adj_list = [[2,4],[1,3],[2,4],[1,3]]
root = build_graph(adj_list)
cloned = solution.cloneGraph(root)
print(cloned.val)  # Should print 1 (the value of the root node)

# Print original and cloned root node values and ids
print("Original root val:", root.val, "id:", id(root))
print("Cloned root val:", cloned.val, "id:", id(cloned))

# Check neighbors of root
print("Original neighbors:", [n.val for n in root.neighbors])
print("Cloned neighbors:", [n.val for n in cloned.neighbors])
print("Original neighbor ids:", [id(n) for n in root.neighbors])
print("Cloned neighbor ids:", [id(n) for n in cloned.neighbors])

# Check that the objects are different
print("Root nodes are different objects:", root is not cloned)
print("First neighbor nodes are different objects:", root.neighbors[0] is not cloned.neighbors[0])