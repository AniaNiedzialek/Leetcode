from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)
        min_diff = float('inf')
        for i in range(1, len(vals)):
            min_diff = min(min_diff, vals[i] - vals[i-1])
        return min_diff if vals else 0

# Example test case:
if __name__ == "__main__":
    # Tree:   4
    #        / \
    #       2   6
    #      / \
    #     1   3
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    solution = Solution()
    print(solution.getMinimumDifference(root))  # Expected: 1