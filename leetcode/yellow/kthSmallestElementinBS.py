class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        val = []
        
        # inorder traversal
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            val.append(root.val)
            inorder(root.right)
            
        inorder(root)
        for i in range(len(val)):
            return val[k-1]
        
if __name__ == "__main__":
    # Example test case:
    # Tree:   3
    #        / \
    #       1   4
    #        \
    #         2
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    solution = Solution()
    print(solution.kthSmallest(root, 1))  # Expected: 1
    print(solution.kthSmallest(root, 2))  # Expected: 2
    print(solution.kthSmallest(root, 3))  # Expected: 3
    print(solution.kthSmallest(root, 4))  # Expected: 4
    # print(solution.kthSmallest(root, 5))  # Expected: None (if k is out of bounds)
