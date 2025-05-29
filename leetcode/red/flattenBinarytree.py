
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            # step 1 - base case:
            if not root:
                return None
            # otherwise check the recursion
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # step 2 - only need to check the left side
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            last = rightTail or leftTail or root
            return last
        dfs(root)