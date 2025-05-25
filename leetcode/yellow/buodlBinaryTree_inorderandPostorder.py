from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # step 1 - base case
        if not inorder or not postorder:
            return None
        # step 2 -  find root
        value = postorder.pop()
        root = TreeNode(value)
        # step 3 - find root in inorder
        mid = inorder.index(value)
        # step 4 - recursively build the tree
        root.right = self.buildTree(inorder[mid + 1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        return root