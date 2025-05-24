from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # use DFS 
        # step 1 - base case
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
    
solution = Solution()

    # Test case 1: Empty tree
root1 = None
print("Test case 1 (empty tree):", solution.maxDepth(root1))  # Expected: 0

# Test case 2: Single node
root2 = TreeNode(1)
print("Test case 2 (single node):", solution.maxDepth(root2))  # Expected: 1

# Test case 3: Balanced tree
#      1
#     / \
#    2   3
#   / 
#  4
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
print("Test case 3 (balanced):", solution.maxDepth(root3))  # Expected: 3

# Test case 4: Unbalanced tree
    #      1
    #     /
    #    2
    #   /
    #  3
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.left.left = TreeNode(3)
print("Test case 4 (unbalanced):", solution.maxDepth(root4))  # Expected: 3

# Test case 5: Right-skewed tree
# 1
#  \
#   2
#    \
#     3
root5 = TreeNode(1)
root5.right = TreeNode(2)
root5.right.right = TreeNode(3)
print("Test case 5 (right-skewed):", solution.maxDepth(root5))  # Expected: 3