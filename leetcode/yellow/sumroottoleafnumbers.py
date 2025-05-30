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
# ...existing code...

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example tree
    #     1
    #    / \
    #   2   3
    # Numbers: 12, 13 => sum = 25
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Test case 1:", solution.sumNumbers(root1))  # Expected: 25

    # Test case 2: Tree with more levels
    #      4
    #     / \
    #    9   0
    #   / \
    #  5   1
    # Numbers: 495, 491, 40 => sum = 495 + 491 + 40 = 1026
    root2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    print("Test case 2:", solution.sumNumbers(root2))  # Expected: 1026

    # Test case 3: Single node
    root3 = TreeNode(7)
    print("Test case 3:", solution.sumNumbers(root3))  # Expected: 7

    # Test case 4: Empty tree
    root4 = None
    print("Test case 4:", solution.sumNumbers(root4))  # Expected: 0