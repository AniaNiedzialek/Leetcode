from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS - check if same structure and same values

        def balances(p,q):
            # step 1 - base case
            if not p and not q: # both are invalid entries
                return True
            # step 2 - if either is invalid
            if (not p and q) or (p and not q):
                return False
            # step 3 - check if different values
            if p.val != q.val:
                return False
            return balances(p.left, q.left) and balances(p.right, q.right)
        
        return balances(p, q)