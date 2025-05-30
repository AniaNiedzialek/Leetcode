from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        

        def dfs(root, current, result):
            # step 1 - base case
            if not root:
                return None
            
            # step 2 - adjust the current
            current = current * 10 + root.val

            # step 3 - if at the leaf
            if not root.left and not root.right:
                result.append(current)

            # step 4 - recursively call the rest of the nodes
            dfs(root.left, current, result)
            dfs(root.right, current, result)

        dfs(root, 0, result)
        total = sum(result)
        return total
