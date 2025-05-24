
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # step 1 - base case
        if not root:
            return None
        # step 2 - inverting
        root.left, root.right = root.right, root.left
        # step 3 - recursively call the method
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root