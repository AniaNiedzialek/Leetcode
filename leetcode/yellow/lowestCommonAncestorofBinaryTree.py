


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
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    p = root.left
    q = root.right
    solution = Solution()
    print("Test Case 1:", solution.lowestCommonAncestor(root, p, q).val)  # Expected: 1
    
    # test case 2
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)  
    p = root.left  # 5
    q = root.left.right.right  # 7  \
    solution = Solution()
    print("Test Case 2:", solution.lowestCommonAncestor(root, p, q).val)  # Expected: 5
    