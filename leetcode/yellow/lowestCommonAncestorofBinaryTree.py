


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # step 1 - base case
        if not root:
            return None
        # step 2 - if node found at the root
        if root == p or root == q:
            return root
        # step 3 - recursively traverse the entire tree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # step 4 - if the left or right is non null
        if left and right:
            return root
        else:
            return left or right