
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # step 1 - base case
        if not preorder or not inorder:
            return None
        # step 2 - find the root
        root = TreeNode(preorder[0])
        # step 3 - find the root in the the inorder
        mid = inorder.index(preorder[0])
        # step 4 - recursively build tree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
