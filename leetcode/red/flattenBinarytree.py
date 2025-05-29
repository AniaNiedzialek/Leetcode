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

def print_flattened_list(root):
    """Helper to print the flattened tree as a list."""
    result = []
    while root:
        result.append(root.val)
        root = root.right
    print(result)

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example tree
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    root1 = TreeNode(1,
                     TreeNode(2, TreeNode(3), TreeNode(4)),
                     TreeNode(5, None, TreeNode(6)))
    solution.flatten(root1)
    print("Test case 1 (flattened):")
    print_flattened_list(root1)  # Expected: [1, 2, 3, 4, 5, 6]

    # Test case 2: Single node
    root2 = TreeNode(1)
    solution.flatten(root2)
    print("Test case 2 (single node):")
    print_flattened_list(root2)  # Expected: [1]

    # Test case 3: Empty tree
    root3 = None
    solution.flatten(root3)
    print("Test case 3 (empty tree):")
    print_flattened_list(root3)  # Expected: []