from typing import Optional

class Node:
    def __init__(self, val =0, neighbors=0):
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