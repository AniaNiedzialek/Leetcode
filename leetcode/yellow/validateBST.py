
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val = []
        def inorder(root):
            if not root:
                return False
            inorder(root.left)
            val.append(root.val)
            inorder(root.right)
        # print(root)
        inorder(root)
        print(val)

        for i in range(1, len(val)):
            if val[i] <= val[i - 1]:
                return False

        return True
    
    
# ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Valid BST
    #     2
    #    / \
    #   1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print("Test case 1 (valid BST):", solution.isValidBST(root1))  # Expected: True

    # Test case 2: Invalid BST
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print("Test case 2 (invalid BST):", solution.isValidBST(root2))  # Expected: False

    # Test case 3: Single node
    root3 = TreeNode(1)
    print("Test case 3 (single node):", solution.isValidBST(root3))  # Expected: True

    # Test case 4: Empty tree
    root4 = None
    print("Test case 4 (empty tree):", solution.isValidBST(root4))  # Expected: True